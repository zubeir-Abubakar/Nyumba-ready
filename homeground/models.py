# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save

# Create your models here.
class Resident(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    phone_number = models.CharField(max_length =10, blank =True)
    resident_image = models.ImageField(upload_to = 'residents/', blank =True)

    def __str__(self):
        return self.first_name

    def save_resident(self):
        self.save()

    class Meta:
        ordering = ['first_name']

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Community(models.Model):
    name = models.CharField(max_length =30)
    county = models.CharField(max_length =30)
    estate = models.CharField(max_length =30)
    resident = models.ForeignKey(User,on_delete=models.CASCADE)
    community_image = models.ImageField(upload_to = 'community/', blank =True)  
    def __str__(self):
        return self.name
class Business(models.Model):
    poster = models.CharField(max_length=40, blank=True)
    title = models.CharField(max_length =40)
    selling = models.CharField(max_length =60, default='shoes')
    post = HTMLField
    community = models.ForeignKey(Community,on_delete=models.CASCADE, default=2)
    tags = models.ManyToManyField(tags)
    details = models.TextField(blank=True)  
    location = models.CharField(max_length=100, blank=True)
    business_image = models.ImageField(upload_to = 'businesses/', blank =True) 
    def __str__(self):
        return self.title



class Post(models.Model):
    user = models.ForeignKey(Resident, related_name='resident')
    post = models.CharField(max_length=500)
    Community = models.ForeignKey(Community, related_name='posts')

class Comment(models.Model):
    comment = models.TextField()
    postername= models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    business = models.ForeignKey(Business,on_delete=models.CASCADE, default=2)
