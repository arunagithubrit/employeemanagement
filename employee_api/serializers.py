from rest_framework import serializers
from employee.models import User,Employee

class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["id","username","email","password","phone","address"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class EmployeeSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Employee
        fields="__all__"

