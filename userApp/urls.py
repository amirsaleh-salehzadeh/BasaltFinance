from django.urls import path
from django.contrib.auth import views as auth_viewsfrom userApp import views

app_name = 'userApp'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    # path('<int:id>/', views.user_profile, name='user_profile'),
    path('users/', views.user_list, name='user_list'),
    path('create_user/', views.create_user, name='create_user'),
]
