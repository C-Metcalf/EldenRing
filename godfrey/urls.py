from django.urls import path
from . import views


app_name = "godfrey"

urlpatterns = [
    path("", views.index, name="index"),
    path("Godfrey/", views.godfrey, name="godfrey"),
]