from django import forms
from indoapp.models import IndoUsers

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