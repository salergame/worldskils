# hospital/models.py

from django.db import models
from users.models import Patient, InsuranceCompany, Technician, Accountant

class LabService(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    code = models.CharField(max_length=100, unique=True)
    execution_time = models.PositiveIntegerField() 
    average_deviation = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    services = models.ManyToManyField(LabService, through='ProvidedService')
    status = models.CharField(max_length=100) 
    execution_time = models.PositiveIntegerField() 
    def __str__(self):
        return f"Order {self.id} for {self.patient}"


class ProvidedService(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    service = models.ForeignKey(LabService, on_delete=models.CASCADE)
    executed_at = models.DateTimeField(null=True, blank=True)
    executed_by = models.ForeignKey(Technician, on_delete=models.SET_NULL, null=True)
    analyzer = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.service} in Order {self.order.id}"


class AnalyzerWork(models.Model):
    provided_service = models.ForeignKey(ProvidedService, on_delete=models.CASCADE)
    order_received_at = models.DateTimeField()
    execution_time_seconds = models.PositiveIntegerField()

    def __str__(self):
        return self.pk


class ArchiveModel(models.Model):
    archived_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    class Meta:
        abstract = True
