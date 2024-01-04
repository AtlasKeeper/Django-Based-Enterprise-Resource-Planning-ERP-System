from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, User, Permission
from erp_app.models import Department, Employee

class Command(BaseCommand):
    help = 'Reset ERP system by deleting all groups and users'

    def handle(self, *args, **kwargs):
        # Delete all groups
        Group.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all groups'))

        # Delete all users
        User.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all users'))
