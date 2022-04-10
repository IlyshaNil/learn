from rest_framework import viewsets
from . import serializers
from django.contrib.auth.models import User



class UserListViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetailViewSet(viewsets.ModelViewSet ):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer