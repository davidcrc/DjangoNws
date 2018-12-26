# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from models import Post
# Create your views here.


# def index(request, username="By asiesps"):
#     response = {}
#     response['say'] = 'hellooo human'
#     response['title'] = 'Mi titulo'
#     response['username'] = username
#     return render(request, 'index.html', response)


# def fake(request):

#     return render(request, 'fake.html' )

# Podemos extender de templateView y modificarlo para que reciba diferentes datos o variables
# class IndexNew(TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self, username, **kwargs):
#         context = super(IndexNew, self).get_context_data(**kwargs)

#         response = {}
#         response['say'] = 'hellooo human'
#         response['title'] = 'Mi titulo'
#         response['username'] = username

#         context.update(response)

#         return context

class IndexListView(ListView):
    model = Post
    ordering = ['-create_at']