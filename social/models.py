from django.db import models

# Create your models here.



class Profile(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    bio = models.TextField()
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
