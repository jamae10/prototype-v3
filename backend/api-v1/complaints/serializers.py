from rest_framework import serializers
from .models import Complaint
from accounts.models import Student, Nurse
import uuid, datetime

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'


class PostComplaintSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Complaint
        fields = ('student', 'name', 'chief_complain', 'message','illness_period', 'medications')

