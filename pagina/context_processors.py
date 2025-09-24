# context_processors.py
from .models import SiteConfiguration, Informacoes

def site_config(request):
    site_config = SiteConfiguration.objects.first()  # pega a configuração do site
    informacoes = Informacoes.objects.first()       # pega as informações do rodapé
    return {
        'site_config': site_config,
        'informacoes': informacoes
    }
