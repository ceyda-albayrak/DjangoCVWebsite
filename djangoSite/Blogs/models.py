from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=250,verbose_name="Başlık")
    description=models.TextField(verbose_name="İçerik")
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name='Yazar')
    
    def __str__(self):
        return self.title
        