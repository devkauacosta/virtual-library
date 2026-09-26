from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from library.views import BookListView, BookDetailView, PublisherListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookListView.as_view(), name='books_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('publishers/', PublisherListView.as_view(), name='publisher_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
