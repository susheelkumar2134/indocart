from django.shortcuts import render,redirect
from indoapp.models import IndoUsers
from indoapp.forms import RegistrationForm
from django.contrib.auth import logout
from django.conf import settings
from django.core.mail import send_mail,EmailMultiAlternatives
# Create your views here.

# def SendEmail(Email):
#     subject='This is from scoutgym .'
#     message='You are successfully register'
#     from_email=settings.EMAIL_HOST_USER
#     recipient_list=[Email]
#     send_mail(subject,message,from_email,recipient_list)

def SendEmailHTML(Email):
    subject='This is from Indocart.'
    msg= f'''<h1> Welcome to Indocart </h1>
                <p> Congrats and Thank you for your registration on scoutgym. This is your {Email} email address.<br>
                This email address will help you login on our platform, just enter your email in username box
                and enter your password.</p>
                <span style='color:red'> please don't reply for this email.</span>'''
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[Email]
    message=EmailMultiAlternatives(subject,msg,from_email,recipient_list)
    message.content_subtype='html'
    message.send()

def index(request):
    return render(request,'Index.html')

def registration(request):
    # success=''
    if request.method == 'POST':
        Form=RegistrationForm(request.POST)
        Email = request.POST.get('Email')
        FindUser= IndoUsers.objects.filter(Email=Email)
        if FindUser:
            Error='Email is already Exist. Please enter another email.'
            return render(request,"registration.html",{"registrationform":Form,'error':Error})
        else:
             if Form.is_valid:
                try:
                    Form.save()
                    Success=" You are register succesfully. Now you can login here with your Email and Password. "
                    SendEmailHTML(Email)
                    return render(request,'login.html',{'success':Success})
                except:
                    pass
    else:
        Form=RegistrationForm()
    return render(request,'registration.html',{'registrationform':Form})

def login_view(request):
    if request.method == 'POST':
        Email=request.POST.get('email')
        Password=request.POST.get('password')
        FindUser=IndoUsers.objects.filter(Email=Email,Password=Password)
        FindUser2=IndoUsers.objects.filter(Email=Email,Password=Password).first()
        if FindUser:
            return render(request,'Index.html',{'user':FindUser,'user2':FindUser2})
        else:
            Error='Username or password not match. Please enter correct details.'
            return render(request,"login.html",{'error':Error})
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def cart(request):
    return render(request,'cart.html')
