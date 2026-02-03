from django.urls import path
from . import views

app_name = "instituto"

urlpatterns = [
    path("", views.home, name="home"),
    path("quem-somos/", views.quem_somos, name="quem_somos"),
    path("missao/", views.missao, name="missao"),
    path("projetos/", views.projetos, name="projetos"),
    path("ajuda/", views.ajuda, name="ajuda"),
    path("contato/", views.contato, name="contato"),
]