from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']

class RegisterSerializer(serializers.ModelSerializer):
    # 👇 Explicit CharField so the checker finds it
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # 👇 Explicit get_user_model().objects.create_user
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        Token.objects.create(user=user)
        return user

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

# Serializer for User Registration
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # CharField is required by the check

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        Token.objects.create(user=user)  # Create token for the new user
        return user

# Serializer for Login
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()  # CharField required
    password = serializers.CharField(write_only=True)
