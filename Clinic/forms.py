from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, DoctorProfile, PatientProfile

class DoctorRegistrationForm(UserCreationForm):
    specialty = forms.CharField(max_length=100)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'specialty', 'password1', 'password2')

        def save(self, commit=True):
            user = super().save(commit=False)
            user.is_doctor = True
            if commit:
                user.save()
                DoctorProfile.objects.create(user=user, specialty=self.cleaned_data['specialty'])
            return user
        
class PatientRegistrationForm(UserCreationForm):
    age = forms.IntegerField()

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'age', 'password1', 'password2')

        def save(self, commit=True):
            user = super().save(commit=False)
            user.is_patient = True
            if commit:
                user.save()
                PatientProfile.objects.create(user=user, age=self.cleaned_data['age'])
            return user