# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Post, Author
# Register your models here.

# Para que el modelo aparezaca en el sito de administracio
# de django , debe añadirse aqui
@admin.register(Post)       # un decorador
class PostAdmin(admin.ModelAdmin):
    # Otra forma de retornar para que aparexca en el titulo
    list_display = ('title', 'image_tag' ,'create_at', 'update_at')

# admin.site.register(Post, PostAdmin)      # = q el @admin

# TYambien añadir el author para que aparezca en el manager de django
class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author, AuthorAdmin)