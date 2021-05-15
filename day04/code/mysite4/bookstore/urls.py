from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add', views.add_view),
    url(r'^list', views.list_view),
    url(r'^mod/(\d+)', views.mod_view),
    url(r'^del/(\d+)', views.del_view),
]
