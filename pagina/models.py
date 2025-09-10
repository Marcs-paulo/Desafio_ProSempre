from django.db import models
from django.contrib.auth.hashers import make_password, check_password
# só para teste

class SiteConfiguration(models.Model):
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    instagram = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SiteConfiguration, self).save(*args, **kwargs)
    def __str__(self):
        return "Configuração do Site"
    
class Usuario(models.Model):
    nome_de_usuario = models.CharField(max_length= 150, unique=True)
    nome_completo = models.CharField(max_length= 255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length= 128)
    perfil  = models.CharField(
        max_length= 20,
        choices = [
            ('admin', 'Admin'),
            ('leitor', 'Leitor'),
        ],
        default= 'leitor'
    )
    data_de_registro = models.DateTimeField(auto_now_add=True)
    ultimo_login = models.DateTimeField(null=True, blank=True)

    def set_senha(self, senha_bruta):
        self.senha = make_password(senha_bruta)
        self.save()
    
    def check_senha (self, senha_bruta):
        return check_password(senha_bruta, self.senha)
    
    def __str__ (self):
        return self.nome_de_usuario

class Planos(models.Model):
    tipos_de_planos = [
        ('gratis', 'gratuito'),
        ('duo', 'Duo'),
        ('angelical', 'Angelical'),
    ]
    titulo = models.CharField(max_length=100)
    descrição = models.TextField()
    beneficios = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=20, choices=tipos_de_planos)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__ (self):
        return self.titulo
    
class Usuario_plano(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='subscription')
    planos = models.ForeignKey(Planos, on_delete=models.CASCADE, related_name='subscription')
    data_inicio = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.usuario.nome_de_usuario} - {self.planos.titulo}'
    
class Noticias(models.Model):
    TIPOSMODAL = [
        ('autoopen', 'Abrir automático'),
        ('updade_notification', 'Notificação Atualizada'),
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
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
    