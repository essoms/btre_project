from django.db import models
from datetime import datetime

# Create your models here.

class Realtor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=40)
    is_mvp = models.BooleanField(default=True)
    hire_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
 