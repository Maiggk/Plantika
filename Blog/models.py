# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class p_author(models.Model):
    alias = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45,null=True)
    about = models.CharField(max_length=300,null=True)
    profile_img = models.CharField(max_length=45,null=True)
    created = models.CharField(max_length=45)
    password = models.CharField(max_length=200)
    
    class Meta:
        app_label = 'Blog'
        db_table = 'p_author'

    def __str__(self):
        return '{}'.format(self.alias)

@python_2_unicode_compatible
class p_post(models.Model):
    post_code = models.CharField(max_length=45,null=True)
    name = models.CharField(max_length=200)
    sub_name = models.CharField(max_length=100,null=True)
    post = models.TextField()
    rate = models.IntegerField(null=True)
    author = models.ForeignKey(p_author)
    cover_image = models.CharField(max_length=100,null=True)
    date_post = models.CharField(max_length=45,null=True)
    schedule_post = models.CharField(max_length=45)
    posted = models.IntegerField()
    
    class Meta:
        app_label = 'Blog'
        db_table = 'p_post'

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