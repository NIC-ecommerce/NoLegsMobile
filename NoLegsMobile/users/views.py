from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from . import serializers
from .models import CustomUser

class CustomUserCreateView(generics.CreateAPIView):
    serializer_class = serializers.CustomUserCreateSerializer

class CustomUserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer

class CustomUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.CustomUserUpdateSerializer
    permission_classes = [IsAuthenticated]
