from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(
        required=True, min_length=8, write_only=True
    )

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "password_confirmation")
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 8},
            "email": {"required": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password_confirmation"]:
            raise serializers.ValidationError(
                {"password_confirmation": "as senha não são iguais"}
            )
        return attrs

    def create(self, validated_data):
        del validated_data["password_confirmation"]
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)
