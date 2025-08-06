from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError #August 3, 2025

User = get_user_model()

class UsersCreateSerializer(UserCreateSerializer):
    group = serializers.CharField(write_only=True, required = True)
    class Meta(UserCreateSerializer.Meta):
        model=User
        fields= (*UserCreateSerializer.Meta.fields, "group")
    
    def validate_group(self, value):
        if not Group.objects.filter(name=value).exists():
            raise serializers.ValidationError(f"Group '{value}' does not exist.")
        return value
    
    def perform_create(self, validate_data):
        group_name = self.initial_data.get("group")
        user = super().perform_create(validate_data)


        if group_name:
            group = Group.objects.get(name=group_name)
            user.groups.add(group)
        return user
    
class LogoutUserSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs
    def save(self, **kwargs):
        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except TokenError as e:
            raise serializers.ValidationError("Invalid or already blacklisted token") from e
    