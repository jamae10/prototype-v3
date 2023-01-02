from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed  
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Student, Nurse, Doctor
from .serializers import StudentLoginSerializer, NurseLoginSerializer, DoctorLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class StudentLoginView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        serializer = StudentLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        user = authenticate(
            email=data['email'],
            password=data['password']
            )
        if not user: 
            raise serializers.ValidationError({'detail': 'Incorrect email or password'})

        if not user.is_student == True:
            raise serializers.ValidationError({'detail': 'User is not Student'})
        

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            },
            status=status.HTTP_200_OK
        )

class NurseLoginView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        serializer = NurseLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        
        user = authenticate(
            email=data['email'],
            password=data['password']
            )

        if not user: 
            raise serializers.ValidationError({'detail': 'Incorrect email or password'})

        if not user.is_nurse == True:
            raise serializers.ValidationError({'detail': 'User is not Nurse'})

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            },
            status=status.HTTP_200_OK
        )


class DoctorLoginView(APIView):
    permission_classes = (permissions.AllowAny, )
    # serializer_class = DoctorLoginSerializer

    def post(self, request):
        serializer = DoctorLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        
        user = authenticate(
            email=data['email'],
            password=data['password']
            )
        if not user: 
            raise serializers.ValidationError({'detail': 'Incorrect email or password'})

        if not user.is_doctor == True:
            raise serializers.ValidationError({'detail': 'User is not Doctor'})

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            },
            status=status.HTTP_200_OK
        )
       

class StudentSignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        try:
            data = self.request.data

            name = data['name']
            email = data['email']
            password = data['password']
            password2 = data['password2']
            is_student = data['is_student']

            if is_student == 'True':
                is_student = True
            else:
                is_student = False
            
            if password == password2:
                if User.objects.filter(email=email).exists():
                    return Response({'error': 'Email already exists'})
                else:
                    if len(password) < 6:
                        return Response({'error': 'Password must be at least 6 characters'})
                    else:
                        if is_student:
                            user = User.objects.create_student(email=email, password=password, name=name)
                            try:
                                Student.objects.create(user=user, email=email, name=name)
                                user.save()
                                return Response({'success': 'Student created successfully'})
                            except:
                                return Response({'error': 'Something went wrong in adding the Student in Database'})

                            # user.save()
                            # return Response({'success': 'Student created successfully'})
                        else:
                            return Response({'error': 'User is not a Student'})
            else:
                return Response({'error': 'Password do not match'})

        except:
            return Response({'error': 'Something went wrong when registering an account'})


class NurseSignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        try:
            data = self.request.data

            name = data['name']
            email = data['email']
            password = data['password']
            password2 = data['password2']
            is_nurse = data['is_nurse']

            if is_nurse == 'True':
                is_nurse = True
            else:
                is_nurse = False
            
            if password == password2:
                if User.objects.filter(email=email).exists():
                    return Response({'error': 'Email already exists'})
                else:
                    if len(password) < 6:
                        return Response({'error': 'Password must be at least 6 characters'})
                    else:
                        if is_nurse:
                            user = User.objects.create_nurse(email=email, password=password, name=name)
                            try:
                                Nurse.objects.create(user=user, email=email, name=name)
                                user.save()
                                return Response({'success': 'Nurse created successfully'})
                            except:
                                return Response({'error': 'Something went wrong in adding the Nurse in Database'})

                            # user.save()
                            # return Response({'success': 'Student created successfully'})
                        else:
                            return Response({'error': 'User is not a Nurse'})
            else:
                return Response({'error': 'Password do not match'})

        except:
            return Response({'error': 'Something went wrong when registering an account'})


class DoctorSignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        try:
            data = self.request.data

            name = data['name']
            email = data['email']
            password = data['password']
            password2 = data['password2']
            is_doctor = data['is_doctor']

            if is_doctor == 'True':
                is_doctor = True
            else:
                is_doctor = False
            
            if password == password2:
                if User.objects.filter(email=email).exists():
                    return Response({'error': 'Email already exists'})
                else:
                    if len(password) < 6:
                        return Response({'error': 'Password must be at least 6 characters'})
                    else:
                        if is_doctor:
                            user = User.objects.create_doctor(email=email, password=password, name=name)
                            try:
                                Doctor.objects.create(user=user, email=email, name=name)
                                user.save()
                                return Response({'success': 'Doctor created successfully'})
                            except:
                                return Response({'error': 'Something went wrong in adding the Doctor in Database'})

                            # user.save()
                            # return Response({'success': 'Student created successfully'})
                        else:
                            return Response({'error': 'User is not a Doctor'})
            else:
                return Response({'error': 'Password do not match'})

        except:
            return Response({'error': 'Something went wrong when registering an account'})