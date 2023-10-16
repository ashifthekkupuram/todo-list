from django.urls import path
from .views import (
    LoginPage,
    LogoutPage,
    UserRegisterView,
    ProfileView,
    ProfileUpdateView
)

urlpatterns = [
    path('login/',LoginPage.as_view(),name='login'),
    path('logout/',LogoutPage.as_view(),name='logout'),
    path('register/',UserRegisterView.as_view(),name='register'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('profile/<int:pk>',ProfileUpdateView.as_view(),name='profile-update'),
]
