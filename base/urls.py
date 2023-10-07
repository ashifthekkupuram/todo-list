from django.urls import path
from .views import HomeView,TaskView,TaskCreate,TaskUpdate,TaskDelete

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('task/<int:pk>/',TaskView.as_view(),name='task'),
    path('task-create/',TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>',TaskDelete.as_view(),name='task-delete'),
]