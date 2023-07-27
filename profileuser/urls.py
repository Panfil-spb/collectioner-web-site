from django.urls import path
from profileuser import views
urlpatterns = [
    path('<int:user_id>', views.profil_euser, name='profileuser'),
    path('update', views.update_profile_info, name='update_profile'),
    path('users', views.view_users, name='users')

]
