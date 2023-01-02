from django.contrib import admin
from .models import Diagnosis

class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('id','diagnosis_id','student','assigned_doctor', 'initial_diagnosis', 'created_at')
    list_display_links = ('id', 'diagnosis_id', 'student')
    search_fields = ('diagnosis_id','assigned_doctor','student' )
    list_per_page = 25

admin.site.register(Diagnosis, DiagnosisAdmin)
