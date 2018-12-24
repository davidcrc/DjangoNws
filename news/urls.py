from django.conf.urls import url
from django.contrib import admin
from . import views      # traer la url que creamos

urlpatterns = [
    
    url(r'^index/', views.index),
]
