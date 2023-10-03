from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','password1','password2']

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = UserChangeForm.Meta.fields        