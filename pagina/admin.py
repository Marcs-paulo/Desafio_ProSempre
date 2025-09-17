from django.contrib import admin
from .models import Informacoes, Usuario, Planos, UsuarioPlano, Noticias, MidiaSobreNos, Avaliacoes, SiteConfiguration,Beneficio

class BeneficioInline(admin.StackedInline):
    model = Beneficio
    extra = 0
    can_delete = True  # habilita remoção
    verbose_name = "Benefício"
    verbose_name_plural = "Benefícios"
@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    fieldsets = (
        ("🔗 Navbar Links", {
            "fields": ("navbar_home_link", "navbar_noticias_link", "navbar_blog_link", "navbar_sobre_link", "navbar_testar_link")
        }),
        ("💰 Seção de Preço", {
            "fields": ("preco_titulo", "preco_valor", "preco_disclaimer", "preco_botao_texto", "preco_botao_link")
        }),
("🎯 Benefícios", {
    "fields": ("beneficios_parte1", "beneficios_parte2", "beneficios_parte3"),
}),

        ("ℹ️ Sobre Nós", {
            "fields": ("sobre_nome", "sobre_cargo", "sobre_texto", "sobre_imagem")
        }),
    )
    inlines = [BeneficioInline]
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'nome_completo', 'email', 'perfil', 'data_de_registro', 'last_login')
    search_fields = ('username', 'email', 'nome_completo')
    list_filter = ('perfil',)
    readonly_fields = ('data_de_registro', 'last_login')

@admin.register(Planos)
class PlanosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'preco', 'destaque')
    search_fields = ('titulo',)
    list_filter = ('destaque',)
    readonly_fields = ('criado_em', 'atualizado_em')
    ordering = ('preco',)

@admin.register(UsuarioPlano)
class UsuarioPlanoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'plano', 'data_inicio', 'data_fim')
    search_fields = ('usuario__username', 'plano__titulo')
    list_filter = ('plano',)
    readonly_fields = ('data_inicio', 'criado_em', 'atualizado_em') 

@admin.register(Informacoes)
class InformacoesAdmin(admin.ModelAdmin):
    list_display = ('rua_bairro', 'cidade', 'telefone', 'email', 'instagram', 'facebook', 'youtube')
    
    def has_add_permission(self, request):
        # Só permite adicionar se ainda não existir nenhum registro
        return not Informacoes.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Não permite deletar
        return False

@admin.register(Noticias)
class NoticiasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao', 'destaque', 'categoria', 'criado_por', 'tipo_modal')
    search_fields = ('titulo', 'sumario', 'conteudo', 'categoria', 'criado_por__nome_completo')
    list_filter = ('destaque', 'categoria', 'tipo_modal', 'data_publicacao')
    readonly_fields = ('criado_em', 'atualizado_em') 
    date_hierarchy = 'data_publicacao'

@admin.register(MidiaSobreNos)
class MidiaSobreNosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo_midia', 'data_publicacao')
    list_filter = ('tipo_midia', 'data_publicacao')
    search_fields = ('titulo', 'descricao')
    ordering = ('-data_publicacao',)
@admin.register(Avaliacoes)
class AvaliacoesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'create_at', 'updated_at')
    search_fields = ('nome', 'texto_avaliacao')
    readonly_fields = ('create_at', 'updated_at')
    ordering = ('-create_at',)

