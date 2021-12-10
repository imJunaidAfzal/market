from django.shortcuts import render
from .serializer import UserSerializer, LoginSerializer
from .models import CustomUser
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response


# Create your views here.
class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"user": serializer.data, "msg": "User created successfully"})


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serialzer = self.serializer_class(data=request.data)
        serialzer.is_valid(raise_exception=True)
        return Response(serialzer.data)
