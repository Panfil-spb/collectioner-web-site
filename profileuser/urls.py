from django.urls import path
from profileuser import views
urlpatterns = [
    path('', views.profileuser, name='profileuser'),
    path('update', views.updateprofileinfo, name='update_profile')
]
