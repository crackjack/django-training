# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.models import Blog

def index(request):
    fullname = "{0} {1}".format(request.user.first_name, request.user.last_name)
    context = dict()
    context['fullname'] = fullname
    return render(request, 'index.html', context)

def all_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs})

def view_blog(request, input_slug):
    blog = Blog.objects.get(slug=input_slug)
    return render(request, 'single_blog.html', {'blog': blog})
