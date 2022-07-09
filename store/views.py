from django.db import connection
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from store.serializers import ProductSerializer, ReviewSerializer, AddProductSerializer, AddReviewSerializer


def dictfetchall(cursor):
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def select_all_rows(table_name):
    all_selected = None
    query = f"SELECT * FROM {table_name};"
    with connection.cursor() as cursor:
        cursor.execute(query)
        all_selected = dictfetchall(cursor)

    return all_selected


def select_one_row(pk, table_name):
    one_selected = None
    query = f"""SELECT * FROM {table_name}
                WHERE id={pk};"""
    with connection.cursor() as cursor:
        cursor.execute(query)
        one_selected = dictfetchall(cursor)[0]

    return one_selected


def delete_one_row(pk, table_name):
    query = f"""DELETE FROM {table_name}
                WHERE id={pk};"""
    with connection.cursor() as cursor:
        cursor.execute(query)


def update_one_row(pk, table_name, data):
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
        UPDATE {table_name}
        SET {set_query_assignment} 
        WHERE id={pk};
    """

    with connection.cursor() as cursor:
        cursor.execute(query)

    return select_one_row(pk, table_name)


@api_view()
def test(request):
    return Response(select_one_row(1, 'store_product'))


class ProductViewSet(ModelViewSet):
    table_name = "store_product"
    all_products = select_all_rows(table_name)
    queryset = all_products
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return AddProductSerializer
        return ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = select_one_row(kwargs['id'], self.table_name)
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except IndexError:
            return Response({"detail": "Not Found."},
                            status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        delete_one_row(kwargs['id'], self.table_name)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        instance = update_one_row(kwargs['id'], self.table_name, dict(request.data))
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ReviewViewSet(ModelViewSet):
    table_name = "store_review"
    lookup_field = 'id'

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
            all_selected = dictfetchall(cursor)

        return all_selected

    def retrieve(self, request, *args, **kwargs):
        try:
            # instance = select_one_row(kwargs['id'], self.table_name)
            query = f"""SELECT * FROM {self.table_name}
                        WHERE id={kwargs['id']} AND product_id={self.kwargs['product_id']};"""
            with connection.cursor() as cursor:
                cursor.execute(query)
                instance = dictfetchall(cursor)[0]

            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except IndexError:
            return Response({"detail": "Not Found."},
                            status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        delete_one_row(kwargs['id'], self.table_name)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        instance = update_one_row(kwargs['id'], self.table_name, dict(request.data))
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


