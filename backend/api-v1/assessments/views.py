from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import AssessmentPostSerializer, AssessmentUpdateSerializer
from rest_framework import permissions
from .utils import predictDisease
from .models import Assessment
from accounts.models import Doctor
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class AssessmentCreateView(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self, request, pk, format=None):
        
        # serializer = AssessmentSerializer(data=request.data)
        data = self.request.data
        # symptoms = self.request.POST.getlist('symptoms')
        # add_data = dict(request.data)
        symptoms = self.request.data['symptoms']
        results = {}
        symptom = ''
        for elements in symptoms:
            symptom += elements
        symptom = symptom[:-1]

        try: 
            results = predictDisease(symptom)
            serializer = AssessmentPostSerializer(data=request.data)
            try:
                findings = results['predictions']
                final_prediction = results['final_prediction']
                lr_prediction= results['lr_prediction']
                rf_prediction= results['rf_prediction']
                gb_prediction= results['gb_prediction']

                description = results['gb_prediction']
                similarDiseases = results['similarDiseases']
                treatment = results['treatment']

                if serializer.is_valid():
                    serializer.save(final_prediction=final_prediction, lr_prediction=lr_prediction,rf_prediction=rf_prediction,gb_prediction=gb_prediction,final_prediction_description=description,final_prediction_treatment=treatment,final_prediction_similar_diseases=similarDiseases)
                    return Response({'success': 'Assessment saved!'})
                else:
                    return Response(print(serializer.errors))

            except:
                return Response({'error': 'Something went wrong in adding the Assessment in Database'})
            
        except:
            return Response({'error': 'Something went wrong in predicting'})

class AssessmentUpdateView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = AssessmentUpdateSerializer

    def get(self, request, pk, *args, **kwargs):
        try:
            assessment_id = request.query_params['assessment_id']
            if assessment_id != None:
                assessment = Assessment.objects.get(assessment_id = assessment_id)
                serializer = AssessmentUpdateSerializer(assessment)
        except:
            assessments = self.get_queryset()
            serializer = AssessmentUpdateSerializer(assessments, many=True)
        return Response(serializer.data)

    def patch(self, request, pk, *args, **kwargs):
        # data = request.data
        assessment_id = self.request.data.get('assessment_id')
        assigned_doctor = self.request.data.get('assigned_doctor')
        assessment_object = Assessment.objects.get(assessment_id=assessment_id)
        

        assessment_object.assessment_id = request.data.get('assessment_id', assessment_object.assessment_id)
        assessment_object.comments = request.data.get('comments', assessment_object.comments)
        assessment_object.assigned_doctor = Doctor.objects.get(id=assigned_doctor)

        assessment_object.save()

        serializer = AssessmentUpdateSerializer(assessment_object)
        return Response ({'success': 'Assessment record assigned for diagnosis'})