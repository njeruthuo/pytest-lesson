import pytest
from ..models import Classroom, Student

@pytest.mark.django_db
def test_student_created(create_student):
    student = Student.objects.first()
    assert student.first_name == "Julius"
    assert student.last_name == "Njeru"
    assert student.is_qualified == True


@pytest.mark.django_db
def test_student_update(create_student):
    Student.objects.update(first_name="Halx")

    student = Student.objects.first()

    assert student.first_name == "Halx"


@pytest.mark.django_db
def test_student_delete(create_student):
    Student.objects.get(first_name="Julius").delete()

    student_list = list(Student.objects.all())

    assert len(student_list) == 0


@pytest.mark.django_db
def test_get_student_and_classroom(create_student, create_classroom):
    student = Student.objects.first()
    classroom = Classroom.objects.first()

    assert student.first_name == "Julius"
    assert classroom.name == 'Form 3'


@pytest.mark.django_db
def test_add_students_to_classroom(create_classroom, create_student):
    classroom = Classroom.objects.get(name="Form 3")
    student1 = Student.objects.get(first_name="Julius")
    student2 = Student.objects.create(
        first_name="Halx", last_name="Kinuthia", reg_number=2334, is_qualified=True, average_score=65)

    classroom.students.add(student1, student2)

    assert len(list(classroom.students.all())) == 2

    classroom.students.remove(student2)

    assert len(list(classroom.students.all())) == 1


@pytest.mark.django_db
def test_update_classroom(create_classroom):
    classroom = Classroom.objects.get(name="Form 3")

    classroom.student_capacity = 100

    assert classroom.student_capacity == 100
