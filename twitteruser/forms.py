from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import TwitterUser


class TwitterUserCreationForm(UserCreationForm):
    class Meta:
        model = TwitterUser
        fields = "__all__"