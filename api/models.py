from django.db import models
from django.contrib.auth import get_user_model


class Thing(models.Model):
    title = models.TextField()
    year = models.CharField(max_length=4)
    image = models.URLField(max_length=500)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    thing = models.ForeignKey(Thing, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text
