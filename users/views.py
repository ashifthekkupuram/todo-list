from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView,UpdateView,View
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect

# Create your views here.
class LoginPage(LoginView):
    template_name = 'users/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

class LogoutPage(LoginRequiredMixin, LogoutView):
    next_page = 'login'    

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    fields = ['username','email']
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return super(UserRegisterView, self).get(request)
    
class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/profile.html')
