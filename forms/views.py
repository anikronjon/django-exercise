from django.shortcuts import render, HttpResponseRedirect
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login


# Create your views here.
def home_view(request):
    return render(request, 'forms/homepage.html', {'name': request.user})


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
                return HttpResponseRedirect('dashbord/')
        else:
            form = UserRegistrationForm()
        return render(request, 'forms/registration.html', {'form': form, 'name': request.user})

