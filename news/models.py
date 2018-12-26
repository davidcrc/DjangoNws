# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.html import format_html
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
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null = True )
    create_at = models.DateTimeField(auto_now=True, auto_now_add=False, null = True )
    update_at = models.DateTimeField(auto_now=False, auto_now_add=True, null = True )

    def image_tag(self):
        return format_html( "<image src='{}' style='height:140px'/>".format(self.image.url))

class Author(models.Model):
    '''
    
    '''
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    
    image = models.ImageField(upload_to="author_image", null = True )
    create_at = models.DateTimeField(auto_now=True, auto_now_add=False, null = True )
    update_at = models.DateTimeField(auto_now=False, auto_now_add=True, null = True )

    # Cambiar el nombre dentro del objeto en el manage de django
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)    


