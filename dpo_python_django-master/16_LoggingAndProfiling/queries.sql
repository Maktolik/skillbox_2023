SELECT ("shopapp_order_products"."order_id") AS "_prefetch_related_val_order_id",
 "shopapp_product"."id",
  "shopapp_product"."name",
   "shopapp_product"."description",
    "shopapp_product"."price",
     "shopapp_product"."discount",
      "shopapp_product"."created_at",
       "shopapp_product"."archived",
        "shopapp_product"."preview" FROM "shopapp_product"
INNER JOIN "shopapp_order_products" ON ("shopapp_product"."id" = "shopapp_order_products"."product_id") WHERE "shopapp_order_products"."order_id" IN (1)
ORDER BY "shopapp_product"."name" ASC, "shopapp_product"."price" ASC; args=(1,); alias=default
