from django.shortcuts import render

# Create your views here.

def view_hospital(request):
    return render(request, 'hospital/hospital.html')