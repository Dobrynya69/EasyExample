from django.db import models

class Movie(models.Model):
    title = models.TextField()
    year = models.CharField(max_length=4)
    image = models.URLField()

