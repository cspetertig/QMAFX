# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect
from tasks import backtest_start
from models import BackTest
from Strategy.models import Strategy
from django.contrib.auth.decorators import login_required
import pandas as pd
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


@login_required
def run(request, pk):
    try:
        res = backtest_start.delay(pk)
        print res
        strategy = Strategy.objects.get(pk=pk)
        strategy.status = 'PROCESSING'
        strategy.save()
        return HttpResponseRedirect('/strategy/all/')
    except ObjectDoesNotExist as e:
        return render(request, 'error.html', {'error': e})


@login_required
def backtest_index(request):
    backtests = BackTest.objects.all()
    return render(request, 'Backtest/index.html', {'index': backtests})


@login_required
def detail(request, pk):
    try:
        backtest = BackTest.objects.get(pk=pk)
    except ObjectDoesNotExist as e:
        return render(request, 'error.html', {'error': e})
    image = '/static/img/' + backtest.strategy.title + '.png'
    order=pd.read_csv('C:\\Users\\cspet\\\Documents\\QMAFX\\ForexWeb\\Backtest\\HistoryData\\ResultData\\Order_'+backtest.strategy.title+'.csv')
    order_list=[]
    for i in order.values:
        new_data={}
        new_data['Symbol']=i[1]
        new_data['Lot']=i[2]
        new_data['Type']=i[3]
        new_data['OpenTime']=i[4]
        new_data['CloseTime']=i[5]
        new_data['OpenPrice']=i[6]
        new_data['ClosePrice']=i[7]
        new_data['Mount']=i[11]
        order_list.append(new_data)
    paginator = Paginator(order_list, 20)
    page = request.GET.get('page', 1)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:

        contacts = paginator.page(1)
    except EmptyPage:

        contacts = paginator.page(paginator.num_pages)
    return render(request, 'Backtest/detail.html', {'image': image, 'backtest': backtest,'order':contacts})


@login_required
def delete(request, pk):
    try:
        backtest = BackTest.objects.get(pk=pk)
        # str='rm /home/jaden/Github/ForexWeb/static/img/%s.png' %(backtest.strategy.title)
        # exec(str)
        backtest.delete()
        return HttpResponseRedirect('/backtest/')
    except ObjectDoesNotExist as e:
        return render(request, 'error.html', {'error': e})

@login_required
def error(request,pk):
    try:
        backtest=BackTest.objects.get(pk=pk)
        return render(request,'Backtest/error.html',{'error':backtest.error_info})
    except ObjectDoesNotExist as e:
        return render(request, 'error.html', {'error': e})