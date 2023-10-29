from django.shortcuts import render,redirect
from indoapp2.models import IndoUsers,Products,DeliveryDetails,KartProducts,PlacedOrder
from indoapp2.forms import RegistrationForm ,DeliveryForm
from django.contrib.auth import logout
from django.conf import settings
from django.core.mail import send_mail,EmailMultiAlternatives
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

# git remote add origin https://github.com/susheelkumar2134/indocart.git
# git branch -M main
# git push -u origin main

# def SendEmail(Email):
#     subject='This is from scoutgym .'
#     message='You are successfully register'
#     from_email=settings.EMAIL_HOST_USER
#     recipient_list=[Email]
#     send_mail(subject,message,from_email,recipient_list)

def RegistrationSendEmailHTML(Email):
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

def LoginSendEmailHTML(Email):
    subject='This is from Indocart.'
    msg= f'''<h1> You are login successfully into Indocart </h1>
                <p> Thanku to be a part of indocart. This is your email address {Email}.</p>
                <b><span style='color:red;'> please don't reply for this email.</span></b>'''
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[Email]
    message=EmailMultiAlternatives(subject,msg,from_email,recipient_list)
    message.content_subtype='html'
    message.send()
    
# def login_required(request,funs):
#     def login_check():
#         if 'username' in request.session:
#             funs()
#             return login_required()
#         else:
#             return redirect('cart')
#     return login_check
        

def index(request):
    username=None
    products=Products.objects.all()
    sp=request.POST.get("searchproduct")
    search_products=Products.objects.filter(Q(ProductName=sp) | Q(ProductCategory=sp) | Q(ProductBrand=sp))
    try:
        username=request.session['username']
        return render(request,'Index.html',{'user2':username,'products':products,'search_products':search_products})
    except:
        pass
    return render(request,'Index.html',{'user2':username,'products':products,'search_products':search_products})

def registration(request):
    sp=request.POST.get("searchproduct")
    search_products=Products.objects.filter(Q(ProductName=sp) | Q(ProductCategory=sp) | Q(ProductBrand=sp))
    if request.method == 'POST':
        Form=RegistrationForm(request.POST)
        Email = request.POST.get('Email')
        FindUser= IndoUsers.objects.filter(Email=Email)
        if FindUser:
            Error='Email is already Exist. Please enter another email.'
            return render(request,"registration.html",{"registrationform":Form,'error':Error,'search_products':search_products})
        else:
             if Form.is_valid:
                try:
                    Form.save()
                    RegistrationSendEmailHTML(Email)
                    return redirect('login')
                except:
                    pass
    else:
        Form=RegistrationForm()
    return render(request,'registration.html',{'registrationform':Form,'search_products':search_products})

def loginview(request):
    username=None
    products=Products.objects.all()
    sp=request.POST.get("searchproduct")
    search_products=Products.objects.filter(Q(ProductName=sp) | Q(ProductCategory=sp) | Q(ProductBrand=sp))
    if request.method == 'POST':
        Email=request.POST.get('email')
        Password=request.POST.get('password')
        FindUser=IndoUsers.objects.filter(Email=Email,Password=Password)
        FindUser2=IndoUsers.objects.filter(Email=Email,Password=Password).first()
        # FindUser3=IndoUsers.objects.filter(Email=Email,Password=Password).get() # FinderUser2 and FndUser3 both queryset work same. But not FinUser.
        if FindUser:
            request.session['username'] = FindUser2.FirstName
            request.session['email'] = FindUser2.Email
            request.session['useraddressid']=FindUser2.id
            print(FindUser2.id)
            username=request.session['username']
            LoginSendEmailHTML(Email)
            return render(request,'Index.html',{'user':FindUser,'user2':username,'products':products,'search_products':search_products})
        else:
            Error='Username or password not match. Please enter correct details.'
            return render(request,"login.html",{'user2':username,'error':Error,'search_products':search_products})
    else:
        pass
    return render(request,'login.html',{'user2':username,'search_products':search_products})

