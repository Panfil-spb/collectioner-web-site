import os
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import UserInfo
from .forms import UserInfoForm
# Create your views here.


@login_required
def update_profile_info(request: HttpRequest) -> HttpResponse:
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
        return redirect('profileuser', request.user.id)


@login_required
def profil_euser(request: HttpRequest, user_id: int) -> HttpResponse:
    user = get_object_or_404(User, id=user_id)
    user_info = get_object_or_404(UserInfo, user=user)

    return render(request, 'profileuser/profile.html', {'avatar': user_info.user_avatar, 'firstname': user_info.first_name, 'secondname': user_info.last_name,
                                                        'last_login': f'{user.last_login.day}.{user.last_login.month}.{user.last_login.year} в {user.last_login.hour}:{user.last_login.minute}',
                                                        'town': user_info.town, 'phonenumber': user_info.phonenumber,
                                                        'user_id': user_id})


@login_required
def view_users(request: HttpRequest):
    page = request.GET.get('page', 1)
    users_info = UserInfo.objects.all()

    paginator = Paginator(users_info, 3)
    page_objs = paginator.get_page(page)
    page_objs.next_page_number
    return render(request, 'profileuser/users.html', {'page_objs': page_objs, 'page': page})
