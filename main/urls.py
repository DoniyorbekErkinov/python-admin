from main.views import BookListView, BookDetailView
from django.urls import path


urlpatterns = [
    path('books/', BookListView.as_view()),
    path('books/<int:pk>/', BookDetailView.as_view())
]
