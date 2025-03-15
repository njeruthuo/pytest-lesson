import pytest

from ..serializers import StudentSerializer, Student


@pytest.mark.django_db
def test_student_serializer_output(create_student):
    student = Student.objects.get(first_name="Julius")

    serializer = StudentSerializer(student)

    expected_data = {
        'first_name': "Julius", 'last_name': "Njeru", 'reg_number': 668, 'is_qualified': True, 'average_score': 61
    }

    assert serializer.data == expected_data


@pytest.mark.django_db
def test_student_serializer_input_valid_data(create_student):
    payload = {
        'first_name': 'Oliver',
        'last_name': 'Karenge',
        'reg_number': 667,
        'is_qualified': True,
        'average_score': 65.5
    }

    serializer = StudentSerializer(data=payload)

    assert serializer.is_valid()

    assert serializer.validated_data['first_name'] == "Oliver"
