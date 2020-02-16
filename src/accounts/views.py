import json

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from rest_framework import permissions, status, views, viewsets
from rest_framework.response import Response

from .models import User
from .permissions import IsAccountOwner
from .serializers import UserSerializer, LoginSerializer


class UserView(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [IsAccountOwner]


    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)
        
        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
    serializer_class = LoginSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            account = authenticate(
                username=serializer.data['email'],
                password=serializer.data['password']
            )

        if account is not None:
            if account.is_active:
                login(request, account)

                serialized = UserSerializer(account)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)