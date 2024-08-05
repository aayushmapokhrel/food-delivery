from rest_framework import serializers

# from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.validators import ValidationError

from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, allow_blank=True)

    class Meta:
        model = User
        fields = ["username", "password", "email"]

    def validate(self, validated_data):
        user = validated_data["username"]
        if len(user) < 8:
            raise ValidationError(
                {
                    "username": "Username should be more 8 cha"
                    }
                    )
        return validated_data

    def validate_password(self, password):
        if len(password) < 8:
            raise ValidationError(
                {
                    "password": "password should be more 8 cha"
                    }
                    )
        return password


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]

    def to_representation(self, instance):
        token = RefreshToken.for_user(instance)
        data = super().to_representation(instance)
        data["access_token"] = str(token.access_token)
        data["refresh_token"] = str(token)
        return data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError(
                        "User account is disabled."
                        )
                data["user"] = user
            else:
                raise serializers.ValidationError(
                    "Unable to log in with provided credentials."
                )
        else:
            raise serializers.ValidationError(
                "Must include 'username' and 'password'."
                )

        return data
