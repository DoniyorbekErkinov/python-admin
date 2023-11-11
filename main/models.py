from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    fullName = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, related_name="users")
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, related_name="users"
    )

    def save(self, *args, **kwargs):
        # Create default Role and Department if they don't exist
        role = Role.objects.get_or_create(name="Default Role")[0]
        department = Department.objects.get_or_create(name="Default Department")[0]
        self.role = role
        self.department = department
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


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
