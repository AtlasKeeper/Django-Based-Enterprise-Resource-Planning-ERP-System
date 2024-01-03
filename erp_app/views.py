from django.shortcuts import render, get_object_or_404
from .models import Employee, Department
from django.shortcuts import render

def welcome(request):
    return render(request, 'erp_app/welcome.html')

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'erp_app/employee_list.html', {'employees': employees})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'erp_app/employee_detail.html', {'employee': employee})

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'erp_app/department_list.html', {'departments': departments})

def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'erp_app/department_detail.html', {'department': department})
