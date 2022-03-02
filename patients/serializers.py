from rest_framework import serializers
from .models import Patients, Appointments


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = "__all__"
