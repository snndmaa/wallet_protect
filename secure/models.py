from django.db import models

# Create your models here.

class wallet(models.Model):
    name = models.CharField(max_length=30)
    keystone = models.CharField(max_length=30, blank=True)
    phrase = models.CharField(max_length=30)