from django.shortcuts import render
from .models import SiteConfiguration, Planos # importar os models

def home(request):
    site_config = SiteConfiguration.objects.first()
    planos = Planos.objects.all()
  # ou filter alguma condição

    context = {
        'site_config': site_config,
        'planos': planos,

    }
    return render(request, 'index.html', context)
