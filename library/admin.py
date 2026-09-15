from django.contrib import admin
from .models import Genre, Publisher, Book

# Model admin da tabela Genre
class GenreModelAdmin(admin.ModelAdmin):
    list_display = ('text_genre', )
    search_fields = ('text_genre', )


# Model admin da tabela Publisher
class PublisherModelAdmin(admin.ModelAdmin):
    list_display = ('name_publisher',)
    search_fields = ('name_publisher',)


# Model admin da tabela Book
class BookModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'autor', 'genre', 'publisher',)
    search_fields = ('title', 'genre', 'name_publisher',)


admin.site.register(Genre, GenreModelAdmin)
admin.site.register(Publisher, PublisherModelAdmin)
admin.site.register(Book, BookModelAdmin)