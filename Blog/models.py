# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings


class CustomUser(User): #Herencia de tabla Usuarios, cambiado a autores
    class Meta:
        proxy = True
        app_label = 'auth'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

RATE_TYPE = (
    ('1','Aburrido'),
    ('2','Irrelevante'),
    ('3','Relevante'),
    ('4','Entretenido'),
    ('5','Interesante')
)
        
@python_2_unicode_compatible
class p_post(models.Model):
    post_code = models.CharField(max_length=45,null=True,blank=True)
    name = models.CharField(max_length=200)
    sub_name = models.CharField(max_length=100,null=True,blank=True)
    post = models.TextField()
    rate = models.CharField(max_length=1,choices=RATE_TYPE,null=True,blank=True)
    rate_count = models.IntegerField(blank=True,null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    cover_image = models.CharField(max_length=100,null=True,blank=True)
    date_post = models.CharField(max_length=45,null=True,blank=True)
    schedule_post = models.CharField(max_length=45)
    posted = models.IntegerField(blank=True)
    
    class Meta:
        app_label = 'Blog'
        db_table = 'p_post'
        verbose_name = 'Post'
        verbose_name_plural = "Posts"

    def __str__(self):
        return '{}'.format(self.name)
    
@python_2_unicode_compatible
class p_media_src(models.Model):
    type = models.CharField(max_length=45,null=True)
    name = models.CharField(max_length=200,null=True)
    date_upload = models.CharField(max_length=45,null=True)
    post_id = models.ForeignKey(p_post)
    order = models.IntegerField(null=True)
    
    class Meta:
        app_label = 'Blog'
        db_table = 'p_media_src'

    def __str__(self):
        return '{}'.format(self.name)
    
@python_2_unicode_compatible
class p_tag(models.Model):
    name = models.CharField(max_length=45)
    
    class Meta:
        app_label = 'Blog'
        db_table = 'p_tag'

    def __str__(self):
        return '{}'.format(self.name)

@python_2_unicode_compatible
class p_post_tag(models.Model):
    post_id = models.ForeignKey(p_post)
    tag_id = models.ForeignKey(p_tag)
    
    class Meta:
        app_label = 'Blog'
        db_table = 'p_post_tag'

    def __str__(self):
        return '{} - {}'.format(self.post_id,self.tag_id)