# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Product

class User(AbstractUser):
    company_name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    buy_hystory = models.ManyToManyField(Product, related_name='buyers')