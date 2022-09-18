from django.conf import urls
from django.urls import path 
from . import views
urlpatterns=[
    path('carblog/',views.blogHome,name="HomePage"),
    path('sellcar/',views.carSell,name="CarSell")
]