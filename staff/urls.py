from django.urls import path
from .views import StaffViewSet


urlpatterns = [
    path("", StaffViewSet.as_view({"get": "list", "post": "create"}), name="staff-CR"),
    path(
        "<int:pk>/",
        StaffViewSet.as_view({"get": "retirve", "put": "update", "delete": "destroy"}),
        name="staff-RUD",
    ),
]
