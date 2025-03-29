from django.db import models

# Create your models here.
class user(models.Model):
    display_name = models.CharField(max_length=255, null=1)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length = 255)
    age = models.IntegerField(null=1)
    money = models.IntegerField(null = 1)
    
    def __str__(self):
        return f"{self.display_name}"
