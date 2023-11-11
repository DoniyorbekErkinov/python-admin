from django.contrib import admin
from main.models import Book, Author
from django.contrib.auth.admin import UserAdmin
from .models import Role, Department, CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ("username", "fullName", "created_at", "role", "department")
    list_filter = ("role", "department")
    search_fields = ("username", "fullName")


class RoleAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Department, DepartmentAdmin)
# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
