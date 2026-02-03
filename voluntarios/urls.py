from django.urls import path
from . import views

app_name = "voluntarios"

urlpatterns = [
    path("", views.lista_voluntarios, name="lista"),
    path("novo/", views.voluntario, name="novo"),
]