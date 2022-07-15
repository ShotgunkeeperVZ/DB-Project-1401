from django.db import connection, IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, \
    ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

import sql_functions
from store.serializers import ProductSerializer, ReviewSerializer, \
    CustomerSerializer, AddCartItemSerializer, CartItemSerializer, CartSerializer, \
    AddCartSerializer, CreateOrderSerializer, OrderSerializer, OrderItemSerializer, UpdateCartSerializer, \
    AddProductSerializer, AddReviewSerializer, AddCustomerSerializer


def select_customer_by_user_id(user_id):
    query = f"""SELECT * FROM store_customer
                WHERE user_id={user_id};"""
    with connection.cursor() as cursor:
        cursor.execute(query)
        one_selected = sql_functions.dictfetchall(cursor)[0]

    return one_selected


def update_customer_by_user_id(user_id, data):
    set_query_assignment = sql_functions.create_set_query_assignment(data)

    query = f"""
        UPDATE store_customer
        SET {set_query_assignment} 
        WHERE user_id={user_id};
    """

    with connection.cursor() as cursor:
        cursor.execute(query)

    return select_customer_by_user_id(user_id)


@api_view()
def test(request):
    query = f"""SELECT * FROM store_cartitem
                WHERE cart_id='c54f645e-0c2a-44b3-8318-b51e8af0cecc'"""
    with connection.cursor() as cursor:
        cursor.execute(query)
        all_selected = sql_functions.dictfetchall(cursor)
    return Response(all_selected)

    # return Response(sql_functions.select_one_row_by_id(3, 'store_product'))


