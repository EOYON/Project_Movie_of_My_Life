from rest_framework import serializers
from ..models import Credit, Movie
from .user import UserSerializer

class CreditSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'

    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Credit
        fields = '__all__'
