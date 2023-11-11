from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from main.serializers import (
    BookSerializer,
    AuthorSerializer,
    CustomUserSerializer,
    DepartmentSerializer,
    RoleSerializer,
)
from rest_framework import permissions
from main.models import Book, Author, CustomUser, Department, Role


class CustomUserView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class DepartmentView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class RoleView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class AuthorsView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
