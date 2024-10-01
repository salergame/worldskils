# users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ('patient', 'Пациент'),
        ('technician', 'Лаборант'),
        ('accountant', 'Бухгалтер'),
        ('admin', 'Администратор'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    passport_series = models.CharField(max_length=10)
    passport_number = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    insurance_number = models.CharField(max_length=50)
    insurance_type = models.CharField(max_length=100)
    insurance_company = models.ForeignKey('InsuranceCompany', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class InsuranceCompany(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    inn = models.CharField(max_length=12)
    bank_account = models.CharField(max_length=20)
    bic = models.CharField(max_length=9)

    def __str__(self):
        return self.name


class Technician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    last_login = models.DateTimeField(null=True, blank=True)
    services = models.ManyToManyField('hospital.LabService')

    def __str__(self):
        return self.full_name


class Accountant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    last_login = models.DateTimeField(null=True, blank=True)
    billed_services = models.ManyToManyField('hospital.LabService')

    def __str__(self):
        return self.full_name
