from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Voluntario
from praticantes.models import Praticante  # para calcular participação


# Create your views here.

def lista_voluntarios(request):
    voluntarios = Voluntario.objects.all()
    total_praticantes = Praticante.objects.count() or 1

    voluntarios_info = []
    for v in voluntarios:
        atendidos = v.praticantes.count()
        participacao = round((atendidos / total_praticantes) * 100, 1)
        voluntarios_info.append({
            "nome": v.nome,
            "email": v.email,
            "area": v.area,
            "atendidos": atendidos,
            "participacao": participacao,
        })

    return render(request, "voluntarios/lista_voluntarios.html", {
        "voluntarios": voluntarios_info
    })

def voluntario(request):
    if request.method == "POST":
        Voluntario.objects.create(
            nome=request.POST["nome"],
            email=request.POST["email"],
            area=request.POST["area"]
        )
        messages.success(request, "Cadastro realizado com sucesso! Obrigado por se voluntariar 💙")
        return redirect("instituto:home")

    return render(request, "voluntarios/voluntario.html")
