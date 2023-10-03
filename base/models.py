from django.db import models
from users.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField(null=True,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by {self.author.username}'