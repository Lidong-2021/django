from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def page1_view(request):
    return HttpResponse('page1')


def page2_view(request):
    return HttpResponse('page2')


def page3_view(request):
    return HttpResponse('page3')