def logoutview(request):
    if 'username' in request.session:
        try:
            del request.session['username']
            del request.session['email']
            del request.session['useraddressid']
            del request.session["productid"]
        except:
            pass
        logout(request)
    return redirect('index')

def cart(request):
    tem=[]
    user_id=None
    amount=0.0
    shipping_amount=40.0
    try:
        user_id=request.session["useraddressid"]
        # if request.method == "GET":
        # prod_id = request.GET['pid']            
        # print("This is productss",prod_id)
    except:
        pass
    username=None
    cart_products=None
    sp=request.POST.get("searchproduct")
    search_products=Products.objects.filter(Q(ProductName=sp) | Q(ProductCategory=sp) | Q(ProductBrand=sp))
    cart_products=KartProducts.objects.filter(user=user_id)
    try:
        username=request.session['username']
        product_id=request.session["productid"]
        p=Products.objects.filter(id=product_id).get()
        cheek=KartProducts.objects.filter(product=product_id).exists()
        # return render(request,'cart.html',{'user2':username,'search_products':search_products,"cart_products":cart_products})
        if cheek == False:
            k=KartProducts(user=user_id,product=product_id,quantity=1,ProductName=p.ProductName,ProductDetails=p.ProductDetails,ProductPrice=p.ProductPrice,ProductCategory=p.ProductCategory,ProductImage=p.ProductImage)
            k.save()
            cart_products=KartProducts.objects.filter(user=user_id)
            for p in cart_products:
                    tem_amount= p.quantity * p.ProductPrice
                    tem.append(p.ProductPrice)
                    amount += tem_amount
                    total_amount=shipping_amount + amount
                    # print(tem_amount)
            # print(cart_products)
            return render(request,'cart.html',{'user2':username,'search_products':search_products,"cart_products":cart_products,"tem_amount":tem,'totalamount':total_amount,'amount':amount})
        # return render(request,'cart.html',{'user2':username,'search_products':search_products,"cart_products":cart_products})     
    except:
        pass
    cart_products=KartProducts.objects.filter(user=user_id)
    if cart_products:
        for p in cart_products:
            tem_amount=p.quantity * p.ProductPrice
            tem.append(p.ProductPrice)
            amount += tem_amount
            total_amount=shipping_amount + amount
        return render(request,'cart.html',{'search_products':search_products,'user2':username,"cart_products":cart_products,"tem_amount":tem,'totalamount':total_amount,'amount':amount})
    return render(request,'cart.html',{'search_products':search_products,'user2':username})

def cart_quan(request):
    tem=[]
    user_id=None
    amount=0.0
    total_amount=0.0
    shipping_amount=40.0
    data={}
    try:
        user_id=request.session["useraddressid"]
    except:
        pass
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        prod_quan = request.GET['prod_quantity']            
        print("This is productss",prod_id,prod_quan,user_id)
        c=KartProducts.objects.filter(user=user_id,product=prod_id).first()
        print(c)
        c.quantity=prod_quan
        c.save()
    cart_products=KartProducts.objects.filter(user=user_id)
    if cart_products:
        for p in cart_products:
            tem_amount=p.quantity * p.ProductPrice
            tem.append(p.ProductPrice)
            amount += tem_amount
            total_amount=shipping_amount + amount  
        data={"tem_amount":tem,'totalamount':total_amount,'amount':amount}
    return JsonResponse(data)


def remove_cart(request):
    user_id=None
    cart_products=None
    amount=0.0
    total_amount=0.0
    shipping_amount=40.0
    data={}
    try:
        user_id=request.session["useraddressid"]
    except:
        pass

    if request.method == 'GET':
            prod_id = request.GET['prod_id']           
            print("This is productss",prod_id,user_id)
            c=KartProducts.objects.filter(user=user_id,id=prod_id).first()
            c.delete() 
            request.session["productid"]=0
            print("work done")
    cart_products=KartProducts.objects.filter(user=user_id)
    print(cart_products)
    if cart_products:
        for p in cart_products:
            tem_amount=p.quantity * p.ProductPrice
            amount += tem_amount
            total_amount=shipping_amount + amount  
        data={'totalamount':total_amount,'amount':amount}
        return JsonResponse(data)
    else:
        data={'totalamount':total_amount,'amount':amount}
    return JsonResponse(data)

