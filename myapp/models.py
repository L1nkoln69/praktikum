from django.db import models
from django.urls import reverse  # noqa F401
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=1000)
    image = models.ImageField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_publication = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])

    def get_update_url(self):
        return reverse('update_user_post', args=[str(self.id)])


class Comment(models.Model):
    user_name = models.CharField(max_length=70, default='Anonymous ')
    text_comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True, default=1)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user_name}'
