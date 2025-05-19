from django.db import models
from django.urls import reverse
# Create your models here.
class user(models.Model):
    display_name = models.CharField(max_length=255, null=1)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length = 255)
    age = models.IntegerField(null=1)
    money = models.IntegerField(null = 1)
    
    def __str__(self):
        return f"{self.display_name}"
    def get_link(self):
        return reverse('testing:get_info', kwargs={'id': self.id} )

class Comment(models.Model):
    author = models.CharField(max_length=1000,null= True)
    user_comment = models.CharField(max_length=1000, null= True)
    
    def __str__(self):
        return f"Binh luan cua {self.author}" 
