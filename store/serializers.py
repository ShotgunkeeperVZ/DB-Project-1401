from django.db import connection
from rest_framework import serializers


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
    user_id = serializers.IntegerField()
    phone = serializers.IntegerField()
    address = serializers.CharField()
    postal_code = serializers.CharField()

    def create(self, validated_data):
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO store_customer (phone, address, postal_code, user_id)
                              VALUES (%s, %s, %s, %s)""",
                           [
                               validated_data['phone'],
                               validated_data['address'],
                               validated_data['postal_code'],
                               validated_data['user_id'],
                           ])
        return validated_data

