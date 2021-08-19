from rest_framework import generics
from .serializers import ArtSerializer
from .models import Art

from .serializers import ArtistSerializer
from .models import Artist

from .serializers import UserSerializer
from .models import User
# Create your views here.

class ArtList(generics.ListCreateAPIView):
    queryset = Art.objects.all().order_by('id')
    serializer_class = ArtSerializer

class ArtDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Art.objects.all().order_by('id')
    serializer_class = ArtSerializer

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all().order_by('id')
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all().order_by('id')
    serializer_class = ArtistSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
