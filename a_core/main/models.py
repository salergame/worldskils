from django.db import models

# Create your models here.
class Labservices(models.Model):
    name = models.CharField(max_length=100)
    cost = models.PositiveIntegerField()
    service_code = models.CharField(max_length=100)
    deadline = models.DateField()
    average_deviation = models.FloatField()
    
    def __str__(self):
        return self.service_code

