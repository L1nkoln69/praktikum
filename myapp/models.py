from django.db import models
from django.urls import reverse  # noqa F401


class Post(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=1000)
    image = models.ImageField()
    description = models.TextField()
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    date_publication = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])


class Comment(models.Model):
    user_name = models.CharField(max_length=70, default='Anonymous ')
    text_comment = models.TextField()

    def __str__(self):
        return f'{self.user_name}'


class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    about = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name}'
