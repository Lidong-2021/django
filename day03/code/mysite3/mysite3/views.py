from django.http import HttpResponse
from django.shortcuts import render


def shebao_view(request):
    if request.method == 'GET':
        return render(request, 'shebao.html')
