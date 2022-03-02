from itertools import product
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Patients
from .serializers import PatientSerializer


class PatientViewSet(viewsets.ViewSet):
    def __get_patient(self, pk=None):
        try:
            patient = Patients.objects.get(id=pk)
        except Patients.DoesNotExist:
            patient = None
        return patient

    def list(self, request):
        patients = Patients.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrive(self, request, pk=None):
        patient = self.__get_patient(pk)
        if patient is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def update(self, request, pk=None):
        patient = self.__get_patient(pk)
        if patient is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSerializer(data=request.data, instance=patient)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        patient = self.__get_patient(pk)
        if patient is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
