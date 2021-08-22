from rest_framework import serializers
from .models import Art
from .models import Artist
from .models import User

class ArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Art
        fields = ('id', 'title', 'author', 'rating', 'image', 'price', 'description', 'created_date',)
        depth = 1

class ArtistSerializer(serializers.ModelSerializer):
    art = ArtSerializer(many=True)

    class Meta:
        model = Artist
        fields = ('id', 'name', 'bio', 'art',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',)
