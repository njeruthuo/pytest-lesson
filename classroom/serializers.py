from rest_framework import serializers
from .models import Classroom, Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields = ["first_name", "last_name",
                  "reg_number", "is_qualified", "average_score"]
