from django.contrib import admin
from . import models


# Register your models here.
class Book3Manager(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(models.Author3)
admin.site.register(models.Book3, Book3Manager)
