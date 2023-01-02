from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import DiagnosisPostSerializer
from rest_framework import permissions
from .models import Assessment
from complaints.models import Complaint
from assessments.models import  Assessment
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class DiagnosisCreateView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, pk, format=None):
        data = self.request.data
        assessment = data.get('assessment')
        assessment_object = Assessment.objects.get(id=assessment)
        serializer = DiagnosisPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(is_sent=True)
            assessment_object.initial_diagnosis_status = 'Done'
            assessment_object.save()
            return Response({'success':'Diagnosis posted'})
        else:
            return Response({'error':'Diagnosis not posted'})
