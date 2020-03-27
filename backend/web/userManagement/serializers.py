from rest_framework import serializers
from . import models
from .models import CustomUser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username', )



class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

class UserSerializerLogin(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = models.CustomUser
        fields = ( 'username', 'password','token')
        extra_kwargs = {'password': {'write_only': True}}

    @staticmethod
    def get_profile(user):
        """
        Get or create profile
        """

        user, created = CustomUser.objects.get_or_create(user=user)
        return UserSerializer(user, read_only=True).data    


    @staticmethod
    def get_token(user):
        """
        Get or create token
        """

        token, created = Token.objects.get_or_create(user=user)
        return token.key

