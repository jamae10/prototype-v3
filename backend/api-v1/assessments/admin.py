from django.contrib import admin
from .models import Assessment

class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id','assessment_id','student','assigned_nurse', 'complaint', 'created_at', 'initial_diagnosis_status')
    list_display_links = ('id', 'assessment_id', 'complaint')
    search_fields = ('name','subject')
    list_per_page = 25

admin.site.register(Assessment, AssessmentAdmin)