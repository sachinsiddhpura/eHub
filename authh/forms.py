from django import forms
from django.contrib.auth import get_user_model

user = get_user_model()

class ContactForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}))
	email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}))
	content=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Your Content'}))

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if not 'gmail.com' and '@' in  email:
			return ValidationError('Please Enter Correct Email')
		return email

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))

class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Username'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Your Password'}))

	def clean_password(self):
		data=self.cleaned_data
		password = self.cleaned_data.get('password')
		password1 =self.cleaned_data.get('password1')
		if password != password1:
			return forms.ValidationError('Your Password Does Not Match')
		return data 

	def clean_username(self):
		username =self.cleaned_data.get('username')
		qs = user.objects.filter(username=username)
		if qs.exists():
			return forms.ValidationError('Username {} already exists'.format(username))
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = user.objects.filter(email=email)
		if qs.exists():
			return forms.ValidationError('Email {} already exists'.format(email))
		return email
