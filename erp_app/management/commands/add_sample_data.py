from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, User, Permission
from erp_app.models import Department, Employee
import random

class Command(BaseCommand):
    help = 'Add sample data to the ERP system'

    def handle(self, *args, **kwargs):
        # Create groups if they don't exist
        manager_group, created = Group.objects.get_or_create(name='Managers')
        developer_group, created = Group.objects.get_or_create(name='Developers')
        hr_group, created = Group.objects.get_or_create(name='HR')
        sales_group, created = Group.objects.get_or_create(name='Sales')
        finance_group, created = Group.objects.get_or_create(name='Finance')

        self.stdout.write(self.style.SUCCESS('Successfully created groups'))

        # Assign permissions to groups
        manager_group.permissions.add(
            Permission.objects.get(codename='add_employee'),
            Permission.objects.get(codename='change_employee'),
            Permission.objects.get(codename='view_employee')
        )
        developer_group.permissions.add(
            Permission.objects.get(codename='view_employee')
        )
        hr_group.permissions.add(
            Permission.objects.get(codename='add_employee'),
            Permission.objects.get(codename='view_employee')
        )
        sales_group.permissions.add(
            Permission.objects.get(codename='view_employee')
        )
        finance_group.permissions.add(
            Permission.objects.get(codename='view_employee')
        )

        self.stdout.write(self.style.SUCCESS('Successfully assigned permissions to groups'))

        # Create 1000 users with different names and associate them with groups
        for i in range(1, 1001):
            username = f'user{i}'
            password = f'password{i}'
            first_name = f'User{i}'
            last_name = f'LastName{i}'

            user = User.objects.create_user(username, password=password, first_name=first_name, last_name=last_name)
            # Associate users with random groups
            if i % 5 == 0:
                user.groups.add(manager_group)
            elif i % 5 == 1:
                user.groups.add(developer_group)
            elif i % 5 == 2:
                user.groups.add(hr_group)
            elif i % 5 == 3:
                user.groups.add(sales_group)
            else:
                user.groups.add(finance_group)

            self.stdout.write(self.style.SUCCESS(f'Successfully created user: {username}'))

        self.stdout.write(self.style.SUCCESS('Successfully created users'))

        # Create 15 departments
        for i in range(1, 16):
            name = f'Department{i}'
            description = f'Description for Department{i}'
            Department.objects.create(name=name, description=description)

        self.stdout.write(self.style.SUCCESS('Successfully created departments'))

        # Create 500 employees and associate them with departments
        for i in range(1, 501):
            name = f'Employee{i}'
            email = f'employee{i}@example.com'
            department = Department.objects.get(pk=random.randint(1, 15))
            Employee.objects.create(name=name, email=email, department=department)

        self.stdout.write(self.style.SUCCESS('Successfully created employees'))

        self.stdout.write(self.style.SUCCESS('Sample data added successfully!'))
