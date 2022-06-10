
from rest_framework import viewsets, serializers
from books.serializers import UserSerializer
from books.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

