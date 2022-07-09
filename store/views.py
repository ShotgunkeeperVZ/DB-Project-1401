from django.db import connection, IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

import sql_functions
from store.serializers import ProductSerializer, ReviewSerializer, AddProductSerializer, AddReviewSerializer


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
        # try:
        #     instance = sql_functions.select_one_row(kwargs['id'], self.table_name)
        #     serializer = self.get_serializer(instance)
        #     return Response(serializer.data)
        # except IndexError:
        #     return Response({"detail": "Not Found."},
        #                     status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        return self.sql_destroy(request, *args, **kwargs)
        # sql_functions.delete_one_row(kwargs['id'], self.table_name)
        # return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        return self.sql_update(request, *args, **kwargs)
    #     partial = kwargs.pop('partial', False)
    #     instance = sql_functions.update_one_row(kwargs['id'], self.table_name, dict(request.data))
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     return Response(serializer.data)


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

    def destroy(self, request, *args, **kwargs):
        return self.sql_destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        try:
            return self.sql_update(request, *args, **kwargs)
        except IntegrityError:
            return Response({'detail': 'sql constraint failed (rating cannot be less than 0 and more than 5)'},
                            status=status.HTTP_400_BAD_REQUEST)

