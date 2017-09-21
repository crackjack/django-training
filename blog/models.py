# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ManyToManyField('Category')
    author = models.ForeignKey('Author', blank=True, null=True)
    body = models.TextField(blank=True)
    is_published = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.title)

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return str(self.name)
