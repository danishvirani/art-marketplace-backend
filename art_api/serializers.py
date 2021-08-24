from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from .models import Art
from .models import Artist
from .models import User

class ArtSerializer(serializers.ModelSerializer):

    class Meta:
        model = Art
        fields = ('id', 'title', 'author', 'rating', 'image', 'price', 'description', 'created_date',)
<<<<<<< HEAD

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author'] = ArtistSerializer(
            Artist.objects.get(pk=data['author'])).data
        return data
=======
>>>>>>> 8a30ee6982017c33f9df2335c3be5c5807c38d20

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
<<<<<<< HEAD
        fields = ('id', 'name', 'bio',)
=======
        fields = ('id', 'name', 'bio', 'art',)
>>>>>>> 8a30ee6982017c33f9df2335c3be5c5807c38d20

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
<<<<<<< HEAD
        fields = ('id', 'username', 'password', 'cart',)

    def create(self, validated_data):
        user = User.objects.create(
        username = validated_data['username'],
        password = make_password(validated_data['password'])
        )
        user.save()
        return user

    def update(self,instance,validated_data):
        user = User.objects.get(username=validated_data['username'])
        user.password = make_password(validated_data['password'])
        user.save()
        return user
=======
        fields = ('id', 'username', 'password',)
>>>>>>> 8a30ee6982017c33f9df2335c3be5c5807c38d20
