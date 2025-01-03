from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'name',
            'surname',
            'phone'
        ]

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data['name'],
            surname=validated_data['surname'],
            phone=validated_data['phone']
        )
        return user


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = [
            'email',
            'password'
        ]

    def validate(self, data):
        user = authenticate(
            email=data['email'],
            password=data['password']
        )

        if user and user.is_active:
            return user
        raise serializers.ValidationError("Hatalı bilgiler")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'name',
            'surname',
            'phone'
        ]
