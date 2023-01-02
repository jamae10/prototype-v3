from rest_framework import serializers
from .models import Diagnosis

class DiagnosisPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ('complaint', 'assessment', 'student', 'initial_diagnosis','recommendations', 'additional_notes', 'assigned_doctor')

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = '__all__'