#
def placeorder(request):
    user_id=None
    cart_products=None
    amount=0.0
    total_amount=0.0
    shipping_amount=40.0
    try:
        user_id=request.session["useraddressid"]
    except:
        pass
    cart_products=KartProducts.objects.filter(user=user_id)
    if cart_products:
        for p in cart_products:
            tem_amount=p.quantity * p.ProductPrice
            amount += tem_amount
            total_amount=shipping_amount + amount  
    alladdress=DeliveryDetails.objects.filter(user=user_id)
    return render(request,"placeorder.html",{"cart_products":cart_products,"alladdress":alladdress,"total_amount":total_amount})

def order(request):
    user_id=request.session["useraddressid"]
    order=PlacedOrder.objects.filter(user=user_id)
    return render(request,"ordercomplete.html",{"order":order})

def payment_done(request):
    user_id=request.session["useraddressid"]
    cart_products=KartProducts.objects.filter(user=user_id)
    custid= request.GET['custid']
    for c in cart_products:
       PlacedOrder(user=user_id,customer=custid,product=c.product,quantity=c.quantity,ProductName=c.ProductName,ProductDetails=c.ProductDetails,ProductPrice=c.ProductPrice,ProductCategory=c.ProductCategory,ProductImage=c.ProductImage).save()
       c.delete()
    request.session["productid"]=0
    return redirect("order")

# def remove_cart(request):
#     user_id=None
#     amount=0.0
#     total_amount=0.0
#     shipping_amount=40.0
#     datas={}
#     try:
#         user_id=request.session["useraddressid"]
#     except:
#         pass
#     if request.method == 'GET':
#         prod_id = request.GET['prod_id']           
#         print("This is productss",prod_id,user_id)
#         c=KartProducts.objects.filter(user=user_id,id=prod_id).first()
#         c.delete() 
#         del request.session["productid"]
#         print("work done")
#     cart_products=KartProducts.objects.filter(user=user_id)
#     print(cart_products)
#     # if cart_products:
#     #     for p in cart_products:
#     #         tem_amount=p.quantity * p.ProductPrice
#     #         amount += tem_amount
#     #         total_amount=shipping_amount + amount  
#     #     datas={'totalamount':total_amount,'amount':amount}
#     #     data={"name":"sumit"}
#     #     return JsonResponse(datas)
#     # else:
#     #     for p in cart_products:
#     #         tem_amount=p.quantity * p.ProductPrice
#     #         amount += tem_amount
#     #         total_amount=shipping_amount + amount  
#     #     datas={'totalamount':total_amount,'amount':amount}
#     data={"name":"sumit"}
#     return JsonResponse(data)

# def cart_quan(request):
#     data={"name":"sumit",
#           "age":20}
#     return JsonResponse(data)



def trys(request):
    data={"name":"sumit"}
    return JsonResponse(data)

