# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Post
# Register your models here.

# Para que el modelo aparezaca en el sito de administracio
# de django , debe añadirse aqui

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)