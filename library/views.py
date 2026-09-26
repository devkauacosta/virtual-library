from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Publisher
from unidecode import unidecode

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
            books = books.filter(title__contains=search)
        return books    


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'


class PublisherListView(ListView):
    """
    Retorna uma lista de todos objetos da tabela Publisher
    """

    model = Publisher
    template_name = 'publishers.html'
    context_object_name = 'publishers'

    def get_queryset(self):
            publishers = super().get_queryset().order_by('name_publisher')
            search = self.request.GET.get('search')
            if search:
                publishers = publishers.filter(name_publisher__contains=search)
            return publishers