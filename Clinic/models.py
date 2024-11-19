from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class CustomUser(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )

class DoctorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    specialty = models.CharField(max_length=200)

class PatientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField()
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

class Appointment(models.Model):
    Patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    PhoneNumber = models.CharField(max_length=20)
    Email = models.EmailField()
    Date = models.DateField()
    Time = models.TimeField()
    Department = models.CharField(max_length=100)
    Doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    Reason = models.TextField()

class Department(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    