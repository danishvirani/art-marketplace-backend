from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.name 

class Artist(models.Model):
    name = models.CharField(max_length=32)
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Art(models.Model):
    title = models.CharField(max_length=32)
    author = models.ForeignKey(Artist, null=True, on_delete=models.SET_NULL, related_name='art')
    rating = models.IntegerField(null=True)
    image = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    created_date = models.DateField()

    def __str__(self):
        return self.name
