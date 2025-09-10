from django.contrib import admin
from .models import SiteConfiguration, Usuario, Planos, Usuario_plano

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome_de_usuario', 'nome_completo', 'email', 'perfil', 'data_de_registro', 'ultimo_login')
    search_fields = ('nome_de_usuario', 'email', 'nome_completo')
    list_filter = ('perfil',)

@admin.register(Planos)
class PlanosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'preco', 'criado_em', 'atualizado_em')
    search_fields = ('titulo', 'tipo')

@admin.register(Usuario_plano)
class UsuarioPlanoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'planos', 'data_inicio', 'end_date', 'criado_em', 'atualizado_em')
    search_fields = ('usuario__nome_de_usuario', 'planos__titulo')
    list_filter = ('planos',)

@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ('endereco', 'telefone', 'email', 'instagram', 'facebook', 'youtube')

    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj = None):
        return False