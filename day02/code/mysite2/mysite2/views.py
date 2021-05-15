from django.http import HttpResponse
from django.shortcuts import render


def sum_view(request):
    if request.method == "GET":
        try:
            start = int(request.GET.get('start', '0'))
            stop = int(request.GET.get('stop'))
            step = int(request.GET.get('step', '1'))
            mysum = sum(range(start, stop, step))
            return HttpResponse("结果是：%d" % mysum)
        except Exception as e:
            return HttpResponse('输入有误：%s' % e)


login_from_html = """
    <form action="/login" method="post">
        用户名：<input type="text" name="username" >
        <input type="submit" value="提交">
    </form>
"""


def login(request):
    if request.method == 'GET':
        return HttpResponse(login_from_html)
    elif request.method == 'POST':
        name = request.POST.get('username', '属性错误')
        return HttpResponse(name)


def login2(request):
    if request.method == 'GET':
        # 返回模板 1.加载模板2.生成html 3.将html返回浏览器
        from django.template import loader
        t = loader.get_template('mylogin.html')
        html = t.render({'name': 'tarena'})
        return HttpResponse(html)
    elif request.method == 'POST':
        pass


def test(request):
    # 方法2：

    dict_test = {
        'h1': 'Hello world',
        'p': 'python'
    }
    return render(request, 'test.html', dict_test)


def mytemp_view(request):
    x = 5
    x += 10
    return render(request, 'mytemp.html', locals())


def mycal_view(request):
    html = """
    <form action="/mycal" method="POST">
        <input type="text" name="x" value="1">
        <select name="op">
            <option value="add">+加</option>
            <option value="sub">-减</option>
            <option value="mul">*乘</option>
            <option value="div">/除</option>
        </select>
        <input type="text" name="y" value="2">=<span>3</span>
        <div>
            <input type="submit" value="开始计算">
        </div>
    </form>
    """
    if request.method == "GET":
        return HttpResponse(html)
    if request.method == 'POST':
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        op = request.POST['op']
        result = 0
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x / y
        return render(request, 'mycal.html', locals())


def ggj(request):
    if request.method == "GET":
        return render(request, 'ggj.html', locals())
    elif request.method == 'POST':
        base = int(request.POST.get('base', '0'))
        huKou = request.POST.get('huKou')
        yl_gr = base * 0.08
        yg_dw = base * 0.19
        sy_gr = 0
        if huKou == '1':
            sy_gr = base * 0.2 / 100
        elif huKou == '2':
            sy_gr = 0
        sy_dw = base * 0.8 / 100
        gs_gr = shyu_gr = 0
        gs_dw = base * 0.5 / 100
        shyu_dw = base * 0.8 / 100
        yiliao_gr = base * 0.02 + 3
        yiliao_dw = base * 0.1
        ggj_gr = base * 0.12
        ggj_dw = base * 0.12
        gr = yl_gr + sy_gr + gs_gr + shyu_gr + yiliao_gr + ggj_gr
        dw = yg_dw + sy_dw + gs_dw + shyu_dw + yiliao_dw + ggj_dw
        return render(request, 'ggj.html', locals())