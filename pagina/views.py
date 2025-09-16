from django.shortcuts import render
from .models import Informacoes, Planos, Avaliacoes

def home(request):
    # Pega a primeira configuração do site (supondo que só exista uma)
    site_config = Informacoes.objects.first()

    # Todos os planos disponíveis
    planos = Planos.objects.all()

    # Todos os depoimentos cadastrados, ordenados do mais recente para o mais antigo
    depoimentos = Avaliacoes.objects.all().order_by('-create_at')

    # Monta o contexto que será enviado para o template
    context = {
        'info': site_config,   # <-- aqui passamos o registro correto
        'planos': planos,            
        'depoimentos': depoimentos,  
    }

    # Renderiza a página 'index.html' com o contexto
    return render(request, 'index.html', context)
