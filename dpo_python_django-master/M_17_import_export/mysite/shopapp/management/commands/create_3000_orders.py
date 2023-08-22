from typing import Sequence
import random

from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction

from shopapp.models import Order, Product




class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        for i in range(3000):
            self.stdout.write(f"Create {i} order with products")
            user = User.objects.get(username=random.choice(["admin","Zeka","Mili"]))
            products: Sequence[Product] = Product.objects.defer("description", "price", "created_at").all()
            # products: Sequence[Product] = Product.objects.only("delivery_address", "promocode").all()
            order = Order.objects.create(
                delivery_address=random.choice(["ul Sovetov, d 313","ul Moscka, d 15", "ul Juki d 22"]),
                promocode=random.choice(["SKILLBOX55","PROMO25","PRO33"]),
                user=user,
            )
            for product in products:
                order.products.add(product)
            order.save()
            self.stdout.write(f"Created {i} order {order}")
