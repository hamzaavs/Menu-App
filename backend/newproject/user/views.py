from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login, logout
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, RoleSerializer
from .models import User, Role


# Create your views here.
def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    roles = list(user.roles.values_list('name', flat=True))
    refresh['roles'] = roles

    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh),
    }


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Kayıt Olunmuştur',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data
            tokens = get_token_for_user(user)
            login(request, user)

            response = Response({
                'message': 'Giriş Yapıldı',
                'access_token': tokens['access'],
                'refresh_token': tokens['refresh']
            }, status=status.HTTP_200_OK)

            response.set_cookie(
                key='access_token',
                value= tokens['access'],
                httponly=True,
                samesite='Lax',
                secure=True
            )

            response.set_cookie(
                key='refresh_token',
                value= tokens['refresh'],
                httponly=True,
                samesite='Lax',
                secure=True
            )
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Çıkış yapıldı"}, status=status.HTTP_200_OK)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class RoleCreateView(APIView):
    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Rol oluşturuldu',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoleAssignView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            role_id = request.data.get('role_id', [])
            roles = Role.objects.filter(id__in=role_id)
            user.roles.set(roles)

            return Response({
                'message': 'Rol Atandı'
            }, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({
                'message': 'Kullanıcı bulunamadı'
            }, status=status.HTTP_400_BAD_REQUEST)
