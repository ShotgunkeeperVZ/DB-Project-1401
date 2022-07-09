from django.db import connection, IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

import sql_functions
from store.serializers import ProductSerializer, ReviewSerializer, AddProductSerializer, AddReviewSerializer, \
    AddCustomerSerializer, CustomerSerializer


def select_customer_by_user_id(user_id):
    query = f"""SELECT * FROM store_customer
                WHERE user_id={user_id};"""
    with connection.cursor() as cursor:
        cursor.execute(query)
        one_selected = sql_functions.dictfetchall(cursor)[0]

    return one_selected


def update_customer_by_user_id(user_id, data):
    set_query_assignment = ""
    valid_data = {data_key: data_value for data_key, data_value
                  in data.items() if data_value not in [[''], []]}

    for item in valid_data.items():
        if type(item[1]) is list:
            set_query_assignment += f"{item[0]}='{item[1][0]}', "
        else:
            set_query_assignment += f"{item[0]}='{item[1]}', "

    # to remove ', ' from end of set_query_assignment
    set_query_assignment = set_query_assignment[:-2]

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
    return Response(sql_functions.select_one_row(1, 'store_product'))


class ProductViewSet(ModelViewSet, sql_functions.SQLHttpClass):
    table_name = "store_product"
    all_products = sql_functions.select_all_rows(table_name)
    queryset = all_products
    lookup_field = 'id'

    def __init__(self, **kwargs):
        super().__init__(self.table_name, **kwargs)
        # SHM.__init__(self, self.table_name, **kwargs)

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return AddProductSerializer
        return ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        return self.sql_retrieve(self.table_name, request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return self.sql_destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
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
        all_selected = None
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
            return ModelViewSet.create(self, request, *args, **kwargs)
        except IntegrityError:
            return Response({'detail': 'sql constraint failed (rating cannot be less than 0 and more than 5)'},
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return self.sql_destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        try:
            return self.sql_update(request, *args, **kwargs)
        except IntegrityError:
            return Response({'detail': 'sql constraint failed (rating cannot be less than 0 and more than 5)'},
                            status=status.HTTP_400_BAD_REQUEST)


class CustomerViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,
                      GenericViewSet, sql_functions.SQLHttpClass):
    table_name = 'store_customer'
    lookup_field = 'id'
    queryset = sql_functions.select_all_rows(table_name)

    def __init__(self, **kwargs):
        super().__init__(self.table_name, **kwargs)

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'POST']:
            return AddCustomerSerializer
        return CustomerSerializer

    def retrieve(self, request, *args, **kwargs):
        return self.sql_retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return self.sql_update(request, *args, **kwargs)

    @action(detail=False, methods=['GET', 'PUT'])
    def me(self, request, *args, **kwargs):
        if request.user.id is None:
            # customer = self.create(request, *args, **kwargs)
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

