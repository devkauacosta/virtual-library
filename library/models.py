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


#Tabela de Livros
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='book_genre')
    publication_year = models.IntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, related_name='book_publisher')
