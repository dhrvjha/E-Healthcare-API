
from rest_framework import viewsets, status
from rest_framework.response import Response
from staff.models import Staff
from .serializer import StaffSerializer


class StaffViewSet(viewsets.ViewSet):
    def __get_staff(self, pk=None):
        try:
            staff = Staff.objects.get(id=pk)
        except Staff.DoesNotExist:
            staff = None
        return staff

    def list(self, request):
        staff = Staff.objects.all()
        serailzer = StaffSerializer(staff)
        return Response(serailzer.data)

    def create(self, request):
        serializer = StaffSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def retrive(self, request, pk=None):
        staff = self.__get_staff(pk)
        if staff is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StaffSerializer(instance=staff)
        return Response(serializer.data)

    def update(self, request, pk=None):
        staff = self.__get_staff(pk)
        if staff is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StaffSerializer(instance=staff, data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


    def destroy(self, request, pk=None):
        staff = self.__get_staff(pk)
        if staff is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
