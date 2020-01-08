from django.conf.urls import url,include
from django.contrib.auth.models import User
import views

urlpatterns=[
    url(r'^detail/(?P<pk>\d+)/$', views.detail),
    url(r'^error/(?P<pk>\d+)/$', views.error),
    url(r'^del/(?P<pk>\d+)/$', views.delete),
    url(r'^(?P<pk>\d+)/$',views.run),
    url(r'',views.backtest_index),
]