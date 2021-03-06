from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=32)
    bio = models.CharField(max_length=500)

class Art(models.Model):
    title = models.CharField(max_length=32)
    author = models.ForeignKey(Artist, null=True, on_delete=models.SET_NULL, related_name='art')
    rating = models.IntegerField(null=True, blank=True)
    image = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=500)
    created_date = models.DateField()

class User(models.Model):
    username = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=1000)
    use = models.CharField(max_length=32)
    cart = ArrayField(models.IntegerField()
                   , size=10, null=True, blank=True)
    # cart = ArrayField(
    #     models.ForeignKey(Art, null=True, on_delete=models.SET_NULL))
