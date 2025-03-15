import pytest

from ..models import Classroom, Student

@pytest.fixture
def create_student(db):
    return Student.objects.create(
        first_name="Julius", last_name="Njeru", reg_number=668, is_qualified=True, average_score=61)


@pytest.fixture
def create_classroom(db):
    return Classroom.objects.create(
        name='Form 3',
        student_capacity=200
    )
