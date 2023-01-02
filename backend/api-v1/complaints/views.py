from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Complaint
from .serializers import ComplaintSerializer, PostComplaintSerializer
from rest_framework.views import APIView
import uuid
import datetime
from accounts.models import Student, Nurse
from rest_framework.decorators import api_view
from rest_framework import status

class ComplaintListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    pagination_class = None

class ComplaintView(RetrieveAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

class StatusView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Complaint.objects.filter(initial_diagnosis_status='Pending', assessment_status='Pending')
    serializer_class = ComplaintSerializer
    pagination_class = None



class ComplaintPostView(APIView):
    # permission_classes = (IsAuthenticated, )
    permission_classes = (permissions.AllowAny, )

    def post(self,request,pk,format=None):
        serializer = PostComplaintSerializer(data=request.data)

        # if serializer.objects.filter(**request.data).exists():
        #     raise serializers.ValidationError('This data already exists')

        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Complaint saved!'})
        return Response({'error': 'Complaint was not saved'})