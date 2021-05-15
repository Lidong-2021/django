from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=30,
                             null=False,
                             unique=True,
                             verbose_name='书名')
    pub = models.CharField(max_length=50,
                           verbose_name='出版社',
                           null=True)
    price = models.DecimalField(decimal_places=2,
                                max_digits=7,
                                verbose_name='定价',
                                default=0)
    marker_price = models.DecimalField(decimal_places=2,
                                       max_digits=7,
                                       verbose_name='零售价',
                                       default='99999')

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(verbose_name='年龄', default=1)
    email = models.EmailField(verbose_name='邮箱', default='xxx@qq.com')

    def __str__(self):
        return self.name


class Wife(models.Model):
    name = models.CharField(max_length=50, verbose_name='姓名')
    author = models.OneToOneField(Author, on_delete=models.PROTECT, )
