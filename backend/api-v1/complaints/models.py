from django.db import models
from django.utils.timezone import now
from datetime import datetime
from accounts.models import Student, Nurse
from django.utils.translation import gettext_lazy as _


class Complaint(models.Model):

    class Status(models.TextChoices):
        PENDING = "pending", _("Pending")
        DONE = "done", _("Done")
        NONE = "not needed", _("Not Needed")
        
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    complaint_id = models.CharField(max_length=20, unique=True)
    chief_complain = models.CharField(max_length=500, blank=True)
    message = models.CharField(max_length=1000, blank=True)
    illness_period = models.CharField(max_length=500, blank=True)
    medications = models.CharField(max_length=500, blank=True)
    slug = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(default=now)
    received_by = models.ForeignKey(Nurse, on_delete=models.DO_NOTHING, blank=True, null=True)
    received_at = models.DateTimeField(default=datetime.now)
    assessment_status = models.CharField(
        max_length=50, choices=Status.choices, default=Status.PENDING
    )
    initial_diagnosis_status = models.CharField(
        max_length=50, choices=Status.choices, default=Status.PENDING
    )

    def __str__(self):
        return str(self.id)
    