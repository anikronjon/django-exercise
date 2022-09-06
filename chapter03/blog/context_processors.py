from .models import Category
from django.shortcuts import render


def post_category(request):
    categories = Category.objects.all()
    return {'categories': categories}
