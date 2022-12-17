from django.contrib import admin
from .models import Genre, Credit, Movie, Review

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Credit)
admin.site.register(Review)