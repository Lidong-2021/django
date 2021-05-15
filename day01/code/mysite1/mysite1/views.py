from django.http import HttpResponse


def page1_view(request):
    html = '<h1>这是第一个页面</h>'
    return HttpResponse(html)


def page2_view(request):
    html = '<h1>这是第二个页面</h>'
    return HttpResponse(html)


def page_index(request):
    html = '<h1>这是我的首页</h>'
    return HttpResponse(html)


def pagen(request, n):
    html = '<h1>这是我的第%s个页面</h>' % n
    return HttpResponse(html)


def index(request, x):
    return HttpResponse("hello, world. You're at the polls index.%s" % x)


def op_view(request, x, op, y):
    if op == 'add':
        return HttpResponse("<h1>%d+%d的结果是%d</h1>" % (x, y, x + y))
    elif op == 'sub':
        return HttpResponse("<h1>%d-%d的结果是%d</h1>" % (x, y, x - y))
    elif op == 'mul':
        return HttpResponse("<h1>%d*%d的结果是%d</h1>" % (x, y, x * y))


def person_view(request, name, age):
    return HttpResponse('姓名：%s，年龄:%d' % (name, age))


def birthday_view(request, n1, n2, n3):
    if 999 < n1 < 10000 and n2 < 13 and n3 < 32:
        return HttpResponse('生日是：%s年，%s月，%d日' % (n1, n2, n3))
    elif n1 < 32 and n2 < 13 and 999 < n3 < 10000:
        return HttpResponse('生日是：%s年，%s月，%d日' % (n3, n2, n1))
    else:
        return HttpResponse('出错啦！')


def sum_view(request):
    if request.method == "GET":
        start = int(request.GET['start'])
        stop = int(request.GET['stop'])
        step = int(request.GET['step'])
        re = sum(range(start, stop, step))
        return HttpResponse(re)
    else:
        return HttpResponse('404')