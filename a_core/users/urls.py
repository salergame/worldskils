from django.urls import path
from .views import *

app_name = "users"

urlpatterns = [
    path("registrations/", register, name="index"),
    path("login/",login, name="login"),
]