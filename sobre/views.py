# sobre/views.py
from django.shortcuts import render
from .models import CardsHistoria, Valores, Membros

def sobre_view(request):
    history_cards = CardsHistoria.objects.all()
    values = Valores.objects.all()
    team_members = Membros.objects.all()
    return render(request, 'sobre-nos.html', {
        'history_cards': history_cards,
        'values': values,
        'team_members': team_members,
    })
