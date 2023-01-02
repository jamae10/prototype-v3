from django.urls import path
from .views import StudentSignupView,NurseSignupView, DoctorSignupView, StudentLoginView, NurseLoginView, DoctorLoginView

urlpatterns = [
    path('signup-student', StudentSignupView.as_view()),
    path('signup-nurse', NurseSignupView.as_view()),
    path('signup-doctor', DoctorSignupView.as_view()),
    path('login-student', StudentLoginView.as_view()),
    path('login-nurse', NurseLoginView.as_view()),
    path('login-doctor', DoctorLoginView.as_view()),
]