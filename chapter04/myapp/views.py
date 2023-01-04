from django.shortcuts import render
from django.http import HttpResponse
from .tasks import notify_email
# Create your views here.


def home(request):
    notify_email.delay("Hello")
    return HttpResponse("Hello world")
