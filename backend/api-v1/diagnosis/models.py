from django.db import models
from django.utils.timezone import now
from datetime import datetime
from accounts.models import Student, Nurse, Doctor
from complaints.models import Complaint
from assessments.models import Assessment
from django.utils.translation import gettext_lazy as _


class Diagnosis(models.Model):

    complaint = models.OneToOneField(Complaint, on_delete=models.DO_NOTHING)
    assessment = models.OneToOneField(Assessment, on_delete=models.DO_NOTHING)
    diagnosis_id = models.CharField(max_length=20, unique=True)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    initial_diagnosis = models.CharField(max_length=3000)
    recommendations = models.CharField(max_length=3000)
    additional_notes = models.CharField(max_length=3000, blank=True)
    created_at = models.DateTimeField(default=now)
    assigned_doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    is_sent = models.BooleanField(default=False)


    def __str__(self):
        return str(self.id)
    