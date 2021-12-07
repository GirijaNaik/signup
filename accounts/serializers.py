from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.password_validation import validate_password

User = get_user_model()
class SignupSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        read_only_fields = ('id', 'is_active', 'is_staff')
        extra_kwargs = {

                       'password': {'write_only': True}
        }

        def validate_password(self, value):
            validate_password(value)
            return value

        def create(self, validated_data):
            user = get_user_model()(**validated_data)
            user.set_password(validated_data['password'])
            user.save()
            return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)



class EmptySerializer(serializers.Serializer):
    pass

class UserRegisterSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'email', 'password', 'first_name', 'last_name')

        def validate_email(self, value):
            user = User.objects.filter(email = 'email')
            if user:
                raise serializers.ValidationError("Email is already taken")
            return BaseUserManager.normalize_email(value)

        def validate_password(self, value):
            password_validation.validate_password(value)
            return value

class PasswordChangeSerializer(serializers.Serializer):
        current_password = serializers.CharField(required=True)
        new_password = serializers.CharField(required=True)

        def validate_current_password(self, value):
            if not self.context['request'].user.check_password(value):
                raise serializers.ValidationError('Current password does not match')
            return value

        def validate_new_password(self, value):
            password_validation.validate_password(value)
            return value

class UserLogoutSerializer(serializers.Serializer):
    pass




