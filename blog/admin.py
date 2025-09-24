from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "tag", "date")   # colunas na listagem
    list_filter = ("tag", "author", "date")             # filtros na lateral
    search_fields = ("title", "content", "author")      # barra de pesquisa
    prepopulated_fields = {"slug": ("title",)}          # slug automático
    date_hierarchy = "date"                             # navegação por data
    ordering = ("-date",)                               # ordenação padrão
