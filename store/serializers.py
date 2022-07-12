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
    product_id = serializers.IntegerField()
    cart_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class AddCartItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def create(self, validated_data):
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO store_cartitem (product_id, cart_id, quantity)
                              VALUES (%s, %s, %s)""",
                           [
                               validated_data['product_id'],
                               validated_data['cart_id'],
                               validated_data['quantity'],
                           ])
        return validated_data


class CartSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    items = serializers.SerializerMethodField(method_name='test', read_only=True)
    # total_price = serializers.IntegerField()

    def test(self, cart):
        query = f"""
                SELECT * FROM store_cartitem
                WHERE cart_id={cart['id']}
                """

        with connection.cursor() as cursor:
            cursor.execute(query)
            items = sql_functions.dictfetchall(cursor)
        return items


class AddCartSerializer(serializers.Serializer):
    def create(self, validated_data):
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO store_cart DEFAULT VALUES""")
        return validated_data
