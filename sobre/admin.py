# sobre/admin.py
from django.contrib import admin
from .models import CardsHistoria, Valores, Membros

admin.site.register(CardsHistoria)
admin.site.register(Valores)
admin.site.register(Membros)
