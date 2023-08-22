from typing import Sequence

from django.contrib.auth.models import User
from django.core.management import BaseCommand


from shopapp.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Create demo select fields")
        users_info = User.objects.values_list("username", flat=True)
        for u_info in users_info:
            print(u_info)

        # product_values = Product.objects.values("pk", "name")
        # for p_values in product_values:
        #     print((p_values))

        self.stdout.write("Done")