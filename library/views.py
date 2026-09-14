from django.shortcuts import render
from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    """
    Retorna uma lista de todos objetos da tabela Book
    """

    model = Book
    template_name = 'books.html'
    context_object_name = 'books'

    #Filtro de busca
    def get_queryset(self):
        books = super().get_queryset().order_by('title')
        search = self.request.GET.get('search')
        if search:
            books = books.filter(model_contains=search)
        return books