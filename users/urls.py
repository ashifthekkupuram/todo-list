from django.urls import path
from .views import (
    LoginPage,
    LogoutPage
)

urlpatterns = [
    path('login/',LoginPage.as_view(),name='login'),
    path('logout/',LogoutPage.as_view(),name='logout'),
]
