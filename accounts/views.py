import django
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse, request
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'home.html')

def user_registration(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form' : form,
    }

    return render(request, "register.html", context=context)


# Login

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            return redirect('/')
        else:
            messages.info(request, 'Username or password is incorrect!')

    context = {
        "form" : ""
    }
    return render(request, "login.html", context=context)


# logout
def user_logout(request):
    logout(request)
    return redirect("login")    