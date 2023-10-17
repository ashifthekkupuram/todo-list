from django.urls import path
from .views import (
    LoginPage,
    LogoutPage,
    UserRegisterView,
    ProfileView,
    ProfileUpdateView
)
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('login/',LoginPage.as_view(),name='login'),
    path('logout/',LogoutPage.as_view(),name='logout'),
    path('register/',UserRegisterView.as_view(),name='register'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('profile/<int:pk>',ProfileUpdateView.as_view(),name='profile-update'),
    #Password Change
    path('password_change/',PasswordChangeView.as_view(
        template_name = 'users/password_change.html'
    ),name='password_change'),
    path('password_change_done/',PasswordChangeDoneView.as_view(
        template_name = 'users/password_change_done.html'
    ),name='password_change_done'),
    #Password Reset
    path('password_reset/',PasswordResetView.as_view(
        template_name = 'users/password_reset.html'
    ),name='password-reset'),
    path('password_reset_done/',PasswordResetDoneView.as_view(
        template_name = 'users/password_reset_done.html'
    ),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(
        template_name = 'users/password_reset_confirm.html'
    ),name='password_reset_confirm'),
    path('password_reset_complete/',PasswordResetCompleteView.as_view(
        template_name = 'users/password_reset_complete.html'
    ),name='password_reset_complete'),
]
