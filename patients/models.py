from django.db import models
from staff.models import Staff
import uuid

# Create your models here.


class Patients(models.Model):
    # TODO: Complete all the fields for patients
    id = models.UUIDField(
        default=uuid.uuid4, blank=True, null=False, primary_key=True, db_index=True
    )
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    age = models.PositiveIntegerField(blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Appointments(models.Model):
    # TODO: all apointments after delete date should delete
    patient = models.ForeignKey(Patients, on_delete=models.DO_NOTHING)
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
