from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/popular/', views.popular_movie_list),
    path('movies/recommended/', views.recommended_movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/reviews/', views.review_create),
    path('movies/reviews/<review_pk>/', views.review_detail),
    path('movies/genres/<int:genre_pk>/follow/', views.genre_follow),
    path('credits/<int:credit_pk>/follow/', views.credit_follow),
]
