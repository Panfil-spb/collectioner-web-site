from django.db import models
from django.contrib.auth.models import User
# Create your models here.


def user_directory_path(instance, filename):
    return f'profileuser/user_{instance.user.id}/{filename}'


class UserInfo(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    user_avatar = models.ImageField(upload_to=user_directory_path, null=True)
    phonenumber = models.CharField(max_length=15, null=True)
    town = models.CharField(max_length=50, null=True)
