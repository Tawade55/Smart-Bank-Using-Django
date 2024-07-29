from django import forms
from django.contrib.auth.forms import UserCreationForm	#usercreation form has username,email,password 
from userauths.models import User

class UserRegisterForm(UserCreationForm):
	username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":" Enter The Username"}))
	email=forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"Enter your Email Address "}))
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Enter Password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Enter Confirm Password"}))

	class Meta:
		model=User
		fields=['username','email','password1','password2']
