from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('date_publication', 'is_published')

    fields = ['date_publication', 'is_published', 'user', 'description',
              'short_description', 'title']


admin.site.register(Comment)
