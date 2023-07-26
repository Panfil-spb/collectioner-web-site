from django import forms
from .models import UserInfo


class UserInfoForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ('user_avatar', 'phonenumber',
                  'town', 'first_name', 'last_name')
        UserInfo.objects.update()
