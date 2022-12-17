from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Credit, Genre
    
class UserSerializer(serializers.ModelSerializer):
    class CreditSerializer(serializers.ModelSerializer):
        class Meta:
            model = Credit
            fields = ('id',)

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id',)

    followings = CreditSerializer(many=True, read_only=True)
    favorite_genre = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'followings', 'favorite_genre',)

