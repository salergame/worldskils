from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Patient)
admin.site.register(InsuranceCompany)
admin.site.register(Technician)
admin.site.register(Accountant)