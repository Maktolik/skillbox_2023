from random import choices
from string import ascii_letters

from django.contrib.auth.models import User, Permission
from django.test import TestCase
from django.urls import reverse

from mysite import settings
from shopapp.models import Product, Order


# class ProductCreateViewTestCase(TestCase):
#     def setUp(self) -> None:
#         self.product_name = "".join(choices(ascii_letters, k=10))
#         Product.objects.filter(name=self.product_name).delete()
#
#     def test_create_product(self):
#         response = self.client.post(
#             reverse("shopapp:product_create"),
#             {
#                 "name": self.product_name,
#                 "price": "222",
#                 "description": "new PSP 2023",
#                 "discount": "25",
#                 "created_by": "Tolik",
#              }
#         )
#         self.assertRedirects(response, reverse("shopapp:products_list"))
#         self.assertTrue(
#             Product.objects.filter(name=self.product_name).exists()
#         )
#
#
# class ProductDetailsViewTestCase(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.product = Product.objects.create(name="Best PC")
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.product.delete()
#
#     def test_get_product_and_check_content(self):
#         response = self.client.get(
#             reverse("shopapp:product_details", kwargs={"pk": self.product.pk})
#         )
#         self.assertContains(response, self.product.name)
#
#
# class ProductsListViewTestCase(TestCase):
#     fixtures = [
#         'products-fixture.json',
#     ]
#
#     def test_products(self):
#         response = self.client.get(reverse("shopapp:products_list"))
#         self.assertQuerySetEqual(
#             qs=Product.objects.filter(archived=False).all(),
#             values=(p.pk for p in response.context["products"]),
#             transform=lambda p:p.pk,
#         )
#         self.assertTemplateUsed(response, 'shopapp/products-list.html')
#
#
# class OrdersListViewTestCase(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         # cls.credentials = dict(username="test", password="10061997OkO")
#         cls.user= User.objects.create_user(username="test", password="10061997OkO")
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.user.delete()
#
#     def setUp(self) -> None:
#         self.client.force_login(self.user)
#
#     def test_orders_view(self):
#         response = self.client.get(reverse("shopapp:orders_list"))
#         self.assertContains(response, "Orders")
#
#     def test_orders_view_not_auth(self):
#         self.client.logout()
#         response = self.client.get(reverse("shopapp:orders_list"))
#         self.assertEqual(response.status_code, 302)
#         self.assertIn(str(settings.LOGIN_URL), response.url)
#
#
# class ProductsExportViewTestCase(TestCase):
#     fixtures = [
#         'products-fixture.json'
#     ]
#
#     def test_get_products_view(self):
#         response = self.client.get(
#             reverse("shopapp:products_export"),
#         )
#         self.assertEqual(response.status_code, 200)
#         products = Product.objects.order_by("pk").all()
#         expected_data = [
#             {
#                 "pk": product.pk,
#                 "name": product.name,
#                 "price": str(product.price),
#                 "archived": product.archived,
#             }
#             for product in products
#         ]
#         product_data = response.json()
#         self.assertEqual(
#             product_data["products"],
#             expected_data,
#         )

class OrderDetailsViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="test", password="10061997OkO")
        permission_order = Permission.objects.get(codename='view_order')
        cls.user.user_permissions.add(permission_order)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)
        self.order = Order.objects.create(
            delivery_address='Moscow',
            promocode='SKILLBOX',
            user=self.user,
        )

    def tearDown(self) -> None:
        self.order.delete()

    def test_order_details(self):
        order_test = self.order
        response = self.client.get(
            reverse("shopapp:order_details", kwargs={"pk": self.order.pk})
        )
        self.assertContains(response, self.order.delivery_address)
        self.assertContains(response, self.order.promocode)
        self.assertEqual(self.order.pk, order_test.pk)


class OrdersExportViewTestCase(TestCase):
    fixtures = [
        'orders-fixtures.json',
        'products-fixtures.json',
        'users-fixtures.json',
    ]
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username="test", password="10061997OkO", is_staff=True)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)
        self.order = Order.objects.create(
            delivery_address='Moscow',
            promocode='SKILLBOX',
            user=self.user,
        )

    def test_get_orders_view(self):
        response = self.client.get(
            reverse("shopapp:orders_export"),
        )
        # orders = Order.objects.order_by("pk").all()
        queryset = (
            Order.objects.order_by("pk")
            .select_related("user")
            .prefetch_related("products")
        )
        expected_data = [
            {
                "pk": order.pk,
                "delivery_address": order.delivery_address,
                "promocode": order.promocode,
                "user": order.user.pk,
                "products": str(order.products),
            }
            for order in queryset
        ]
        order_data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            order_data["orders"],
            expected_data,
        )