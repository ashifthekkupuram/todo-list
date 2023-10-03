from django.urls import path
from .views import (
    LoginPage,
    LogoutPage,
    UserRegisterView
)

urlpatterns = [
    path('login/',LoginPage.as_view(),name='login'),
    path('logout/',LogoutPage.as_view(),name='logout'),
    path('register/',UserRegisterView.as_view(),name='register'),
]
