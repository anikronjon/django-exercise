from django.urls import path
from . import views

app_name = 'forms'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('registration', views.registration_view, name='registration'),

]
