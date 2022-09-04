from .serializers import CategorySerializer, PostSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.generics import ListAPIView
from blog.models import Category, Post, Media


class CategoryListView(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostListView(ReadOnlyModelViewSet):
    queryset = Post.publish_objects.select_related('category').all()
    serializer_class = PostSerializer

