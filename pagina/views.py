from django.shortcuts import render
from .models import Informacoes, Planos, Avaliacoes, SiteConfiguration

def home(request):
    # Pega a primeira configuração de contatos/rodapé
    site_config = Informacoes.objects.first()

    # Pega a configuração geral do site (singleton)
    site_configuration = SiteConfiguration.objects.first()

    # Todos os planos disponíveis
    planos = Planos.objects.all()

    # Todos os depoimentos cadastrados, ordenados do mais recente para o mais antigo
    depoimentos = Avaliacoes.objects.all().order_by('-create_at')

    # Monta o contexto que será enviado para o template
    context = {
        'info': site_config,             # Configurações de contato
        'site_config': site_configuration,  # Configurações gerais (sobre nós, redes, etc.)
        'planos': planos,            
        'depoimentos': depoimentos,  
    }

    # Renderiza a página 'index.html' com o contexto
    return render(request, 'index.html', context)
