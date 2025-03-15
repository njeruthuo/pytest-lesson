from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import StudentSerializer, Student, Classroom


class StudentAPIView(APIView):
    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        serialier_data = StudentSerializer(students, many=True).data
        return Response(serialier_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        reg = kwargs.get('reg_number')

        if reg:
            instance = Student.objects.get(reg_number=reg)

            serializer = StudentSerializer(
                data=request.data, instance=instance)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response({'ERROR': 'UPDATE FAILED'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        reg = kwargs.get('reg_number')

        if reg:
            instance = Student.objects.get(reg_number=reg)

            instance.delete()

            return Response({'SUCCESS': 'DELETION SUCCESS'}, status=status.HTTP_200_OK)
        return Response({'ERROR': 'DELETION FAILED'}, status=status.HTTP_400_BAD_REQUEST)


student_api_view = StudentAPIView.as_view()
