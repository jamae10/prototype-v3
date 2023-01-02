from rest_framework import serializers
from .models import UserAccount
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib import auth

class StudentLoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=100)
    is_student = serializers.BooleanField(read_only=True)


    class Meta:
        model = User
        fields = ['email', 'password', 'is_student']

class NurseLoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=100)
    is_nurse = serializers.BooleanField(read_only=True)


    class Meta:
        model = User
        fields = ['email', 'password', 'is_nurse']    

class DoctorLoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=100)
    is_doctor = serializers.BooleanField(read_only=True)


    class Meta:
        model = User
        fields = ['email', 'password', 'is_doctor']    