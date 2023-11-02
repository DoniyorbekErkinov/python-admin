from main.views import BookListView, BookDetailView, AuthorsView
from django.urls import path


urlpatterns = [
    path("authors/", AuthorsView.as_view()),
    path("books/", BookListView.as_view()),
    path("books/<int:pk>/", BookDetailView.as_view()),
]
