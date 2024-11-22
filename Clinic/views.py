from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import DoctorRegistrationForm, PatientRegistrationForm
from django.http import HttpResponse
from .models import DoctorProfile, Department

# Create your views here.
def register_doctor(request):
    if request.method =='POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        
    else:
        form =DoctorRegistrationForm()

    return render(request, 'register_doctor.html', {'form': form})
    
def register_patient(request):
    if request.method == 'POST':
        form =PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        
    else:
        form = PatientRegistrationForm()

    return render(request, 'register_patient.html', {'form': form})

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def doctors_list(request):
    doctors=DoctorProfile.objects.all()
    return render(request, 'doctors.html', {'doctors' : doctors})

def departments_list(request):
    departments = Department.objects.all()
    return render(request, 'departments.html', {'departments' : departments})

def appointment(request):
    return render(request, 'appointment.html', {})

def video_conference(request):
    return render(request, 'video_conference.html', {})

def meeting(request):
    return render(request, 'meeting.html', {})

def join_room(request):
    return render(request, 'join_room.html', {})