from django.contrib import admin
from .models import Patient, Counsellor, Appointment
# Register your models here.

#Patient list for admin dashboard with search fields
class PatientAdmin(admin.ModelAdmin):
    search_fields = ['Name', 'Email']  # Replace with the fields you want to search on
    list_display = ['Id', 'Name', 'Email', 'Is_active']

#Counsellor list for admin dashboard with search fields
class CounsellorAdmin(admin.ModelAdmin):
    search_fields = ['Name', 'Email']  # Replace with the fields you want to search on
    list_display = ['Id', 'Name', 'Email', 'Is_active']

#Appointment list for admin dashboard with search fields
class AppointmentAdmin(admin.ModelAdmin):
    search_fields = ['Patient', 'Counsellor']  # Replace with the fields you want to search on
    list_display = ['Id', 'Patient', 'Counsellor', 'Appointment_Date', 'Is_active']


admin.site.register(Patient, PatientAdmin)
admin.site.register(Counsellor, CounsellorAdmin)
admin.site.register(Appointment, AppointmentAdmin)
