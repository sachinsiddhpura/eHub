from django.urls import path
from . import views

app_name='authh'

urlpatterns = [
	path('',views.home,name='home'),
	path('login/',views.login,name='login'),
	path('register/',views.register,name='register'),
	path('logout/',views.logout,name='logout'),
	path('cart_page/',views.cart_page,name='cart_page'),
	path('contact/',views.contact,name='contact'),
	path('about/',views.about,name='about')
]
