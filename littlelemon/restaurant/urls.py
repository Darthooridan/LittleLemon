from django.contrib import admin 
from django.urls import path
from . import views 
from .views import sayHello 
  
urlpatterns = [ 
    path('', sayHello, name='sayHello'), 
    path('index/', views.index, name='index'),
]