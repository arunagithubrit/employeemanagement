from django import forms
# from django.contrib.auth.forms import UserCreationForm
from employee.models import User,Employee

class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "salary":forms.NumberInput(attrs={"class":"form-control"}),
            "department":forms.TextInput(attrs={"class":"form-control"}),
            
        }


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password","phone","address"]

        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
            "phone":forms.NumberInput(attrs={"class":"form-control"}),
            "address":forms.TextInput(attrs={"class":"form-control"}),
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

        # fields=["name","email","phone","address","gender"]


