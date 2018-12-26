from django.conf.urls import url
from django.contrib import admin
from . import views      # traer la url que creamos
from django.views.generic import TemplateView

urlpatterns = [
    # Podemos pasar variables como expreiones regulares
    # url(r'^fake', views.fake, name="fake"),
    url(r'^fake', TemplateView.as_view(template_name="fake.html"), name="fake"),
    # url(r'^(?P<username>\w+)', views.IndexNew.as_view(), name="index"),      # /([0-5]+) ... \w+ ... \d+
    url(r'^', views.IndexListView.as_view(), name="index"),
]
