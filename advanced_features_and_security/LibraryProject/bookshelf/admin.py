from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    search_fields = ("username", "email", "first_name", "last_name")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("date_of_birth", "profile_photo")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  
    list_filter = ("publication_year", "author")          
    search_fields = ("title", "author")                    

admin.site.register(Book, BookAdmin)
