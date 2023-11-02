from django.db import models


class Author(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    birthDate = models.DateField(null=True)

    def __str__(self) -> str:
        return self.firstName + " " + self.lastName


class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
