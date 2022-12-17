from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Credit, Genre

class User(AbstractUser):
    followings = models.ManyToManyField(Credit, related_name='followers', blank=True)
    favorite_genre = models.ManyToManyField(Genre, related_name='genre_lovers', blank=True)    
