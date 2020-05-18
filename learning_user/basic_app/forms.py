from django import forms
from django.contrib.auth.models import User
from basic_app.models import Userprofileinfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')



class UserprofileinfoForm(forms.ModelForm):
    class Meta():
        model = Userprofileinfo
        fields = ('portfolio_site','profile_pic')


