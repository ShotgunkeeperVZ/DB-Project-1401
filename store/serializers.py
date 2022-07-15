import uuid

from django.db import connection
from rest_framework import serializers

import sql_functions


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)


class AddCategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO store_category (name)
                              VALUES (%s)""",
                           [
                               validated_data['name']
                           ])
        return validated_data


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=14, decimal_places=4)
    inventory = serializers.IntegerField()
    category_info = serializers.SerializerMethodField(method_name='get_category_info', read_only=True)

    def get_category_info(self, product):
        if product['category_id']:
            return sql_functions.select_one_row_by_id(product['category_id'], 'store_category')


class AddProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=14, decimal_places=4)
    inventory = serializers.IntegerField()
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO store_product (title, price, inventory, category_id)
                              VALUES (%s, %s, %s, %s)""",
                           [
                               validated_data['title'],
                               validated_data['price'],
                               validated_data['inventory'],
                               validated_data['category_id']
                           ])
        return validated_data


class ReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    product_id = serializers.IntegerField(read_only=True)
    content = serializers.CharField()
    rating = serializers.IntegerField()
    score = serializers.IntegerField(read_only=True)


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
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    phone = serializers.CharField()
    address = serializers.CharField()
    postal_code = serializers.CharField()


class AddCustomerSerializer(serializers.Serializer):
    phone = serializers.CharField()
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
                               self.context['user_id']
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


class UpdateCartItemSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()


class CartSerializer(serializers.Serializer):
    id = serializers.CharField()
    # delivery_method for now is consist of "P" and "V" meaning post and vip
    delivery_method = serializers.CharField(read_only=True)
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
        delivery_method = cart['delivery_method']
        delivery_price = None
        if delivery_method == 'P':
            delivery_price = 10
        elif delivery_method == 'V':
            delivery_price = 30

        price = 0
        for item in self.get_items(cart):
            price += item['price'] * item['quantity']
        price += delivery_price
        return price


class AddCartSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True, required=False)
    delivery_method = serializers.CharField(read_only=True)

    def create(self, validated_data):
        generated_id = uuid.uuid4()
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO store_cart (id)
                              VALUES (%s)""",
                           [generated_id])
        validated_data = {'id': generated_id}

        return validated_data


class UpdateCartSerializer(serializers.Serializer):
    delivery_method = serializers.CharField()


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    price = serializers.IntegerField(read_only=True)
    # state is consist of "P", "C", "F" meaning pending, complete and failed
    state = serializers.CharField(read_only=True)
    customer_id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)


class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.CharField()

    def cal_total_price(self, items, delivery_method):
        delivery_price = None
        if delivery_method == 'P':
            delivery_price = 10
        elif delivery_method == 'V':
            delivery_price = 30

        price = 0
        for item in items:
            price += item['price'] * item['quantity']
        price += delivery_price
        return price

    def get_delivery_method(self, cart_id):
        get_delivery_method_query = f"""
            SELECT delivery_method FROM store_cart
            WHERE id='{cart_id}';
        """
        with connection.cursor() as cursor:
            cursor.execute(get_delivery_method_query)
            delivery_method = sql_functions.dictfetchall(cursor)[0]['delivery_method']
        return delivery_method

    def get_cart_items(self, cart_id):
        get_cart_items_query = f"""
            SELECT store_cartitem.id, product_id, quantity, price
            FROM store_cartitem
            INNER JOIN store_product
            ON store_cartitem.product_id = store_product.id
            WHERE cart_id='{cart_id}'
        """
        with connection.cursor() as cursor:
            cursor.execute(get_cart_items_query)
            all_item_selected = sql_functions.dictfetchall(cursor)
        return all_item_selected

    def get_customer_id(self):
        get_customer_id_query = f"""
            SELECT id FROM store_customer
            WHERE user_id={self.context['user_id']};
        """
        with connection.cursor() as cursor:
            cursor.execute(get_customer_id_query)
            customer_id = sql_functions.dictfetchall(cursor)[0]['id']
        return customer_id

    def create_order(self, items, delivery_method, customer_id):
        create_order_query = f"""
            INSERT INTO store_order (price, state, customer_id)
            VALUES (
                {self.cal_total_price(items, delivery_method)},
                'P',
                {customer_id}
            )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_order_query)

    def add_order_items(self, items, order_id):
        order_items_rows = ""
        for item in items:
            order_items_rows += f"({item['product_id']}, {order_id}, {item['quantity']}), "

        if order_items_rows:
            # to remove ,
            order_items_rows = order_items_rows[:-2]

            add_order_items_query = f"""
                INSERT INTO store_orderitem (product_id, order_id, quantity)
                VALUES {order_items_rows}
            """
            with connection.cursor() as cursor:
                cursor.execute(add_order_items_query)

    def delete_cart(self, cart_id):
        delete_cart_query = f"""
            DELETE FROM store_cart
            WHERE id='{cart_id}'
        """
        with connection.cursor() as cursor:
            cursor.execute(delete_cart_query)

    def create(self, validated_data):
        all_item_selected = self.get_cart_items(validated_data['cart_id'])
        customer_id = self.get_customer_id()
        delivery_method = self.get_delivery_method(validated_data['cart_id'])
        self.create_order(all_item_selected, delivery_method, customer_id)
        order_id = sql_functions.get_most_recent_order_id('store_order')
        self.add_order_items(all_item_selected, order_id)
        self.delete_cart(validated_data['cart_id'])
        return validated_data


class OrderItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    order_id = serializers.IntegerField()
    item_info = serializers.SerializerMethodField(method_name='get_item', read_only=True)
    quantity = serializers.IntegerField()
    total_price = serializers.SerializerMethodField(method_name='cal_total_price', read_only=True)

    def get_item(self, order_item):
        query = f"""
                SELECT id, title, price
                FROM store_product
                WHERE id = {order_item['product_id']}
                """
        with connection.cursor() as cursor:
            cursor.execute(query)
            item = sql_functions.dictfetchall(cursor)[0]
        return item

    def cal_total_price(self, cart_item):
        return self.get_item(cart_item)['price'] * cart_item['quantity']

