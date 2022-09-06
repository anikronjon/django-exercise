from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('', include('blog.urls', namespace='blog')),
    path('api/', include('blog.api.urls', namespace='api')),
]
