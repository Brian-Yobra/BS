from rest_framework import viewsets
from .models import Books
from .serializer import BookSerializer

class BooksViewSet(viewsets.ModelViewSet):
    """
    Full CRUD endpoint for Books.
    Supports list, retrieve, create, update, delete.
    """
    queryset = Books.objects.all()
    serializer_class = BookSerializer