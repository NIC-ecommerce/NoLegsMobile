from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from . import serializers
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate

class CustomUserCreateView(generics.CreateAPIView):
    """
    Создание пользователя.

    URL: /api/users/create/
    Метод: POST

    Request Body:
    {
        "username": "string",
        "email": "string",
        "password": "string"
    }

    Response:
    {
        "message": "User registered successfully.",
        "user": {
            "id": "integer",
            "username": "string",
            "email": "string"
        }
    }
    """
    serializer_class = serializers.CustomUserCreateSerializer

class CustomUserListView(generics.ListAPIView):
    """
    Получение списка пользователей.

    URL: /api/users/
    Метод: GET

    Response:
    [
        {
            "id": "integer",
            "username": "string",
            "email": "string"
        }
    ]
    """
    queryset = CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer

class CustomUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Получение, обновление и удаление пользователя.

    URL: /api/users/<id>/
    Методы: GET, PUT, PATCH, DELETE

    Request Body (PUT, PATCH):
    {
        "username": "string",
        "email": "string"
    }

    Response:
    {
        "id": "integer",
        "username": "string",
        "email": "string"
    }
    """
    queryset = CustomUser.objects.all()
    serializer_class = serializers.CustomUserUpdateSerializer
    permission_classes = [IsAuthenticated]


class CustomUserRegistrationView(APIView):
    """
    Регистрация пользователя.

    URL: /api/users/register/
    Метод: POST

    Request Body:
    {
        "username": "string",
        "email": "string",
        "password": "string"
    }

    Response:
    {
        "message": "User registered successfully.",
        "user": {
            "id": "integer",
            "username": "string",
            "email": "string"
        }
    }
    """
    def post(self, request):
        serializer = serializers.CustomUserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "User registered successfully.",
                "user": serializer.data,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomUserLoginView(APIView):
    """
    Вход пользователя.

    URL: /api/users/login/
    Метод: POST

    Request Body:
    {
        "username": "string",
        "password": "string"
    }

    Response:
    {
        "refresh": "string",
        "access": "string"
    }
    """
    def post(self, request, *args, **kwargs):
        serializer = serializers.CustomUserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    }
                )
            else:
                return Response(
                    {"error": "Invalid credentials"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

class CustomUserLogoutView(APIView):
    """
    Выход пользователя.

    URL: /api/users/logout/
    Метод: POST

    Request Body:
    {
        "refresh_token": "string"
    }

    Response:
    {
        "message": "Logout successful"
    }
    """
    def post(self, request):

        try:
            refresh_token = request.data.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)
