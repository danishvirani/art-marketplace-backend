from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from .models import Art
from .models import Artist
from .models import User

class ArtSerializer(serializers.ModelSerializer):

    class Meta:
        model = Art
        fields = ('id', 'title', 'author', 'rating', 'image', 'price', 'description', 'created_date',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author'] = ArtistSerializer(
            Artist.objects.get(pk=data['author'])).data
        return data

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'name', 'bio',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'cart', 'use',)

    def create(self, validated_data):
        user = User.objects.create(
        username = validated_data['username'],
        use = validated_data['use'],
        password = make_password(validated_data['password'])
        )
        user.save()
        return user

    def update(self,instance,validated_data):
        user = User.objects.get(username=validated_data['username'])
        user.password = make_password(validated_data['password'])
        user.save()
        return user
