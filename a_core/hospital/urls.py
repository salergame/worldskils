from django.urls import path
from .views import *

app_name = "hospital"

urlpatterns = [
    path("", view_hospital, name="index"),
]
