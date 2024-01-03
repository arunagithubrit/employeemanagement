from django.urls import path
from employee_api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("employee",views.EmployeeView,basename="employee")

urlpatterns=[
     path('register/',views.UserCreationView.as_view()),
]+router.urls