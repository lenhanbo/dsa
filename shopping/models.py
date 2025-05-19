from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.



class user(models.Model):
    name = models.CharField(max_length=1000)
    rating = models.FloatField(max_length=1000, null = 1)
    money = models.FloatField(max_length= 1000,null = 1)
    def get_absolute_url(self):
        return reverse('user_detail',kwargs = {'pk' : self.id})
    
    

class item(models.Model):
    name = models.CharField(max_length=1000)
    price = models.FloatField(max_length=1000)
    description = models.TextField(max_length=100000, null = 1)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null= 1, blank=1)
    def get_absolute_url(self):
        return reverse('item_detail',kwargs = {'pk' : self.id})
    class Meta:
        ordering = ['price']
        permissions = (('to_comment', 'to comment on a blog'),) # tao permission
