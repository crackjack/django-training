# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    # category = models.ForeignKey('Category')
    # author = models.ForeignKey('Author')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated_on = models.DateTimeField(auto_now=True)
