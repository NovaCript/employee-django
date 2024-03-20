from django.core.management.base import BaseCommand
from faker import Faker
import random
from company.models import Employee, Department

class Command(BaseCommand):
    help = 'Generate employees'

    def handle(self, *args, **kwargs):
        fake = Faker()

        departments = Department.objects.all()

        for department in departments:
            num_employees = random.randint(1, 30)
            for _ in range(num_employees):
                Employee.objects.create(
                    full_name=fake.name(),
                    should=fake.job(),
                    phone=fake.phone_number(),
                    date_of_birth=fake.date_of_birth(),
                    email=fake.email(),
                    department=department
                )

        self.stdout.write(self.style.SUCCESS('Successfully generated employees'))