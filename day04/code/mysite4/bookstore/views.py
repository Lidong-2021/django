from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models
from django.db.models import Q, F


# Create your views here.

def add_view(request):
    if request.method == 'GET':
        return render(request, 'bookstore/add_book.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        pub = request.POST.get('pub')
        price = request.POST.get('price')
        m_price = request.POST.get('m_price')
        try:
            models.Book.objects.create(
                title=title,
                pub=pub,
                price=price,
                marker_price=m_price
            )
            return HttpResponseRedirect('/bookstore/list')
        except:
            return HttpResponse('添加失败！')


def list_view(request):
    # books = models.Book.objects.filter(price__lte=F('marker_price'))
    # books = models.Book.objects.filter(Q(pub='清华大学') | Q(price__gt=90))
    books = models.Book.objects.all()

    # for book in books:
    #     print('书名：', book.title)
    # return HttpResponse('查询成功')
    return render(request, 'bookstore/list.html', locals())


def mod_view(request, id):
    try:
        abook = models.Book.objects.get(id=id)
    except:
        return HttpResponse('没有id为%s的数据记录' % id)
    if request.method == 'GET':
        return render(request, 'bookstore/mod.html', locals())
    elif request.method == 'POST':
        abook.marker_price = request.POST.get('m_price', 0)
        abook.save()
        return HttpResponseRedirect('/bookstore/list')


def del_view(request, id):
    try:
        abook = models.Book.objects.get(id=id)
    except:
        return HttpResponse('没有id为%s的数据记录' % id)
    abook.delete()
    return HttpResponseRedirect('/bookstore/list')
