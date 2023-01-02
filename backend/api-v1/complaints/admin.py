from django.contrib import admin
from .models import Complaint

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id','complaint_id','chief_complain', 'name', 'created_at', 'assessment_status','initial_diagnosis_status')
    list_display_links = ('id', 'complaint_id', 'name')
    search_fields = ('name','chief_complain')
    list_per_page = 25

admin.site.register(Complaint, ComplaintAdmin)