from rest_framework import serializers
from .models import CustomUser
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=50, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'profile_image', 'username', 'facebook',
                  'tweeter', 'linked_in']

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": ("email already exists")})
        if CustomUser.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": ("username already exists")})
        return super().validate(args)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=60, min_length=7,write_only=True)
    tokens=serializers.CharField(max_length=60,read_only=True)

    class Meta:
        model = CustomUser
        fields = [ 'email', 'password','tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed("Invalid cridentials,Please Try again")

        return {
            "email": user.email,
            "username": user.username,
            "tokens": user.tokens
        }

        return super().validate(attrs)
