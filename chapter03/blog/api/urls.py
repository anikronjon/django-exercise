from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('posts', views.PostListView)
router.register('categories', views.CategoryListView)


app_name = 'api'
urlpatterns = [
    path('', include(router.urls))
]