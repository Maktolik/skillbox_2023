from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from .models import *


class SpicificationsInline(admin.TabularInline):
    model = Specifications


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductInline(admin.TabularInline):
    model = Product
    readonly_fields = ["sold"]


class SubCategoryInLine(admin.TabularInline):
    model = SubCategory


class OrderItemInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ["order", "item", "count"]


@admin.action(description="mark as limmited")
def mark_limited(
        modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet
):
    queryset.update(limited=True)


@admin.action(description="unmark as limited")
def unmark_limited(
        modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet
):
    queryset.update(limited=False)


@admin.action(description="mark as published")
def mark_published(
        modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet
):
    queryset.update(is_published=True)


@admin.action(description="unmark as published")
def unmark_published(
        modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet
):
    queryset.update(is_published=False)


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
    list_display = ["id", "title", "created_at"]
    list_display_links = ["id", "title"]
    search_fields = ["id", "title"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SubCategoryInLine,
    ]
    list_display = ["id", "title", "sort_index"]
    list_display_links = ["id", "title"]
    ordering = ["id", "sort_index"]
    fieldsets = [
        (
            None,
            {
                "fields": (
                    "title",
                    "sort_index",
                    "image",
                ),
            },
        ),
        (
            "Tags",
            {
                "fields": ("tags",),
            },
        ),
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = [
        mark_limited,
        unmark_limited,
        mark_published,
        unmark_published,
    ]
    inlines = [
        ProductImageInline,
        SpicificationsInline,
    ]
    list_display = [
        "id",
        "sort_index",
        "name",
        "shop",
        "quantity",
        "description_short",
        "category",
        "is_published",
        "limited",
    ]
    list_display_links = ["id", "name"]
    ordering = ["id", "sort_index", "-name", "shop"]
    search_fields = ["name", "description", "shop"]
    readonly_fields = ["sold"]
    fieldsets = [
        (
            None,
            {
                "fields": (
                    "shop",
                    "name",
                    "description",
                    "quantity",
                    "category",
                    "subcategory",
                ),
            },
        ),
        (
            "Price options",
            {
                "fields": ("price", "discount"),
            },
        ),
        (
            "Sort index",
            {
                "fields": ("sort_index",),
            },
        ),
        (
            "Images",
            {
                "fields": ("preview",),
            },
        ),
        (
            "Publication status",
            {
                "fields": ("is_published",),
            },
        ),
        (
            "Other options",
            {
                "fields": ("limited",),
                "classes": ("collapse",),
                "description": 'Extra options.Field "limited" for mark item as limited.',
            },
        ),
    ]

    def description_short(self, obj: Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + "..."


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id", "item", "rate", "created_at", "author", "text_short"]
    list_display_links = ["id", "item"]
    search_fields = ["id", "item", "author"]

    def text_short(self, obj: Review) -> str:
        if len(obj.text) < 48:
            return obj.text
        return obj.text[:48] + "..."


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInline,
    ]
    list_display = ["id", "user", "created_at", "city", "address", "totalCost"]
    list_display_links = ["id", "user"]
    search_fields = ["id", "user"]
    fieldsets = [
        (
            None,
            {
                "fields": ("user", "city", "address", "totalCost"),
            },
        ),
        (
            "Information",
            {
                "fields": (
                    "fullName",
                    "email",
                    "phone",
                    "paymentType",
                    "status",
                    "deliveryType",
                ),
            },
        ),
    ]


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ["id", "item", "salePrice", "dateFrom", "dateTo"]
    list_display_links = ["id", "item"]
    search_fields = ["id", "item"]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "order", "number", "name", "payment", "created_at"]
    list_display_links = ["id", "user", "order"]
    search_fields = ["id", "user", "order", "payment"]
    readonly_fields = ["id", "user", "order", "number", "name", "payment", "created_at"]
