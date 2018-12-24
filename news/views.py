# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def index(request, username="By asiesps"):
    response = {}
    response['say'] = 'hellooo human'
    response['title'] = 'Mi titulo'
    response['username'] = username
    return render(request, 'index.html', response )


def fake(request):
        
    return render(request, 'fake.html' )