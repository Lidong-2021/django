from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def reg_view(request):
    if request.method == 'GET':
        return render(request, 'user/register.html', locals())
    elif request.method == 'POST':
        user_name = request.POST.get('username')
        passwd = request.POST.get('password')
        passwd2 = request.POST.get('password2')
        if passwd != passwd2:
            return HttpResponse('两次密码不一致')
        return HttpResponse('user_name:%s,passwd%s' % (user_name, passwd))
