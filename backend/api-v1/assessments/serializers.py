from rest_framework import serializers
from .models import Assessment

class AssessmentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ('complaint', 'student', 'assigned_nurse', 'symptoms', 'final_prediction', 'lr_prediction', 'rf_prediction', 'gb_prediction', 'final_prediction_similar_diseases', 'final_prediction_treatment', 'final_prediction_description')

class AssessmentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ('assessment_id', 'comments','assigned_doctor') 
    
    # def validate(self, data):
    #     assessment_id = self.context['assessment_id']

    #     return data
    
    # def update(self, instance, validated_data):
    #     instance.comments = validated_data.get('comments', instance.comments)
    #     instance.assigned_doctor = validated_data.get('assigned_doctor', instance.assigned_doctor)
    #     instance.assessment_id = self.context['assessment_id']
    #     instance.save()
    #     return instance
