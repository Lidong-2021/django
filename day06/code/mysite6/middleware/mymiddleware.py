from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from django.http import Http404


class MyMW(MiddlewareMixin):
    def process_request(self, request):
        print('中间键 process—request方法被调用')
        print('路由是：', request.path)
        print('请求方式：', request.method)
        # if request.path == '/aaaa':
        #     return HttpResponse('当前路由是：/aaaa')
        # return HttpResponse('xxxxxxxxxxxxxxx')


class VisitLimit(MiddlewareMixin):
    # 键ip地址 值访问次数
    visit_times = {}

    def process_request(self, request):
        ip = request.META['REMOTE_ADDR']
        if request.path_info != '/test':
            return None
        times = self.visit_times.get(ip, 0)
        print('IP', ip, '已经访问过/test', times, '次')
        self.visit_times[ip] = times + 1
        if times < 5:
            return None
        return HttpResponse('您已经访问过%s次' % str(times))
