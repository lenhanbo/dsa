
# Create your models here.
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
import os

def user_directory_path(instance, filename):
    # Tạo đường dẫn dạng: "uploads/username/filename"
    return f'uploads/{instance.author.username}/{filename}'

class document(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField(max_length=100000, null = 1)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null= 1, blank=1)
    file = models.FileField(upload_to=user_directory_path, null=1, blank=1)
    upload_date = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse('document_detail',kwargs = {'pk' : self.id})
    def get_file_name(self):
        file_path = self.file.path
        filename=os.path.basename(file_path)
        return filename
    class Meta:
        ordering = ['upload_date']
        # permissions = (('to_comment', 'to comment on a blog'),) # tao permission


class comment(models.Model):
    content = models.CharField(max_length= 10000000,null = 1)
    blog = models.ForeignKey(document, on_delete=models.SET_NULL, null= 1, blank=1)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null= 1, blank=1)
    upload_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['upload_date']

