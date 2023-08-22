from django.urls import path

from .views import *

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="categories"),
    path("catalog/", CatalogView.as_view(), name="catalog"),
    path("products/popular/", ProductsPopularView.as_view(), name="products_popular"),
    path("products/limited/", ProductsLimitedView.as_view(), name="products_limited"),
    path("sales", SalesView.as_view(), name="sales"),
    path("product/<int:id>/", ProductDetailsView.as_view(), name="product"),
    path("product/<int:id>/reviews/", ProductReviewCreateView.as_view(), name="product_review"),
    path("banners", BannerView.as_view(), name="banners"),
    path("orders", OrdersListView.as_view(), name="orders"),
    path("order/<int:id>", OrderCreateView.as_view(), name="order-create"),
    path("payment/<int:id>", PaymentView.as_view(), name="payment"),
    path("tags/", TagListView.as_view(), name="tags"),
    ]
