from itertools import product
from django.urls import path
from .views import PatientViewSet


urlpatterns = [
    path(
        "",
        PatientViewSet.as_view({"get": "list", "post": "create"}),
        name="patients-CR",
    ),
    path(
        "<uuid:pk>/",
        PatientViewSet.as_view(
            {"get": "retrive", "put": "update", "delete": "destroy"}
        ),
        name="patients-RUD",
    ),
]
