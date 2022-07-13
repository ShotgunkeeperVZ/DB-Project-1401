import uuid

from django.db import connection
from rest_framework import serializers

import sql_functions


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=5, decimal_places=3)
    inventory = serializers.IntegerField()


class AddProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=5, decimal_places=3)
    inventory = serializers.IntegerField()

    def create(self, validated_data):
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO store_product (title, price, inventory)
                              VALUES (%s, %s, %s)""",
                           [
                               validated_data['title'],
                               validated_data['price'],
                               validated_data['inventory'],
                           ])
        return validated_data


class ReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    product_id = serializers.IntegerField()
    content = serializers.CharField()
    rating = serializers.IntegerField()


class AddReviewSerializer(serializers.Serializer):
    content = serializers.CharField()
    rating = serializers.IntegerField()

    def create(self, validated_data):
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO store_review (product_id, content, rating)
                              VALUES (%s, %s, %s)""",
                           [
                               self.context['product_id'],
                               validated_data['content'],
                               validated_data['rating'],
                           ])
        return validated_data


class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    phone = serializers.IntegerField()
    address = serializers.CharField()
    postal_code = serializers.CharField()


class AddCustomerSerializer(serializers.Serializer):
    phone = serializers.IntegerField()
    address = serializers.CharField()
    postal_code = serializers.CharField()

    def create(self, validated_data):
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO store_customer (phone, address, postal_code)
                              VALUES (%s, %s, %s)""",
                           [
                               validated_data['phone'],
                               validated_data['address'],
                               validated_data['postal_code'],
                           ])
        return validated_data


class CartItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    # product_id = serializers.IntegerField()
    item_info = serializers.SerializerMethodField(method_name='get_item', read_only=True)
    cart_id = serializers.CharField()
    quantity = serializers.IntegerField()
    total_price = serializers.SerializerMethodField(method_name='cal_total_price', read_only=True)

    def get_item(self, cart_item):
        query = f"""
                SELECT id, title, price
                FROM store_product
                WHERE id = {cart_item['product_id']}
                """

        with connection.cursor() as cursor:
            cursor.execute(query)
            item = sql_functions.dictfetchall(cursor)[0]
        return item

    def cal_total_price(self, cart_item):
        return self.get_item(cart_item)['price'] * cart_item['quantity']


class AddCartItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def create(self, validated_data):
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO store_cartitem (product_id, cart_id, quantity)
                              VALUES (%s, %s, %s)""",
                           [
                               validated_data['product_id'],
                               self.context['cart_id'],
                               validated_data['quantity'],
                           ])
        return validated_data


class CartSerializer(serializers.Serializer):
    id = serializers.CharField()
    items = serializers.SerializerMethodField(method_name='get_items', read_only=True)
    total_price = serializers.SerializerMethodField(method_name='cal_total_price', read_only=True)

    def get_items(self, cart):
        query = f"""
                SELECT store_cartitem.id, product_id, title, price, quantity
                FROM store_cartitem
                INNER JOIN store_product
                ON store_cartitem.product_id = store_product.id
                WHERE cart_id=\'{cart['id']}\';
                """

        with connection.cursor() as cursor:
            cursor.execute(query)
            items = sql_functions.dictfetchall(cursor)
        return items

    def cal_total_price(self, cart):
        price = 0
        for item in self.get_items(cart):
            price += item['price'] * item['quantity']
        return price


class AddCartSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)

    def create(self, validated_data):
        generated_id = uuid.uuid4()
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO store_cart (id)
                              VALUES (%s)""",
                           [generated_id])
        validated_data = {'id': generated_id}

        return validated_data
