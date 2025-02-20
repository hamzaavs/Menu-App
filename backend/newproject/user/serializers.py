from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

from .models import Role, User

User = get_user_model()


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = [
            'id',
            'name',
            'description'
        ]


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

        default_role = Role.objects.get(id=2)
        user.roles.add(default_role)

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
    roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'name',
            'surname',
            'phone',
            'roles'
        ]
