from django.urls import path
from .views import DiagnosisCreateView

urlpatterns = [
    path('create/<pk>', DiagnosisCreateView.as_view()),
]