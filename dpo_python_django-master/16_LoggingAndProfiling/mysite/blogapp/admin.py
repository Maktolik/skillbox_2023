from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from .models import Author, Category, Tag, Article


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = "name", "bio"
    ordering = "name", "pk"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "name",
    ordering = "name",


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = "name",
    ordering = "name",


class AuthorInline(admin.TabularInline):
    model = Author


class CategoryInline(admin.TabularInline):
    model = Category


class TagInline(admin.StackedInline):
    model = Tag


@admin.register(Article)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        # AuthorInline,
        # CategoryInline,
        # TagInline,
    ]
    list_display = "title", "content", "pub_date", "author", "category", "tags_verbose"
    ordering = "author", "pub_date"

    def get_queryset(self, request):
        return Article.objects.select_related("author", "category").prefetch_related("tags")

    def tags_verbose(self, obj: Article) -> str:
        return obj.tags.name
