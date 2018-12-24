# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Cada clase representa una tabla


class Post(models.Model):
    '''
    Cada atributo representa una collumna , parece por defecto el ID
    hay que checar por que aveces necesita que los parametros sean null al llenar la BD
    '''
    title = models.CharField(max_length=150)
    body = models.TextField()
    image = models.ImageField(upload_to="post_image", null = True )
    create_at = models.DateTimeField(auto_now=True, auto_now_add=False, null = True )
    update_at = models.DateTimeField(auto_now=False, auto_now_add=True, null = True )
