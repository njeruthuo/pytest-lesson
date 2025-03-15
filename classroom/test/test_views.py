import json
import pytest
from django.urls import reverse

from ..models import Student


@pytest.mark.django_db
def test_student_api_get(client, create_student):
    response = client.get(reverse("student_api_view"))
    assert response.status_code == 200

    students = list(Student.objects.all())

    assert len(students) == len(response.data)


@pytest.mark.django_db
def test_student_api_post(client, create_student):
    payload = {
        'first_name': 'Oliver',
        'last_name': 'Karenge',
        'reg_number': 667,
        'is_qualified': True,
        'average_score': 65.5
    }

    response = client.post(reverse("student_api_view"),
                           data=json.dumps(payload),
                           content_type="application/json"
                           )
    assert response.status_code == 201

    assert response.json()['first_name'] == 'Oliver'


@pytest.mark.django_db
def test_student_api_put(client, create_student):
    payload = {
        'first_name': 'Oliver',
        'last_name': 'Karenge',
        'reg_number': 667,
        'is_qualified': True,
        'average_score': 65.5
    }

    response = client.put(reverse("student_api_view", kwargs={'reg_number': create_student.reg_number}),
                          data=json.dumps(payload),
                          content_type="application/json")

    assert response.json()['first_name'] == "Oliver"

    assert response.status_code == 202


@pytest.mark.django_db
def test_student_api_delete(client, create_student):
    response = client.delete(reverse("student_api_view", kwargs={
                             'reg_number': create_student.reg_number}))

    student = list(Student.objects.all())

    assert student == []

    assert response.json()['SUCCESS'] == 'DELETION SUCCESS'

    response1 = client.delete(reverse("student_api_view"))

    assert response1.json()['ERROR'] == "DELETION FAILED"

    assert response1.status_code == 400
