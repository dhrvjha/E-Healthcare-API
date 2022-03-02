from venv import create
from django.urls import resolve, reverse
from patients.models import Patients
from rest_framework import status
import pytest


@pytest.mark.django_db
@pytest.mark.parametrize("param", ["patients-CR"])
def test_patient_list(client, param):
    url = reverse(param)
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_patient_create(client, user_data):
    assert Patients.objects.count() == 0
    url = reverse("patients-CR")
    response = client.post(url, user_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert user_data["first_name"] in str(response.content)
    assert Patients.objects.count() == 1


@pytest.mark.django_db
def test_patient_retrive(client, create_test_user):
    url = reverse("patients-RUD", args=[create_test_user.id])
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert str(create_test_user.id) in str(response.content)


@pytest.mark.django_db
def test_patients_update(client, create_test_user, user_data):
    url = reverse("patients-RUD", args=[create_test_user.id])
    user_data["id"] = str(create_test_user.id)
    user_data["first_name"] = "Rohit"
    response = client.put(url, data=user_data, content_type="application/json")
    assert response.status_code == status.HTTP_202_ACCEPTED
    assert (
        user_data["first_name"]
        == Patients.objects.get(id=create_test_user.id).first_name
    )

@pytest.mark.django_db
def test_patients_destroy(client, create_test_user):
    numberOfUsers = Patients.objects.count()
    url = reverse('patients-RUD', args=[create_test_user.id])
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert numberOfUsers-1 == Patients.objects.count()