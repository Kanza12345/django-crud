from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils.dateparse import parse_datetime
from rest_framework import generics
from .models import Patient, Counsellor, Appointment
from .serializers import PatientSerializer, CounsellorSerializer, AppointmentSerializer 
 
def index(request):
  return HttpResponse("Hello Geeks")


class PatientList(generics.ListCreateAPIView):
  serializer_class = PatientSerializer
  queryset = Patient.objects.all()

# API view for listing all active patients
class ActivePatientList(generics.ListAPIView):
  serializer_class = PatientSerializer
  queryset = Patient.objects.filter(Is_active=True)


class CounsellorList(generics.ListCreateAPIView):
  serializer_class = CounsellorSerializer
  queryset = Counsellor.objects.all()


# API view for listing all active counsellors
class ActiveCounsellorList(generics.ListAPIView):
  serializer_class = CounsellorSerializer
  queryset = Counsellor.objects.filter(Is_active=True)


class AppointmentList(generics.ListCreateAPIView):
  serializer_class = AppointmentSerializer
  queryset = Appointment.objects.all()
       
# API view for listing all active appointments
class ActiveAppointmentList(generics.ListAPIView):
  serializer_class = AppointmentSerializer
  queryset = Appointment.objects.filter(Is_active=True)

# API view for listing all appointments by patients
class AppointmentListByPatient(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return Appointment.objects.filter(Patient=patient_id)
    
# API view for listing all appointments by counsellors
class AppointmentListByCounsellor(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        counsellor_id = self.kwargs['counsellor_id']
        return Appointment.objects.filter(Counsellor=counsellor_id)
    
# API view for listing all appointments by date range 
class AppointmentListByDateRange(generics.ListAPIView):
    # http://localhost:8000/api/appointments/?start_datetime=2023-01-01T00:00:00&end_datetime=2023-10-31T23:59:59
    serializer_class = AppointmentSerializer
    

    def get_queryset(self):
        queryset = Appointment.objects.all()
        start_datetime = parse_datetime(self.request.query_params.get('start_datetime'))
        end_datetime = parse_datetime(self.request.query_params.get('end_datetime'))

        if start_datetime is not None and end_datetime is not None:
            queryset =  queryset.filter(Appointment_Date__gte=start_datetime, Appointment_Date__lte=end_datetime).order_by('Appointment_Date')

        return queryset