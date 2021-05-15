from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=50, verbose_name='出版社')

    def __str__(self):
        return self.name


class Book2(models.Model):
    title = models.CharField(max_length=30, verbose_name='书名')
    pub = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
