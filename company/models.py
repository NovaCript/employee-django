from django.db import models

# Create your models here.


class Branch(models.Model):
    address = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)

    def __str__(self):
        return self.short_name


class Department(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    floor = models.IntegerField(null=False, blank=False)
    branch = models.ForeignKey('company.Branch', null=True, blank=True, related_name='departments', on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Employee(models.Model):
    full_name = models.CharField(max_length=100, null=False, blank=False)
    should = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=100, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    department = models.ForeignKey('company.Department', null=True, blank=True, related_name='employees', on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name