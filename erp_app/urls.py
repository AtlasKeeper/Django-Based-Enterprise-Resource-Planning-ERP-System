from django.urls import path
from .views import employee_list, employee_detail, department_list, department_detail, welcome

urlpatterns = [
    path('employees/', employee_list, name='employee_list'),
    path('employees/<int:pk>/', employee_detail, name='employee_detail'),
    path('departments/', department_list, name='department_list'),
    path('departments/<int:pk>/', department_detail, name='department_detail'),
    path('welcome/', welcome, name='welcome'), 
]
