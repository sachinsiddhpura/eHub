from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth import authenticate,get_user_model,logout
from django.contrib.auth import login as auth_login
from .forms import LoginForm,ContactForm,RegisterForm
from .models import Login 
from django.contrib import messages
from django.contrib.auth import logout as django_logout

user = get_user_model()

def home(request):
	context = {
	'title':'S-Mart',
	'content':'Welcome To The Online Shopping In S-MART'
	}
	#if request.user.is_authenticated():
	#	context['premium'] = 'Welcome To You'
	return render(request,'home.html',context)

def about(request):
	context = {
	'title':'About',
	}
	#if request.user.is_authenticated():
	#	context['premium'] = 'Welcome To You'
	return render(request,'about.html',context)

def cart_page(request):
	return render(request,'cart.html',{})

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form.save()
	context = {
		'title':'Contact Form',
		'form':form
	}
	return render(request,'contact.html',context)

def login(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username,password=password)
		if user is not None:
			auth_login(request,user)
			request.session['user'] =request.user.username
			Login.objects.create(username=request.user,s_name=True)
		else:
			messages.error(request,'Wrong Details!!')
			return redirect('/')
	context ={
		'title':'Login',
		'form':form
	}
	return render(request,'login.html',context)

def register(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		email = form.cleaned_data.get('email')
		password = form.cleaned_data.get('password')
		new_user = user.objects.create_user(username,email,password)
		return redirect('/login/')
	context = {
		'title':'Register',
		'form':form
	}
	return render(request,'register.html',context)

def logout(request):
	django_logout(request)
	msg = messages.success(request,'Successfully Logout')
	return render(request,'logout.html',{'msg':msg})
