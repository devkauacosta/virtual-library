from django.contrib import admin
from django.urls import path
from library.views import BookListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookListView.as_view(), name='books_list'),
]
