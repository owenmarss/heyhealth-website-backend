from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from .models import User

class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    nama_lengkap = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=45)
    usia = serializers.IntegerField(default=0)
    nomor_telepon = serializers.CharField(max_length=20)
    password = serializers.CharField(min_length=8, write_only=True)
    
    class Meta:
        model = User
        fields = ["email", "nama_lengkap", "username", "usia", "nomor_telepon", "password"]

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs["email"]).exists()
        if email_exists:
            raise ValidationError("Email has already been used")
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user