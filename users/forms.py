from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
class UserSignupForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class UserEditSettingsForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
