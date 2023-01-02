from django.urls import path
from .views import AssessmentCreateView, AssessmentUpdateView

urlpatterns = [
    path('create/<pk>', AssessmentCreateView.as_view()),
    path('assign/<pk>', AssessmentUpdateView.as_view()),
]