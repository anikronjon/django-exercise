from rest_framework import serializers
from blog.models import Category, Post, Media


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'category', 'title', 'slug', 'description', 'created', 'updated', 'status')
        depth = 1


class CategorySerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True,)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'posts')


