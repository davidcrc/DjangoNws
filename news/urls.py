from django.conf.urls import url
from django.contrib import admin
from . import views      # traer la url que creamos

urlpatterns = [
    # Podemos pasar variables como expreiones regulares
    url(r'^fake', views.fake, name="fake"),
    url(r'^index/(?P<username>\w+)', views.index, name="index"),      # /([0-5]+) ... \w+ ... \d+
    url(r'^index/', views.index, name="index"),
]
