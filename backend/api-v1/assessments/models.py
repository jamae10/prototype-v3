from django.db import models
from django.utils.timezone import now
from datetime import datetime
from accounts.models import Student, Nurse, Doctor
from complaints.models import Complaint
from django.utils.translation import gettext_lazy as _


class Assessment(models.Model):

    class Status(models.TextChoices):
        PENDING = "pending", _("Pending")
        DONE = "done", _("Done")
        NONE = "not needed", _("Not Needed")
    
    class Response(models.TextChoices):
        YES = "yes", _("Yes")
        NO = "no", _("No")

    complaint = models.OneToOneField(Complaint, on_delete=models.DO_NOTHING,blank=True, null=True)
    assessment_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING,blank=True, null=True)
    assigned_nurse = models.ForeignKey(Nurse, on_delete=models.DO_NOTHING,blank=True, null=True)
    symptoms = models.CharField(max_length=1000)
    # findings = models.CharField(max_length=500, blank=True, null=True)
    comments = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(default=now)
    assigned_doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, blank=True, null=True)
    date_assigned = models.DateTimeField(default=datetime.now)
    assessment_status = models.CharField(
        max_length=50, choices=Status.choices, default=Status.PENDING
    )
    initial_diagnosis_status = models.CharField(
        max_length=50, choices=Status.choices, default=Status.PENDING
    )
    for_initial_diagnosis = models.CharField(
        max_length=50, choices=Response.choices, default=Response.YES
    )
    final_prediction = models.CharField(max_length=255, blank=True, null=True)
    lr_prediction = models.CharField(max_length=255, blank=True, null=True)
    rf_prediction = models.CharField(max_length=255, blank=True, null=True)
    gb_prediction = models.CharField(max_length=255, blank=True, null=True)

    final_prediction_similar_diseases = models.CharField(max_length=500, blank=True, null=True)
    lr_prediction_similar_diseases = models.CharField(max_length=500, blank=True, null=True)
    rf_prediction_similar_diseases = models.CharField(max_length=500, blank=True, null=True)
    gb_prediction_similar_diseases = models.CharField(max_length=500, blank=True, null=True)

    final_prediction_treatment = models.CharField(max_length=500, blank=True, null=True)
    lr_prediction_treatment = models.CharField(max_length=500, blank=True, null=True)
    rf_prediction_treatment = models.CharField(max_length=500, blank=True, null=True)
    gb_prediction_treatment = models.CharField(max_length=500, blank=True, null=True)

    final_prediction_description = models.CharField(max_length=500, blank=True, null=True)
    lr_prediction_description = models.CharField(max_length=500, blank=True, null=True)
    rf_prediction_description = models.CharField(max_length=500, blank=True, null=True)
    gb_prediction_description = models.CharField(max_length=500, blank=True, null=True)
    # slug = models.CharField(max_length=200, unique=True)


    def __str__(self):
        return str(self.id)
    