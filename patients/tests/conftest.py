import pytest
from patients.models import Patients


@pytest.fixture
def user_data() -> dict:
    content = {"first_name": "Dhruv", "last_name": "Jha", "age": "24"}
    return content


@pytest.fixture
def create_test_user(user_data) -> Patients:
    test_user = Patients(
        first_name=user_data["first_name"],
        last_name=user_data["last_name"],
        age=user_data["age"],
    )
    test_user.save()
    return test_user


@pytest.fixture
def update_user_data() -> dict:
    content = {
        "first_name": "Rohit",
        "last_name": "Ranjan",
        "age": 14,
    }
    return content
