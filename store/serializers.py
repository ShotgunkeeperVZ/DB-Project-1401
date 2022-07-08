from django.db import connection
from rest_framework import serializers

# from store.models import Product, Review


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


class ReviewSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    # def create(self, validated_data):
    #     product_id = self.context['product_id']
    #     return Review.objects.create(product_id=product_id, **validated_data)
