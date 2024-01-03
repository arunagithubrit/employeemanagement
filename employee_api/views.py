from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.response import Response
from employee_api.serializers import UserSerializer,EmployeeSerializer
from rest_framework import authentication
from rest_framework import permissions
from employee.models import Employee
# Create your views here.

class UserCreationView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        


class EmployeeView(ModelViewSet):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()
    