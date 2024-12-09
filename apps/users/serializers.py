from apps.users.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators = [validate_password,])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Пароли отличаются"})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user



class LoginSerializer(serializers.Serializer):
        username = serializers.CharField(required = True)
        password = serializers.CharField(write_only = True, required = True)

        def post(self, attrs):
            username = attrs.get('username')
            password = attrs.get('username')

            user = authenticate(username=username, password=password)
            if not user:
                 raise serializers.ValidationError({"detail": "Неверные учетные данные"})
            

            attrs['user'] = user
            return attrs


  