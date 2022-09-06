from django.contrib import admin
from .models import Category, Post, Media


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_post')
    prepopulated_fields = {'slug': ('name',)}

    @admin.display(description='Total Post')
    def total_post(self, obj):
        return obj.posts.all().count()


# Media Inline
class MediaInline(admin.TabularInline):
    model = Media


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'created', 'updated')
    list_editable = ('status',)
    radio_fields = {'status': admin.HORIZONTAL}
    prepopulated_fields = {'slug': ('title',)}
    inlines = [MediaInline]
