from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class LoginPage(LoginView):
    template_name = 'users/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

class LogoutPage(LoginRequiredMixin, LogoutView):
    next_page = 'login'    
