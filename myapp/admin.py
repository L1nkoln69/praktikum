from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('date_publication', 'is_published')

    fields = ['date_publication', 'is_published', 'user', 'description',
              'short_description', 'title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('is_published',)

    fields = ['user_name', 'post', 'is_published']
