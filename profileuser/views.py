from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


@login_required
def profileuser(request: HttpRequest) -> HttpResponse:
    user = request.user
    obj = get_object_or_404(User, username=user)
    return render(request, 'profileuser/profile.html', )