# def cart_quantity(request):
#     tem=[]
#     user_id=None
#     amount=0.0
#     shipping_amount=40.0
#     try:
#         user_id=request.session["useraddressid"]
#     except:
#         pass
#     username=None
#     cart_products=None
#     sp=request.POST.get("searchproduct")
#     search_products=Products.objects.filter(Q(ProductName=sp) | Q(ProductCategory=sp) | Q(ProductBrand=sp))
#     cart_products=KartProducts.objects.filter(user=user_id)
#     try:
#         username=request.session['username']
#         product_id=request.session["productid"]
#         p=Products.objects.filter(id=product_id).get()
#         cheek=KartProducts.objects.filter(product=product_id).exists()
#         # return render(request,'cart.html',{'user2':username,'search_products':search_products,"cart_products":cart_products})
#         if cheek == False:
#             k=KartProducts(user=user_id,product=product_id,quantity=1,ProductName=p.ProductName,ProductDetails=p.ProductDetails,ProductPrice=p.ProductPrice,ProductCategory=p.ProductCategory,ProductImage=p.ProductImage)
#             k.save()
#             cart_products=KartProducts.objects.filter(user=user_id)
#             for p in cart_products:
#                     tem_amount= p.quantity * p.ProductPrice
#                     tem.append(p.ProductPrice)
#                     amount += tem_amount
#                     total_amount=shipping_amount + amount
#                     # print(tem_amount)
#             # print(cart_products)
#             return render(request,'cart.html',{'user2':username,'search_products':search_products,"cart_products":cart_products,"tem_amount":tem,'totalamount':total_amount,'amount':amount})
#         # return render(request,'cart.html',{'user2':username,'search_products':search_products,"cart_products":cart_products})     
#     except:
#         pass
#     cart_products=KartProducts.objects.filter(user=user_id)
#     if cart_products:
#         for p in cart_products:
#             tem_amount=p.quantity * p.ProductPrice
#             tem.append(p.ProductPrice)
#             amount += tem_amount
#             total_amount=shipping_amount + amount
#         return render(request,'cart.html',{'search_products':search_products,'user2':username,"cart_products":cart_products,"tem_amount":tem,'totalamount':total_amount,'amount':amount})
#     return render(request,'cart.html',{'search_products':search_products,'user2':username})





def product_detail(request,id):
    request.session["productid"]=id
    username=None
    try:
        username=request.session['username']
        cheek=KartProducts.objects.filter(product=id).exists()
    except:
        pass
    sp=request.POST.get("searchproduct")
    search_products=Products.objects.filter(Q(ProductName=sp) | Q(ProductCategory=sp) | Q(ProductBrand=sp))
    product=Products.objects.filter(id=id).first()
    return render(request,'productdetail.html',{'user2':username,"product":product,'search_products':search_products,"check_product":cheek})

def products(request,type):
    username=None
    sp=request.POST.get("searchproduct")
    search_products=Products.objects.filter(Q(ProductName=sp) | Q(ProductCategory=sp) | Q(ProductBrand=sp))
    try:
        username=request.session['username']
    except:
        pass
    show_products=Products.objects.filter(ProductCategory=type)
    return render(request,'products.html',{'user2':username,'products':show_products,'search_products':search_products})

#
def add_profile(request):
    username=request.session['username']
    sp=request.POST.get("searchproduct")
    search_products=Products.objects.filter(Q(ProductName=sp) | Q(ProductCategory=sp) | Q(ProductBrand=sp))
    if request.method == 'POST':
        Form=DeliveryForm()
        email=request.session['email']
        FindUser=IndoUsers.objects.filter(Email=email).first()
        name=request.POST['name']
        locality=request.POST['locality']
        city=request.POST['city']
        zipcode=request.POST['zipcode']
        state=request.POST['state']
        print(FindUser.id,name,locality,city,zipcode,state)
        try:
            # Form.save()
            if Form.is_valid:
                sv=DeliveryDetails(user=FindUser.id,name=name,locality=locality,city=city,zipcode=zipcode,state=state)
                sv.save()
                save="Address save successfully."
                if 'username' in request.session:
                    return render(request,"profile.html",{"save":save,"form":Form,'user2':username,'search_products':search_products})
        except:
            pass
    else:
        Form=DeliveryForm()
    return render(request,"profile.html",{"form":Form,'user2':username,'search_products':search_products})

def showaddress(request):
    user_id=None
    try:
        user_id=request.session['useraddressid']
    except:
        pass
    alladdress=DeliveryDetails.objects.filter(user=user_id)
    return render(request,"address.html",{'alladdress':alladdress})



# def search_products(request,proname):
#     sp=request.POST.get("searchproduct"Z)
#     all_pro=Products.objects.filter(Q(ProductName=sp) | Q(ProductCategory=sp))
#     return render(request,'Index.html',{"all_pro":all_pro})

# def allproducts(request):
#     show_products=Products.objects.all()
#     return render(request,'products.html',{'products':show_products}) 
