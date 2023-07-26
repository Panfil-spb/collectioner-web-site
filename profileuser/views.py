from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserInfo
from .forms import UserInfoForm
# Create your views here.


@login_required
def updateprofileinfo(request: HttpRequest) -> HttpResponse:
    userinfo = get_object_or_404(UserInfo, user=request.user)
    return render(request, 'profileuser/update_profile.html', {'form': UserInfoForm, 'userinfo': userinfo})


@login_required
def profileuser(request: HttpRequest) -> HttpResponse:
    user = request.user
    obj = get_object_or_404(UserInfo, user=user)
    return render(request, 'profileuser/profile.html', {'img': obj.user_avatar, 'firstname': obj.first_name, 'secondname': obj.last_name,
                                                        'last_login': f'{user.last_login.day}.{user.last_login.month}.{user.last_login.year} в {user.last_login.hour}:{user.last_login.minute}',
                                                        'town': obj.town, 'phonenumber': obj.phonenumber})
