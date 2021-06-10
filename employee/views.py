from django.shortcuts import render
from employee.serializers import EmployeeSerializer
from employee.models import Employee
from rest_framework import viewsets
# Create your views here.
class EmployeeListViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class= EmployeeSerializer