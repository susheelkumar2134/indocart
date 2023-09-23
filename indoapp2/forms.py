from django import forms
from indoapp2.models import IndoUsers,DeliveryDetails

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=IndoUsers
        fields="__all__"
        label={'FirstName':'First name','LastName':'Last Name'}
        widgets={'FirstName': forms.TextInput(attrs={'class':'one'}),
               'LastName': forms.TextInput(attrs={'class':'one'}),
               'Password': forms.PasswordInput(attrs={'class':'one'}),
                'Age': forms.TextInput(attrs={'class':'one'}),
               'Email': forms.EmailInput(attrs={'class':'one'})}

class DeliveryForm(forms.ModelForm):
    class Meta:
        model=DeliveryDetails
        fields = ['name','locality','city','state','zipcode']
        # fields ="__all__"
        widgets={'name': forms.TextInput(attrs={'class':'form-control'}),
               'locality': forms.TextInput(attrs={'class':'form-control'}),
                'city': forms.TextInput(attrs={'class':'form-control'}),
               'zipcode': forms.NumberInput(attrs={'class':'form-control'}),
               'state': forms.Select(attrs={'class':'form-control'})}