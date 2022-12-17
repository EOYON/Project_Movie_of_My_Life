from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Credit(models.Model):
    name = models.CharField(max_length=100)
    job = models.TextField(max_length=50)
    profile_path = models.TextField(max_length=200, null=True)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    vote_average = models.FloatField()
    poster_path = models.TextField(max_length=200)
    genre = models.ManyToManyField(Genre)
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    overview = models.TextField()
    credit = models.ManyToManyField(Credit, related_name='movies')

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vote_point = models.FloatField()
    content = models.CharField(max_length=100, null=True)