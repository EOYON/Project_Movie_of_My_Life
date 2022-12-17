from rest_framework import serializers
from ..models import Movie, Credit, Genre, Review
# from .user import UserSerializer
from django.contrib.auth import get_user_model

class GenreSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'

    movie_set = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    class CreditSerializer(serializers.ModelSerializer):
        class Meta:
            model = Credit
            fields = ('id',)

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', )

    credit = CreditSerializer(many=True, read_only=True)
    genre = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class CreditSerializer(serializers.ModelSerializer):
        class Meta:
            model = Credit
            fields = '__all__'

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'

    class ReviewSerializer(serializers.ModelSerializer):
        class UserSerializer(serializers.ModelSerializer):
    
            class Meta:
                model = get_user_model()
                fields = ('username',)
        
        user = UserSerializer(read_only=True)        
        # user = UserSerializer(read_only=True)

        class Meta:
            model = Review
            fields = ('id', 'user', 'vote_point', 'content',)

    credit = CreditSerializer(many=True, read_only=True)
    genre = GenreSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
