from django.conf.urls import url,include
from django.contrib.auth.models import User
import views

urlpatterns=[
    url(r'^new/',views.add_strategy),
    url(r'^detail/(?P<pk>\d+)/$',views.detail),
    url(r'^(?P<pk>\d+)/$',views.strategy_detail),
    url(r'^delete/(?P<pk>\d+)/$',views.delete),
    url(r'^update/(?P<pk>\d+)/$', views.update),
    url(r'^all/',views.strategy_index)
]