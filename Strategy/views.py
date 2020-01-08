# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from models import Strategy
from forms import StrategyForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@login_required
def add_strategy(request):
    if request.method == 'GET':
        return render(request, 'Strategy/add.html')
    if request.method == 'POST':
        title=request.POST['Title']
        desc=request.POST['Description']
        code=request.POST['Code']
        if title=='' or code=='':
            return render(request, 'error.html', {'error': 'Please input all the fields'})
        else:
            strategy=Strategy(title=title,user=request.user,description=desc,code=code,status='INITIAL')
            strategy.save()
            return HttpResponseRedirect('/strategy/all/')



@login_required
def strategy_detail(requset, pk):
    try:
        strategy = Strategy.objects.get(pk=pk)
        ins = StrategyForm(instance=strategy)
        return render(requset, 'Strategy/detail.html', {'strategy': ins})
    except ObjectDoesNotExist as e:
        return render(requset, 'error.html', {'error': e})



@login_required
def strategy_index(request):
    strategys = Strategy.objects.filter(user=request.user)
    return render(request, 'Strategy/index.html', {'strategy': strategys})

@login_required
def delete(request,pk):
    try:
        strategy=Strategy.objects.get(pk=pk)
        strategy.delete()
        strategys = Strategy.objects.filter(user=request.user)
        return render(request, 'Strategy/index.html', {'strategy': strategys})
    except ObjectDoesNotExist as e:
        return render(request, 'error.html', {'error': e})

@login_required
def detail(request,pk):
    try:
        strategy=Strategy.objects.get(pk=pk)
        return render(request,'Strategy/detail.html',{'strategy':strategy})
    except ObjectDoesNotExist as e:
        return render(request, 'error.html', {'error': e})

@login_required
def update(request,pk):
    try:
        strategy=Strategy.objects.get(pk=pk)
        strategy.code=request.POST['code']
        strategy.status=request.POST['status']
        strategy.save()
        return HttpResponseRedirect('/strategy/all/')
    except ObjectDoesNotExist as e:
        return render(request, 'error.html', {'error': e})