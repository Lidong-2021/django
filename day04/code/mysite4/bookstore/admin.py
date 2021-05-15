from django.contrib import admin
from . import models


# Register your models here.

class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub', 'price', 'marker_price']
    list_display_links = ['id', 'title', 'pub', 'price']
    list_filter = ['pub']
    search_fields = ['title', 'pub']
    list_editable = ['marker_price']


class AuthorManager(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']


class WifeManager(admin.ModelAdmin):
    list_display = ['id', 'name', 'author']


admin.site.register(models.Book, BookManager)
admin.site.register(models.Author, AuthorManager)
admin.site.register(models.Wife, WifeManager)
