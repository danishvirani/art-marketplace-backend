from rest_framework import serializers
from .models import Art
from .models import Artist
from .models import User

class ArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Art
        fields = ('id', 'title', 'author', 'rating', 'image', 'price', 'description', 'created_date',)

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name', 'bio', 'art',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',)
