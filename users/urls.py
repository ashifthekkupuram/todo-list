from django.urls import path
from .views import (
    LoginPage,
    LogoutPage,
    UserRegisterView,
    ProfileView,
    ProfileUpdateView
)
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView

urlpatterns = [
    path('login/',LoginPage.as_view(),name='login'),
    path('logout/',LogoutPage.as_view(),name='logout'),
    path('register/',UserRegisterView.as_view(),name='register'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('profile/<int:pk>',ProfileUpdateView.as_view(),name='profile-update'),
    path('password_change/',PasswordChangeView.as_view(
        template_name = 'users/password_change.html'
    ),name='password_change'),
    path('password_change_done/',PasswordChangeDoneView.as_view(
        template_name = 'users/password_change_done.html'
    ),name='password_change_done')

]
