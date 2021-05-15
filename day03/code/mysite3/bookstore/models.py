from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    pub = models.CharField(max_length=100, null=False)
    marker_price = models.DecimalField(decimal_places=2, max_digits=7)


class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(null=False, default=1)
    email = models.EmailField(null=True)
