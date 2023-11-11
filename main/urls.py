from main.views import (
    BookListView,
    BookDetailView,
    AuthorsView,
    CustomUserView,
    CustomUserDetailView,
    DepartmentView,
    DepartmentDetailView,
    RoleView,
    RoleDetailView,
)
from django.urls import path


urlpatterns = [
    path("users/", CustomUserView.as_view()),
    path("users/<int:pk>/", CustomUserDetailView.as_view()),
    path("departments/", DepartmentView.as_view()),
    path("departments/<int:pk>/", DepartmentDetailView.as_view()),
    path("roles/", RoleView.as_view()),
    path("roles/<int:pk>/", RoleDetailView.as_view()),
    path("authors/", AuthorsView.as_view()),
    path("books/", BookListView.as_view()),
    path("books/<int:pk>/", BookDetailView.as_view()),
]
