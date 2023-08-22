"""
Module with views for online shop.

products orders etc.
"""
from csv import DictWriter
from timeit import default_timer

from django.contrib.gis.feeds import Feed
from django.http import HttpResponse,\
    HttpRequest, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView,\
    DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,\
    PermissionRequiredMixin
from rest_framework.parsers import MultiPartParser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiResponse
from .common import save_csv_products


@extend_schema(description="Products view CRUD")
class ProductViewSet(ModelViewSet):
    """
    Набор представлений для действий над Product.

    Полный CRUD для сущностей товаров.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]
    search_fields = ["name", "description"]

    filterset_fields = [
        "name",
        "description",
        "price",
        "discount",
        "archived",
    ]
    ordering_fields = [
        "name",
        "price",
        "discount",
    ]
    @extend_schema(
        summary="Get one product by ID",
        description="Retrives **product**, return 404 if not found",
        responses={
            200: ProductSerializer,
            404: OpenApiResponse(description="Empty response, no product with ID"),
        }
    )
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)
    @action(methods=["get"], detail=False)
    def download_csv(self, request: Request):
        response = HttpResponse(content_type="text/csv")
        filename = "products-export.csv"
        response["Content-Disposition"] = f"attachment; filename={filename}"
        queryset = self.filter_queryset(self.get_queryset())
        fields = [
            "name",
            "description",
            "price",
            "discount",
        ]
        queryset = queryset.only(*fields)
        writer = DictWriter(response, fieldnames=fields)
        writer.writeheader()

        for product in queryset:
            writer.writerow({
                field: getattr(product, field)
                for field in fields
            })

        return response
    @action(detail=False, methods=['post'], parser_classes=[MultiPartParser])
    def upload_csv(self, request: Request):

        products = save_csv_products(
            request.FILES["file"].file,
            encoding=request.encoding,
        )
        serializer =  self.get_serializer(products, many=True)
        return Response(serializer.data)


class LatestProductsFeed(Feed):
    title = "New products"
    description = "New devices!"
    link = reverse_lazy("shopapp:products_list")

    def items(self):
        return (
        Product.objects.all()[:2]
    )

    def item_title(self, item: Product):
        return item.name

    def item_description(self, item: Product):
        return item.description[:50]


class OrderViewSet(ModelViewSet):
    """Набор представлений для действия над Order."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]
    search_fields = ["user", "products"]

    filterset_fields = [
        "delivery_address",
        "promocode",
        "created_at",
        "user",
        "products",
    ]
    ordering_fields = [
        "created_at",
        "user",
    ]


class ShopIndexView(View):
    """Class describing how to show Shop base page."""

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Переопределение базовой функции.

        Shows index.html.
        """
        products = [
            ('Laptop', 1999),
            ('Desktop', 2999),
            ('Smartphone', 999),
        ]
        context = {
            "time_running": default_timer(),
            "products": products,
            "items": 1,
        }
        return render(request, 'shopapp/shop-index.html', context=context)


class ProductDetailsView(DetailView):
    """Class describes how to show Product details."""

    template_name = "shopapp/products-details.html"
    # model = Product
    context_object_name = "product"
    queryset = Product.objects.prefetch_related("images")


class ProductsListView(ListView):
    """Class describes how to show Product list."""

    template_name = "shopapp/products-list.html"
    # model = Product
    context_object_name = "products"
    queryset = Product.objects.filter(archived=False)


class ProductCreateView(CreateView):
    """Class describes how to show Product create form."""

    model = Product
    fields = "name", "price", "description", "discount", "preview"
    success_url = reverse_lazy("shopapp:products_list")


class ProductUpdateView(UpdateView):
    """Class describes how to show Product update form."""

    model = Product
    fields = "name", "price", "description", "discount", "preview"
    template_name_suffix = "_update_form"

    def get_success_url(self):
        """Определяет куда вернуться после успешного обновления продукта."""
        return reverse(
            "shopapp:product_details",
            kwargs={"pk": self.object.pk},
        )


class ProductDeleteView(DeleteView):
    """Class for show Product delete page."""

    model = Product
    success_url = reverse_lazy("shopapp:products_list")

    def form_valid(self, form):
        """Указывает куда вернуться после удаления продукта."""
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class OrdersListView(LoginRequiredMixin, ListView):
    """Класс определяет отображение списка заказов."""

    queryset = (
        Order.objects
        .select_related("user")
        .prefetch_related("products")
    )


class OrderDetailView(PermissionRequiredMixin, DetailView):
    """Класс определяет отображение деталей заказов."""

    permission_required = "shopapp.view_order"
    queryset = (
        Order.objects
        .select_related("user")
        .prefetch_related("products")
    )


class ProductsDataExportView(View):
    """Класс определяет страницу для экспорта данных."""

    def get(self, request: HttpRequest) -> JsonResponse:
        """Функция для принятия данных по Product."""
        products = Product.objects.order_by("pk").all()
        products_data = [
            {
                "pk": product.pk,
                "name": product.name,
                "price": product.price,
                "archived": product.archived,
            }
            for product in products
        ]
        return JsonResponse({"products": products_data})
