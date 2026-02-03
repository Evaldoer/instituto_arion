from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MensagemContato

def home(request):
    return render(request, "instituto/index.html")

def quem_somos(request):
    return render(request, "instituto/quem_somos.html")

def missao(request):
    return render(request, "instituto/missao.html")

def projetos(request):
    return render(request, "instituto/projetos.html")

def ajuda(request):
    return render(request, "instituto/ajuda.html")

def contato(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        mensagem = request.POST.get("mensagem")

        # Salva no banco
        MensagemContato.objects.create(
            nome=nome,
            email=email,
            mensagem=mensagem
        )

        messages.success(request, f"Obrigado {nome}, sua mensagem foi enviada com sucesso!")
        return redirect("instituto:contato")

    return render(request, "instituto/contato.html")