from django.db import models
# só para teste
class TestModel(models.Model):
    name = models.CharField(max_length=100)

