from django.contrib import admin
from .models import Student, Nurse, Doctor

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','email', 'student_id', 'date_created')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name', 'email')
    list_per_page = 25

class NurseAdmin(admin.ModelAdmin):
    list_display = ('id','name','email', 'nurse_id', 'date_created')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name', 'email')
    list_per_page = 25

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id','name','email', 'doctor_id', 'date_created')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name', 'email')
    list_per_page = 25

admin.site.register(Student, StudentAdmin)
admin.site.register(Nurse, NurseAdmin)
admin.site.register(Doctor, DoctorAdmin)
