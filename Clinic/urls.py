from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register_doctor/', views.register_doctor, name='register_doctor'),
    path('register_patient/', views.register_patient, name='register_patient'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('about/', views.about, name='about'),
    path('doctors/', views.doctors_list, name='doctors'),
    path('departments/', views.departments_list, name='departments'),
    path('appointment/', views.appointment, name='appointment'),
    path('join_room/', views.join_room, name='join_room'),
    path('video_conference/', views.video_conference, name='video_conference'),
    path('meeting/', views.meeting, name='meeting'),
    path('contact/', views.contact, name='contact'),
]