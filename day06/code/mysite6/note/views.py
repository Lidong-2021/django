from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from . import models
from django.core.paginator import Paginator


def check_login(fn):
    def wrap(request, *args, **kwargs):
        if not hasattr(request, 'session'):  # 没有登录
            return HttpResponseRedirect('/user/login')
        if 'user' not in request.session:
            return HttpResponseRedirect('/user/login')
        return fn(request, *args, **kwargs)

    return wrap


# Create your views here.
@check_login
def list_view(request):
    user_id = request.session['user']['id']
    auser = User.objects.get(id=user_id)
    notes = auser.note_set.all()
    return render(request, 'note/showall.html', locals())


@check_login
def add_view(request):
    if request.method == 'GET':
        return render(request, 'note/add_note.html')
    elif request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        # 得到当前用户的信息
        user_id = request.session['user']['id']
        auser = User.objects.get(id=user_id)
        anote = models.Note(user=auser)
        anote.title = title
        anote.content = content
        anote.save()
        return HttpResponseRedirect('/note/')


@check_login
def mod_view(request, id):
    if request.method == 'GET':
        anote = models.Note.objects.get(id=id)

        return render(request, 'note/mod_note.html', locals())
    elif request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        # 得到当前用户的信息
        user_id = request.session['user']['id']
        auser = User.objects.get(id=user_id)
        anote = models.Note.objects.get(id=id)
        anote.title = title
        anote.content = content
        anote.save()
        return HttpResponseRedirect('/note/')


@check_login
def del_view(request, id):
    try:
        anote = models.Note.objects.get(id=id)
    except:
        return HttpResponse('没有id为%s的数据记录' % id)
    anote.delete()
    return HttpResponseRedirect('/note/')


@check_login
def list2_view(request):
    user_id = request.session['user']['id']
    auser = User.objects.get(id=user_id)
    notes = auser.note_set.all()
    # 在此处添加分页功能
    paginator = Paginator(notes, 10)
    cur_page = request.GET.get('page', 1)
    cur_page = int(cur_page)
    page = paginator.page(cur_page)
    return render(request, 'note/listpage.html', locals())
