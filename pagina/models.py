from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser, Group, Permission
import phonenumbers
class Informacoes(models.Model):
    rua_bairro = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=255, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)

    def telefone_formatado(self):
        try:
            numero = phonenumbers.parse(self.telefone, None)  # None aceita qualquer país
            return phonenumbers.format_number(numero, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        except phonenumbers.NumberParseException:
            return self.telefone

    def save(self, *args, **kwargs):
        if not self.pk:  # só força pk=1 se ainda não existe
            self.pk = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return "Configuração do Rodapé"
    
class SiteConfiguration(models.Model):
    # --- Navbar Links ---
    navbar_home_link = models.CharField(max_length=200, blank=True, null=True, default="/home")
    navbar_noticias_link = models.CharField(max_length=200, blank=True, null=True, default="/noticias")
    navbar_blog_link = models.CharField(max_length=200, blank=True, null=True, default="/blog")
    navbar_sobre_link = models.CharField(max_length=200, blank=True, null=True, default="/sobre")
    navbar_testar_link = models.CharField(max_length=200, blank=True, null=True, default="/testar")

    # --- Seção: Preço --- (Agora vem antes do Sobre Nós)
    preco_titulo = models.CharField(max_length=255, blank=True, null=True)
    preco_valor = models.CharField(max_length=50, blank=True, null=True)
    preco_disclaimer = models.CharField(max_length=255, blank=True, null=True)
    preco_botao_texto = models.CharField(max_length=50, blank=True, null=True)
    preco_botao_link = models.URLField(blank=True, null=True)

    # --- Seção: Sobre Nós ---
    sobre_nome = models.CharField(max_length=255, blank=True, null=True)
    sobre_cargo = models.CharField(max_length=255, blank=True, null=True)
    sobre_texto = models.TextField(blank=True, null=True)
    sobre_imagem = models.ImageField(upload_to="quem_somos/", blank=True, null=True)

    # --- Benefícios ---
    beneficios_parte1 = models.CharField(max_length=255, blank=True, null=True, default="Benefícios")
    beneficios_parte2 = models.CharField(max_length=255, blank=True, null=True, default="do nosso plano")
    beneficios_parte3 = models.CharField(max_length=255, blank=True, null=True, default="Angelical")




    def save(self, *args, **kwargs):
        if not self.pk:  # garante singleton
            self.pk = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return "Configuração do Site"


class Beneficio(models.Model):
    site = models.ForeignKey(
        SiteConfiguration,
        on_delete=models.CASCADE,
        related_name="beneficios"
    )
    titulo = models.CharField(max_length=255)
    texto = models.TextField()
    imagem = models.ImageField(upload_to="beneficios/", blank=True, null=True)
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["ordem"]

    def __str__(self):
        return self.titulo


class Hero(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255, null=True, blank=True)
    cta_texto = models.CharField(max_length=50, default="TESTAR GRÁTIS")
    cta_link = models.URLField(null=True, blank=True)

class Usuario(AbstractUser):
    nome_completo = models.CharField(max_length=255)
    perfil = models.CharField(
        max_length=20,
        choices=[('admin', 'Admin'), ('leitor', 'Leitor')],
        default='leitor'
    )
    data_de_registro = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(
        Group,
        related_name="usuarios_custom",
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="usuarios_custom_permissions",
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
    def __str__ (self):
        return self.username

class Planos(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    beneficios = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="pasta_pl")
    destaque = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['preco']  


class UsuarioPlano(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='planos_associados')
    plano = models.ForeignKey(Planos, on_delete=models.CASCADE, related_name='usuarios_associados')
    data_inicio = models.DateTimeField(auto_now_add=True)
    data_fim = models.DateTimeField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.plano.titulo}'
    
class Noticias(models.Model):
    TIPOSMODAL = [
        ('autoopen', 'Abrir automático'),
        ('update_notification', 'Notificação Atualizada'),
    ]
    titulo = models.CharField(max_length=255)
    sumario = models.TextField()
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to="noticias/", max_length= 255, null=True, blank=True)
    data_publicacao = models.DateTimeField()
    destaque = models.BooleanField(default=False)
    categoria = models.CharField(max_length=100)
    criado_por = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='noticias')
    tipo_modal = models.CharField(max_length=30, choices=TIPOSMODAL, null=True, blank=True)
    ordem = models.PositiveIntegerField(default=0)
    link_externo = models.URLField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
    
class TipoMidia(models.TextChoices):
    VIDEO = 'video', 'video'
    FOTO = 'foto','foto'

class MidiaSobreNos(models.Model):
    titulo = models.CharField(max_length=255, verbose_name='Título')
    descricao = models.TextField(verbose_name='Descrição')
    tipo_midia = models.CharField(
        max_length = 20,
        choices=TipoMidia.choices,
        verbose_name = 'Tipo de Mídia'
    )
    midia_url = models.CharField(max_length=255, verbose_name="URL da mídia")
    data_publicacao = models.DateTimeField(verbose_name="Data de publicação")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titulo} ({self.tipo_midia})"
    
class Avaliacoes(models.Model):
    nome = models.CharField(max_length=255)
    texto_avaliacao=models.TextField()
    imagem = models.ImageField(upload_to="pasta_av")
    create_at = models.DateTimeField(auto_now_add=True)  #Criando em:
    updated_at = models.DateTimeField(auto_now=True) #Data de modificação