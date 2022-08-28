from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.slug


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.STATUS.PUBLISHED)

    
class Post(models.Model):
    class STATUS(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date='created')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2, default=STATUS.DRAFT)

    objects = models.Manager()  # The default manager
    publish_objects = PublishedManager()    # Custom manager

    def __str__(self):
        return self.title


class Media(models.Model):
    blog = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='media')
    media = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.blog.title
