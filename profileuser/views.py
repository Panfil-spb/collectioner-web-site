import os
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserInfo
from .forms import UserInfoForm
# Create your views here.


@login_required
def updateprofileinfo(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        userinfo = get_object_or_404(UserInfo, user=request.user)
        return render(request, 'profileuser/update_profile.html', {'form': UserInfoForm, 'userinfo': userinfo})
    else:
        userinfo = get_object_or_404(UserInfo, user=request.user)
        if len(request.FILES) != 0:
            if userinfo.user_avatar:
                if len(userinfo.user_avatar) > 0:
                    os.remove(userinfo.user_avatar.path)
            print(request.FILES)
            userinfo.user_avatar = request.FILES['avatar_user_create']

        userinfo.first_name = request.POST.get('first_name')
        userinfo.last_name = request.POST.get('last_name')
        userinfo.town = request.POST.get('town')
        userinfo.phonenumber = request.POST.get('phonenumber')
        userinfo.save()
        return redirect('profileuser')


@login_required
def profileuser(request: HttpRequest) -> HttpResponse:
    user = request.user
    obj = get_object_or_404(UserInfo, user=user)
    print(obj.user_avatar.url)
    return render(request, 'profileuser/profile.html', {'avatar': obj.user_avatar, 'firstname': obj.first_name, 'secondname': obj.last_name,
                                                        'last_login': f'{user.last_login.day}.{user.last_login.month}.{user.last_login.year} в {user.last_login.hour}:{user.last_login.minute}',
                                                        'town': obj.town, 'phonenumber': obj.phonenumber})
