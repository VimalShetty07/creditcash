from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    
    path('',views.index,name="index"),
    path('index',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('payment',views.payment,name="payment"),
    path('signout',views.signout,name="signout"),
   
]
