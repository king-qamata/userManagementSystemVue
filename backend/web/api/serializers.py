from rest_framework import serializers
from userManagement.serializers import UserSerializer
from .models import Administrator, Moderator
from utils import constants
from utils.permissions import is_administrator, is_moderator


class AdministratorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Administrator
        fields = '__all__'


class AdministratorSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = Administrator
        fields = '__all__'

    def validate(self, data):
        """
        Administrator permissions needed
        """

        if not is_administrator(self.context['request'].user):
            raise serializers.ValidationError(constants.PERMISSION_ADMINISTRATOR_REQUIRED)
        return data





class ModeratorSerializer(serializers.ModelSerializer):
    sponsor = UserSerializer()
    user = UserSerializer()

    class Meta:
        model = Moderator
        fields = '__all__'


class ModeratorSerializerCreate(serializers.ModelSerializer):
    sponsor = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Moderator
        fields = '__all__'

    def validate(self, data):
        """
        Administrator permissions needed
        """

        if not is_administrator(self.context['request'].user):
            raise serializers.ValidationError(constants.PERMISSION_ADMINISTRATOR_REQUIRED)
        return data

    def validate_user(self, user):
        """
        Ensure user is not already moderator or higher
        """

        if is_moderator(user):
            raise serializers.ValidationError('User already has moderator permissions')
        return user
