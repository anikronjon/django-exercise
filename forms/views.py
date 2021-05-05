from django.shortcuts import render, HttpResponseRedirect
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home_view(request):
    return render(request, 'forms/homepage.html', {'name': request.user})


def dashboard_view(request):
    if request.user.is_authenticated:
        return render(request, 'forms/dashboard.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/registration/')


def registration_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                newcomer = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1']
                )
                login(request, newcomer)
                return HttpResponseRedirect('/dashboard/')
        else:
            form = UserRegistrationForm()
        return render(request, 'forms/registration.html', {'form': form, 'name': request.user})
    else:
        return HttpResponseRedirect('/dashboard/')


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = AuthenticationForm()
        return render(request, 'forms/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/')




