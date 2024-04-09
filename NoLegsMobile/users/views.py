from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from . import serializers
from .models import CustomUser

class CustomUserCreateView(generics.CreateAPIView):
    """
    Если что переходить по http://127.0.0.1:8000/api/users/create/ и смотреть какие поля надо регать
    """
    serializer_class = serializers.CustomUserCreateSerializer

class CustomUserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer

class CustomUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.CustomUserUpdateSerializer
    permission_classes = [IsAuthenticated]
