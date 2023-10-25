
from django.urls import path
from .views import PatientList, CounsellorList, AppointmentList, ActivePatientList, ActiveCounsellorList, ActiveAppointmentList, AppointmentListByPatient, AppointmentListByDateRange

#importing the views.py file into this code
from . import views
urlpatterns=[
    path('',views.index),
    path('patient/', PatientList.as_view()),
    path('counsellor/', CounsellorList.as_view()),
    path('appointment/', AppointmentList.as_view()),
    path('active-patients/', ActivePatientList.as_view()),
    path('active-counsellors/', ActiveCounsellorList.as_view()),
    path('active-appointments/', ActiveAppointmentList.as_view()),
    path('appointment-list/<uuid:patient_id>/', AppointmentListByPatient.as_view()),
    path('appointment-list/<uuid:counsellor_id>/', AppointmentListByPatient.as_view()),
    path('appointments/', AppointmentListByDateRange.as_view()),
]