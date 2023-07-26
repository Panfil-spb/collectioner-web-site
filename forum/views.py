from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from profileuser.forms import UserInfoForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from profileuser.models import UserInfo
from profileuser.forms import UserInfoForm
# from profileuser.models import UserInfo
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
        return render(request, 'forum/signup.html', {'user_form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # user = User.objects.create_user(
                #     username=request.POST['username'], password=request.POST['password1'],
                #     email=request.POST['email'])
                user = User.objects.create_user(request.POST)
                user.save()
                login(request, user)
                user_info = UserInfo.objects.create(
                    user=user)
                return redirect('profileuser')
            except IntegrityError:
                return render(request, 'forum/signup.html', {'form': UserCreationForm(), 'error': 'Пользователь с таким логином уже сущесвтует!'})
        else:
            return render(request, 'forum/signup.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    return render(request, 'profileuser/profile.html', context={'name': 'Вася', 'secondname': 'Пупкин', 'town': 'Санкт-Петербург', 'collections': [1, 1, 1, 2]})