class ProductViewSet(ModelViewSet, sql_functions.SQLHttpClass):
    table_name = "store_product"
    # all_products = sql_functions.select_all_rows(table_name)
    lookup_field = 'id'

    def get_queryset(self):
        return sql_functions.select_all_rows(self.table_name)

    def __init__(self, **kwargs):
        super().__init__(self.table_name, **kwargs)

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return AddProductSerializer
        return ProductSerializer

    def create(self, request, *args, **kwargs):
        ModelViewSet.create(self, request, *args, **kwargs)
        return Response(sql_functions.get_last_record_data(self.table_name), status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        return self.sql_retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return self.sql_destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        numeric_fields = ['price', 'inventory']
        is_not_null, response = self.evaluate_null_numeric_data(request.data, numeric_fields)
        if not is_not_null:
            return response
        is_positive, response = self.evaluate_positive_or_zero_numeric_data(request.data, numeric_fields)
        if not is_positive:
            return response
        return self.sql_update(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet, sql_functions.SQLHttpClass):
    table_name = "store_review"
    lookup_field = 'id'

    def __init__(self, **kwargs):
        super().__init__(self.table_name, **kwargs)

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return AddReviewSerializer
        return ReviewSerializer

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_id']}

    def get_queryset(self):
        query = f"""SELECT * FROM store_review
                    WHERE product_id={self.kwargs['product_id']};"""
        with connection.cursor() as cursor:
            cursor.execute(query)
            all_selected = sql_functions.dictfetchall(cursor)

        return all_selected

    def retrieve(self, request, *args, **kwargs):
        try:
            query = f"""SELECT * FROM {self.table_name}
                        WHERE id={kwargs['id']} AND product_id={self.kwargs['product_id']};"""
            with connection.cursor() as cursor:
                cursor.execute(query)
                instance = sql_functions.dictfetchall(cursor)[0]

            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except IndexError:
            return Response({"detail": "Not Found."},
                            status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        try:
            numeric_fields = ['rating']
            is_not_null, response = self.evaluate_null_numeric_data(request.data, numeric_fields)
            if not is_not_null:
                return response

            rating = int(request.data['rating'])
            if rating > 5 or rating < 0:
                return Response({'detail': 'rating cannot be less than 0 and more than 5'},
                                status=status.HTTP_400_BAD_REQUEST)
            ModelViewSet.create(self, request, *args, **kwargs)
            return Response(sql_functions.get_last_record_data(self.table_name), status=status.HTTP_201_CREATED)

        except IntegrityError:
            return Response({'detail': 'sql constraint failed'},
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return self.sql_destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        try:
            numeric_fields = ['rating']
            is_not_null, response = self.evaluate_null_numeric_data(request.data, numeric_fields)
            if not is_not_null:
                return response

            if 'rating' in request.data.keys():
                rating = int(request.data['rating'])
                if rating > 5 or rating < 0:
                    return Response({'detail': 'rating cannot be less than 0 and more than 5'},
                                    status=status.HTTP_400_BAD_REQUEST)
            return self.sql_update(request, *args, **kwargs)
        except IntegrityError:
            return Response({'detail': 'sql constraint failed'},
                            status=status.HTTP_400_BAD_REQUEST)


class CustomerViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,
                      GenericViewSet, sql_functions.SQLHttpClass):
    lookup_field = 'id'
    table_name = 'store_customer'

    def __init__(self, **kwargs):
        super().__init__(self.table_name, **kwargs)

    def get_queryset(self):
        return sql_functions.select_all_rows(self.table_name)

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'POST']:
            return AddCustomerSerializer
        return CustomerSerializer

    def create(self, request, *args, **kwargs):
        if request.user.id is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return ModelViewSet.create(self, request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return self.sql_retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return self.sql_update(request, *args, **kwargs)

    @action(detail=False, methods=['GET', 'PUT'])
    def me(self, request, *args, **kwargs):
        if request.user.id is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            try:
                customer = select_customer_by_user_id(request.user.id)
            except IndexError:
                return Response({"detail": "Not Found."},
                                status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            instance = update_customer_by_user_id(request.user.id, dict(request.data))
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data)


class CartItemViewSet(ModelViewSet, sql_functions.SQLHttpClass):
    lookup_field = 'id'
    table_name = 'store_cartitem'

    def __init__(self, **kwargs):
        super().__init__(self.table_name, **kwargs)

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'POST', 'PATCH']:
            return AddCartItemSerializer
        return CartItemSerializer

    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_id']}

    def get_queryset(self):
        query = f"""SELECT * FROM store_cartitem
                    WHERE cart_id='{self.kwargs['cart_id']}';"""
        with connection.cursor() as cursor:
            cursor.execute(query)
            all_selected = sql_functions.dictfetchall(cursor)

        return all_selected

    def retrieve(self, request, *args, **kwargs):
        try:
            query = f"""SELECT * FROM {self.table_name}
                        WHERE id={kwargs['id']} AND cart_id='{self.kwargs['cart_id']}';"""
            with connection.cursor() as cursor:
                cursor.execute(query)
                instance = sql_functions.dictfetchall(cursor)[0]

            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except IndexError:
            return Response({"detail": "Not Found."},
                            status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        try:
            numeric_fields = ['product_id', 'quantity']

            is_not_null, response = self.evaluate_null_numeric_data(request.data, numeric_fields)
            if not is_not_null:
                return response
            is_positive, response = self.evaluate_positive_numeric_data(request.data, numeric_fields)
            if not is_positive:
                return response

            sql_functions.select_one_row_by_id(self.request.data['product_id'], 'store_product')

            ModelViewSet.create(self, request, *args, **kwargs)
            return Response(sql_functions.get_last_record_data(self.table_name), status=status.HTTP_201_CREATED)

        except IntegrityError:
            return Response({'detail': 'sql constraint failed.'},
                            status=status.HTTP_400_BAD_REQUEST)
        except IndexError:
            return Response({"detail": "Product does not exist."},
                            status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        return self.sql_destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        try:
            numeric_fields = ['product_id', 'quantity']

            is_not_null, response = self.evaluate_null_numeric_data(request.data, numeric_fields)
            if not is_not_null:
                return response
            is_positive, response = self.evaluate_positive_numeric_data(request.data, numeric_fields)
            if not is_positive:
                return response

            sql_functions.select_one_row_by_id(self.request.data['product_id'], 'store_product')
            return self.sql_update(request, *args, **kwargs)
        except IntegrityError:
            return Response({'detail': 'sql constraint failed'},
                            status=status.HTTP_400_BAD_REQUEST)
        except IndexError:
            return Response({"detail": "Product does not exist."},
                            status=status.HTTP_404_NOT_FOUND)


class CartViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,
                  DestroyModelMixin, GenericViewSet, sql_functions.SQLHttpClass):
    table_name = "store_cart"
    lookup_field = 'id'

    def __init__(self, **kwargs):
        super().__init__(self.table_name, **kwargs)

    def get_queryset(self):
        return sql_functions.select_all_rows(self.table_name)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartSerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return UpdateCartSerializer
        return CartSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            query = f"""SELECT * FROM {self.table_name}
                        WHERE id='{kwargs['id']}';"""
            with connection.cursor() as cursor:
                cursor.execute(query)
                instance = sql_functions.dictfetchall(cursor)[0]

            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except IndexError:
            return Response({"detail": "Not Found."},
                            status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        if request.data['delivery_method'] not in ['P', 'V']:
            return Response({'detail': 'Selected delivery method is not available'},
                            status=status.HTTP_400_BAD_REQUEST)

        update_query = f"""
            UPDATE {self.table_name}
            SET delivery_method='{request.data['delivery_method']}' 
            WHERE id='{kwargs['id']}';
        """
        instance_query = f"""
            SELECT * FROM {self.table_name}
            WHERE id='{kwargs['id']}';
        """
        with connection.cursor() as cursor:
            cursor.execute(update_query)
            cursor.execute(instance_query)
            instance = sql_functions.dictfetchall(cursor)[0]

        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        query = f"""DELETE FROM {self.table_name}
                    WHERE id='{kwargs['id']}';"""
        with connection.cursor() as cursor:
            cursor.execute(query)

        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderViewSet(ModelViewSet, sql_functions.SQLHttpClass):
    table_name = 'store_order'
    lookup_field = 'id'

    def __init__(self, **kwargs):
        super().__init__(self.table_name, **kwargs)

    def get_serializer_class(self):
        if self.request.method in ['POST']:
            return CreateOrderSerializer
        return OrderSerializer

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}

    def get_queryset(self):
        return sql_functions.select_all_rows(self.table_name)

    def create(self, request, *args, **kwargs):
        try:
            ModelViewSet.create(self, request, *args, **kwargs)
            return Response(sql_functions.get_last_record_data(self.table_name),
                            status=status.HTTP_201_CREATED)
        except IndexError:
            return Response({"detail": "Not Found."},
                            status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, *args, **kwargs):
        return self.sql_retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return self.sql_destroy(request, *args, **kwargs)


class OrderItemViewSet(ListModelMixin, CreateModelMixin, GenericViewSet, sql_functions.SQLHttpClass):
    table_name = 'store_order'
    lookup_field = 'id'

    def __init__(self, **kwargs):
        super().__init__(self.table_name, **kwargs)

    def get_serializer_class(self):
        return OrderItemSerializer

    def get_queryset(self):
        query = f"""SELECT * FROM store_orderitem
                    WHERE order_id='{self.kwargs['order_id']}';"""
        with connection.cursor() as cursor:
            cursor.execute(query)
            all_selected = sql_functions.dictfetchall(cursor)

        return all_selected

    def retrieve(self, request, *args, **kwargs):
        try:
            query = f"""SELECT * FROM {self.table_name}
                        WHERE id={kwargs['id']} AND order_id='{self.kwargs['order_id']}';"""
            with connection.cursor() as cursor:
                cursor.execute(query)
                instance = sql_functions.dictfetchall(cursor)[0]

            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except IndexError:
            return Response({"detail": "Not Found."},
                            status=status.HTTP_404_NOT_FOUND)

