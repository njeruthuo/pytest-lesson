from django.urls import path
from .views import student_api_view


urlpatterns = [
    path('student_api_view/', student_api_view, name='student_api_view'),
    path('students/<int:reg_number>/', student_api_view, name='student_api_view'),
]
