from django.contrib import admin
from .models import AuthorModel, BookModel


@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name')


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'written_date', 'published_date', 'pages', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('written_date', 'published_date')
