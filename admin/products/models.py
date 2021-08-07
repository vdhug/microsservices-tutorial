from django.db import models

# Create your models here.
class Product(models.Model):
    title: str = models.CharField(max_length=200)
    image: str = models.CharField(max_length=200)
    likes: int = models.PositiveIntegerField(default=0)


class User(models.Model):
    pass