from django.db import models
# só para teste
class SiteConfiguration(models.Model):
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    instagram = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)

    def __str__(self):
        return "Configuração do Site"
    
