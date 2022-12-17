import random as rrandom
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from .serializers.movie import MovieListSerializer, MovieSerializer, GenreSerializer
from .serializers.credit import CreditSerializer
from .serializers.review import ReviewSerializer
from .serializers.user import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Movie, Credit, Genre, Review


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def popular_movie_list(request):
    movies = get_list_or_404(Movie)

    # 1. 인기순
    hot_movies = sorted(movies, key=lambda x: x.popularity, reverse=True)[:28]
    text = '지금 뜨는 영화'
    serializer = MovieListSerializer(hot_movies, many=True)

    hot = {
        'text': text,
        'movies': serializer.data
    }

    # 2. 평점순
    best_movies = rrandom.sample(
        sorted(movies, key=lambda x: x.vote_average, reverse=True)[:100], 28)
    text = '디렉터가 추천하는 영화'
    serializer = MovieListSerializer(best_movies, many=True)

    best = {
        'text': text,
        'movies': serializer.data
    }

    # 3. 랜덤
    random_movies = rrandom.sample(movies, 28)
    text = '오늘은 이거다'
    serializer = MovieListSerializer(random_movies, many=True)

    random = {
        'text': text,
        'movies': serializer.data
    }

    result = {
        'hot': hot,
        'best': best,
        'random': random,
    }
    return Response(result)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommended_movie_list(request):

    result = {}
    user_serializer = UserSerializer(request.user)

    # 1. 배우
    credit_liked = user_serializer.data['followings']

    for credit_path in credit_liked:
        credit = get_object_or_404(Credit, pk=credit_path['id'])
        credit_movies = CreditSerializer(credit).data['movies']
        credit_movies = sorted(
            credit_movies, key=lambda x: x['vote_average'], reverse=True)
        if credit.job == 'Director':
            text = f'{credit.name} 감독의 다른 작품'
        else:
            text = f'{credit.name}의 출연 영화'

        movie_serializer = MovieListSerializer(credit_movies, many=True)

        credit_data = {
            'text': text,
            'movies': movie_serializer.data
        }

        result[credit.name] = credit_data

    # 2. 장르
    genre_liked = user_serializer.data['favorite_genre']
    for genre in genre_liked:
        genre = get_object_or_404(Genre, pk=genre['id'])

        genre_movies = GenreSerializer(genre).data['movie_set']
        genre_movies = rrandom.sample(
            sorted(genre_movies, key=lambda x: x['vote_average'], reverse=True)[:50], 28)

        text = f'당신이 좋아하는 {genre.name} 장르'
        genre_serializer = MovieListSerializer(genre_movies, many=True)

        genre_data = {
            'text': text,
            'movies': genre_serializer.data
        }

        result[genre.name] = genre_data

    return Response(result)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def credit_follow(request, credit_pk):
    credit = get_object_or_404(Credit, pk=credit_pk)
    # 언팔로우
    if request.user.followings.filter(pk=credit_pk).exists():
        request.user.followings.remove(credit)
    # 팔로우
    else:
        request.user.followings.add(credit)
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def genre_follow(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    # 언팔로우
    if request.user.favorite_genre.filter(pk=genre_pk).exists():
        request.user.favorite_genre.remove(genre)
    # 팔로우
    else:
        request.user.favorite_genre.add(genre)
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
