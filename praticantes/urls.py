from django.urls import path
from . import views

app_name = "praticantes"

urlpatterns = [
    path("", views.lista_praticantes, name="lista"),
    path("novo/", views.praticante, name="novo"),
]