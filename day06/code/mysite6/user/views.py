from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from . import models
from .unicodeString import *
from . import forms
from django.contrib.auth.models import User


# Create your views here.

def reg_view(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password1 = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        if len(username) < 2 or len(username) > 14:
            username_err = '用户名长度只能在2到14之间'
            return render(request, 'user/register.html', locals())
        elif password1 == '':
            password_err = '密码不能为空'
            return render(request, 'user/register.html', locals())
        elif password1 != password2:
            password2_err = '两次密码不一致'
            return render(request, 'user/register.html', locals())
        else:
            try:
                # a = models.User.objects.get(username=username)
                auser = User.objects.get(username=username)
                username_err = '用户名已经存在'
                return render(request, 'user/register.html', locals())
            except:
                # auser = models.User.objects.create(username=username, password=password1)
                auser = User.objects.create_user(
                    username=username,
                    password=password1)
                html = "注册成功！<a href='/user/login'>进入登录</a>"
                resp = HttpResponse(html)
                resp.set_cookie('username', str_to_code(username))
                return resp


def login_view(request):
    if request.method == 'GET':
        username = request.COOKIES.get('username', '')
        username = code_to_str(username)  # 将code转str
        return render(request, 'user/login.html', locals())
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == '':
            username_err = '用户名不能为空'
            return render(request, 'user/login.html', locals())
        try:
            # auser = models.User.objects.get(
            auser = User.objects.get(username=username)
            if auser.check_password(password):

                # 记录一个登录状态
                request.session['user'] = {
                    'username': username,
                    'id': auser.id
                }
                resp = HttpResponseRedirect('/')
                if 'remember' in request.POST:
                    resp.set_cookie('username', str_to_code(username))
                return resp  # 登录成功直接跳转到首页
            else:
                password_err = '密码错误'
                return render(request, 'user/login.html', locals())
        except:
            password_err = '用户名不存在'
            return render(request, 'user/login.html', locals())


def reset_view(request):
    username = request.session['user']['username']
    user_id = request.session['user']['id']
    if request.method == 'GET':
        return render(request, 'user/reset_pw.html', locals())
    elif request.method == 'POST':
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        auser = User.objects.get(username=username, id=user_id)
        if auser.check_password(password):
            if password1 != password2:
                password2_err = '两次密码不一致'
                return render(request, 'user/reset_pw.html', locals())
            else:
                auser.set_password(password1)
                auser.save()
                return HttpResponse('密码修改成功！<a href="/">返回首页</a>')
        else:
            password_err = '原密码错误'
            return render(request, 'user/reset_pw.html', locals())


def logout_view(request):
    # 退出登录,注销
    if 'user' in request.session:
        del request.session['user']  # 清除登录记录
    return HttpResponseRedirect('/')


def reg2_view(request):
    if request.method == 'GET':
        my_form = forms.MyRegFrom()
        # html = myform.as_p()
        # print(html)
        # return HttpResponse(html)
        return render(request, 'user/reg2.html', locals())
    elif request.method == 'POST':
        my_form = forms.MyRegFrom(request.POST)
        if my_form.is_valid():
            dic = my_form.cleaned_data
            username = dic['username']
            password = dic['password']
            password2 = dic['password2']
            return HttpResponse(str(dic))
        else:
            return HttpResponse('表单验证失败')
