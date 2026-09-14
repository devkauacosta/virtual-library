from django.db import models

# Tabela de Gêneros Literarios
class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    text_genre = models.CharField(max_length=200)

    def __str__(self):
        return self.text_genre

# Tabela de editoras
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name_publisher = models.CharField(max_length=200)

    def __str__(self):
        return self.name
