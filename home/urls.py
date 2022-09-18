from django.conf import urls
from django.urls import path 
from . import views
urlpatterns=[
    path('',views.HomePage,name="HomePage"),
    path('contact/',views.Contact,name="Contact"),
    path('about/',views.About,name="About"),
    path('login/',views.loginhere,name='Login'),
    path('signup/',views.signup,name="SignUp"),
    path('logout/',views.Logout,name="Logout")
]