from django.db import models


# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=250,verbose_name="Başlık")
    description=models.TextField(verbose_name="İçerik")
   
    def __str__(self):
        return self.title
