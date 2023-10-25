import uuid
from django.db import models

# Create your models here.

# Patient model with the required fields
class Patient(models.Model):
    Id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) 
    Name = models.CharField(max_length=500)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=500)
    Is_active = models.BooleanField(default=True)

    def __str__ (self):
        return self.Name
    
# Counsellor model with the required fields
class Counsellor(models.Model):
    Id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) 
    Name = models.CharField(max_length=500)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=500)
    Is_active = models.BooleanField(default=True)

    def __str__ (self):
        return self.Name
    
# Appointment model with the required fields
class Appointment(models.Model):
    Id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    Patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    Counsellor = models.ForeignKey('Counsellor', on_delete=models.CASCADE)
    Appointment_Date = models.DateTimeField()
    Is_active = models.BooleanField(default=True)