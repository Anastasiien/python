from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class CollectionItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collection_items')
    genres = models.ManyToManyField(Genre, related_name='collection_items')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

