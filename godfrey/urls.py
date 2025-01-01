from django.urls import path
from . import views

app_name = 'godfry'
urlpatterns = [
    path('', views.index, name='index')
]