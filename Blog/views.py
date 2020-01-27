# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'blog/index.html')

def about(request):
    return render(request,'blog/about.html')

def post(request):
    return render(request,'blog/post.html')

def contact(request):
    return render(request,'blog/contact.html')