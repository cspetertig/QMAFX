from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import AnonymousUser,User
from forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
def main(request):
    return render(request,'main.html',{})

def signin(request):
    if not isinstance(request.user,AnonymousUser):
        return HttpResponseRedirect('/')
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "Please Check the Information"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None and user.is_active:
                login(request,user)
                return render(request,'main.html',{})
            else:
                message = "Password Incorrect"
                return render(request, 'login.html', locals())
    login_form = UserForm()
    return render(request, 'login.html', locals())

def logout_mine(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_page(request):
    print "test"
    return render(request,'login.html',{})




