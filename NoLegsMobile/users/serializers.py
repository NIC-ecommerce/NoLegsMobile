from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'role', 'car_model', 'phone']

from rest_framework import serializers
from .models import CustomUser

class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'role', 'car_model','phone']
        extra_kwargs = {
            'password': {'write_only': True},
            'car_model': {'required': False}
        }

    def validate(self, data):
        role = data.get('role')
        car_model = data.get('car_model')

        if role == CustomUser.DRIVER and not car_model:
            raise serializers.ValidationError("Car model is required for drivers.")

        return data

    def create(self, validated_data):
        car_model = validated_data.pop('car_model', None)
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            phone=validated_data['phone'],
            role=validated_data.get('role')
        )
        if car_model and validated_data.get('role') == CustomUser.DRIVER:
            user.car_model = car_model
            user.save()
        return user



class CustomUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['role', 'car_model', 'phone']


from rest_framework import serializers

class CustomUserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)
