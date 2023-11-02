from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from main.serializers import BookSerializer
from rest_framework import permissions
from main.models import Book


class BookListView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
