from rest_framework import serializers
from .models import PatientDoctorMapping
from doctors.models import Doctor

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(source="doctor.name", read_only=True)
    patient_name = serializers.CharField(source="patient.name", read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'patient_name', 'doctor', 'doctor_name', 'created_at']
