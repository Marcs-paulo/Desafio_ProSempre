from django.db import models

class Post(models.Model):
    CATEGORIES = [
        ("noticia", "Notícia"),
        ("dicas", "Dicas"),
        ("resenha", "Resenha"),
        ("classicos", "Clássicos"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)  # para gerar link /blog/slug
    content = models.TextField()
    image = models.ImageField(upload_to="posts/")
    tag = models.CharField(max_length=20, choices=CATEGORIES)
    date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=100, default="Por Equipe AZ Fell")
    author_image = models.ImageField(upload_to="authors/", null=True, blank=True)  # nova foto do autor

    def __str__(self):
        return self.title
