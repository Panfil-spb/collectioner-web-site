from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20)
    secondname = models.CharField(max_length=50)
    phonenumber = models.IntegerField()
    town = models.CharField(max_length=50)
