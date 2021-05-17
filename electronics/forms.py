from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import contactu

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class contactform(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Subject'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Message'}))
    class Meta:
        model = contactu
        fields = ['name','email','subject','message']