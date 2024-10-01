from django.shortcuts import render

# Create your views here.

def registrations(request):
    return render(request, 'users/registrations.html')