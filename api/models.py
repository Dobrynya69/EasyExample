from django.db import models
from django.contrib.auth import get_user_model


class Genre(models.Model):
    name = models.TextField(primary_key=True, max_length=200)


class Anime(models.Model):
    title = models.TextField()
    image = models.URLField(max_length=500)
    genres = models.ManyToManyField(Genre, related_name='genres')
    description = models.TextField(default='No description')

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    anime = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    text = models.TextField()

    def __str__(self):
        return self.text
