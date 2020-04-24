# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import *
from .models import p_post,CustomUser
from django.contrib.auth.admin import UserAdmin

#Admins site titles
admin.site.site_header = "Plantika Administracion";
admin.site.site_title = "Plantika";

# Register your models here.
admin.site.unregister(User)
admin.site.register(CustomUser, UserAdmin)

#Exclude areas here
admin.site.unregister(Group)

@admin.register(p_post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'sub_name', 'post', 'author', 'cover_image','schedule_post']
    pass