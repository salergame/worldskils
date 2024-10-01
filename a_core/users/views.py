from django.shortcuts import render,redirect
from .forms import *
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('main:index')  
    else:
        form = RegistrationForm()

    return render(request, 'users/registration.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('main:index')  
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})