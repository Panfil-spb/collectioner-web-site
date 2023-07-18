from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def home(request: HttpRequest) -> HttpResponse:
    return render(request, "forum/index.html")


def loginuser(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, 'forum/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'forum/login.html', {'form': AuthenticationForm(), 'error': 'Неверный логин или пароль!'})
        else:
            login(request, user)
            return redirect('home')


@login_required
def logoutuser(request: HttpRequest):
    if request.method == 'POST':
        logout(request)
        return redirect('loginuser')


def signupuser(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, 'forum/signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'forum/signup.html', {'form': UserCreationForm(), 'error': 'Пользователь с таким логином уже сущесвтует!'})
        else:
            return render(request, 'forum/signup.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    return render(request, 'forum/profile.html', context={'name': 'Вася', 'secondname': 'Пупкин', 'town': 'Санкт-Петербург', 'collections': [1, 1, 1, 2]})