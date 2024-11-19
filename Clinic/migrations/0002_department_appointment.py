# Generated by Django 5.0.6 on 2024-11-19 09:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clinic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PhoneNumber', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('Department', models.CharField(max_length=100)),
                ('Reason', models.TextField()),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clinic.doctorprofile')),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clinic.patientprofile')),
            ],
        ),
    ]
