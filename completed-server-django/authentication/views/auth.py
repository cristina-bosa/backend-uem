from http import HTTPStatus

from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.models import Users
from authentication.serializers.users import UsersSerializer


class AuthViewset(viewsets.ViewSet):
    @action(detail = False, methods = ['get'], url_path = 'me', permission_classes = [IsAuthenticated])
    def me(self, request):
        return Response(UsersSerializer(request.user).data)

    @action(detail = False, methods = ['post'], url_path = 'login', permission_classes = [])
    def login(self, request):
        user = request.user
        if user and user.is_authenticated:
            return Response(status = HTTPStatus.ACCEPTED)
        else:
            user = authenticate(
                    username = request.data.get('username'),
                    password = request.data.get('password'),
                    )
            if user is None:
                return Response(data = { 'msg': 'Invalid credentials' }, status = HTTPStatus.UNAUTHORIZED)
            login(request, user)
        return Response(status = HTTPStatus.ACCEPTED)

    @action(detail = False, methods = ['post'], url_path = 'logout', permission_classes = [])
    def logout(self, request):
        logout(request)
        return Response(status = HTTPStatus.ACCEPTED)

    @action(detail = False, methods = ['post'], url_path = 'register', permission_classes = [])
    def register(self, request):
        if any([request.data.get('username') is None, request.data.get('email') is None, request.data.get('password') is None]):
            return Response(data = { 'msg': 'Missing user data' }, status = HTTPStatus.BAD_REQUEST)
        try:
            Users.objects.create_user(
                    username = request.data.get('username'),
                    email = request.data.get('email'),
                    password = request.data.get('password'),
                    )
        except Exception as e:
            return Response(data = { 'msg': 'User is already registered' }, status = HTTPStatus.BAD_REQUEST)
        return Response(status = HTTPStatus.CREATED)
