from django.urls import reverse_lazy
from django.shortcuts import render

from django.views.generic import ListView,DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Task

# Create your views here.
class HomeView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'base/home.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(author=self.request.user).order_by('-created','completed')
        
        search_input = self.request.GET.get('search_input') or ''
        
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
        
        context['input'] = search_input
        
        return context

class TaskView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Task
    context_object_name = 'task'

    def test_func(self):
        task = self.get_object()
        if task.author == self.request.user:
            return True
        else:
            return False
        
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'discription']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        task = form.save(commit=False)
        task.author = self.request.user
        task.save()
        return super(TaskCreate, self).form_valid(form)        
