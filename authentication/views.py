from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import LoginForm, RegisterForm
from twitteruser.models import TwitterUser
from twitteruser.forms import TwitterUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                'username'), password=data.get('password'))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('dashboard')))

    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitterUser.objects.create_user(username=data.get(
                'username'), password=data.get('password'), display_name=data.get('display_name'), bio=data.get('bio'))
            login(request, new_user)
            return HttpResponseRedirect(reverse('dashboard'))

    form = RegisterForm()
    return render(request, 'register.html', {'form': form})