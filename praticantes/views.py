from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Praticante
from voluntarios.models import Voluntario

def lista_praticantes(request):
    praticantes = Praticante.objects.all()
    return render(request, "praticantes/lista_praticantes.html", {
        "praticantes": praticantes
    })

def praticante(request):
    if request.method == "POST":
        voluntario_id = request.POST.get("voluntario")
        voluntario = Voluntario.objects.get(id=voluntario_id) if voluntario_id else None

        Praticante.objects.create(
            nome=request.POST["nome"],
            responsavel=request.POST["responsavel"],
            telefone=request.POST["telefone"],
            voluntario=voluntario,
            status=request.POST.get("status", "fila")
        )
        messages.success(request, "Praticante cadastrado com sucesso!")
        return redirect("praticantes:lista")

    voluntarios = Voluntario.objects.all()
    return render(request, "praticantes/praticante.html", {
        "voluntarios": voluntarios
    })