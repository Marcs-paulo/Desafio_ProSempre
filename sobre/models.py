# sobre/models.py
from django.db import models

class CardsHistoria(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Valores(models.Model):
    title = models.CharField(max_length=100)
    position = models.CharField(max_length=50, choices=[('top','Top'), ('left','Left'), ('right','Right')])

    def __str__(self):
        return self.title

class Membros(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team_photos/')

    def __str__(self):
        return self.name
