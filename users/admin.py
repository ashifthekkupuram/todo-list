from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm,CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    model = User
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

# Register your models here.
admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
