from django.db import connection
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

import sql_functions


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


def select_one_row_by_id(pk, table_name):
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


def create_set_query_assignment(data):
    set_query_assignment = ""
    valid_data = {data_key: data_value for data_key, data_value
                  in data.items() if data_value not in [[''], []]}

    for item in valid_data.items():
        if type(item[1]) is list:
            set_query_assignment += f"{item[0]}='{item[1][0]}', "
        else:
            set_query_assignment += f"{item[0]}='{item[1]}', "

    # to remove ', ' from end of set_query_assignment
    return set_query_assignment[:-2]


def update_one_row(pk, table_name, data):
    set_query_assignment = create_set_query_assignment(data)

    query = f"""
        UPDATE {table_name}
        SET {set_query_assignment} 
        WHERE id={pk};
    """

    with connection.cursor() as cursor:
        cursor.execute(query)

    return select_one_row_by_id(pk, table_name)


def get_most_recent_order_id(table_name):
    get_most_recent_order_id_query = f"""
        SELECT id FROM {table_name}
        ORDER BY id DESC 
        LIMIT 1
    """
    with connection.cursor() as cursor:
        cursor.execute(get_most_recent_order_id_query)
        most_recent_order_id = sql_functions.dictfetchall(cursor)[0]['id']
    return most_recent_order_id


def get_last_record_data(table_name):
    most_recent_order_id = get_most_recent_order_id(table_name)
    return select_one_row_by_id(most_recent_order_id, table_name)


def evaluate_all_available_data(dict_data: dict):
    for key in dict_data.keys():
        if not dict_data[key] and dict_data[key] != 0:
            return False, key
    return True, ""


class SQLHttpClass(GenericAPIView):
    def __init__(self, table_name, **kwargs):
        super().__init__(**kwargs)
        self.table_name = table_name

    def get_serializer_class(self):
        pass

    def sql_retrieve(self, request, *args, **kwargs):
        try:
            instance = select_one_row_by_id(kwargs['id'], self.table_name)
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except IndexError:
            return Response({"detail": "Not Found."},
                            status=status.HTTP_404_NOT_FOUND)

    def sql_destroy(self, request, *args, **kwargs):
        delete_one_row(kwargs['id'], self.table_name)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def sql_update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = select_one_row_by_id(kwargs['id'], self.table_name)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        instance = update_one_row(kwargs['id'], self.table_name, dict(request.data))
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def evaluate_null_numeric_data(self, dict_data, numeric_fields):
        for key in numeric_fields:
            if key in dict_data.keys():
                if not dict_data[key] and dict_data[key] != 0:
                    response = Response({'detail': f'field \'{key}\' cannot be empty.'},
                                        status=status.HTTP_400_BAD_REQUEST)
                    return False, response
        return True, ""

    def evaluate_positive_or_zero_numeric_data(self, dict_data, numeric_fields):
        for field in numeric_fields:
            if field in dict_data.keys():
                if dict_data[field] < 0:
                    response = Response({'detail': f'field \'{field}\' should be zero or positive.'},
                                        status=status.HTTP_400_BAD_REQUEST)
                    return False, response
        return True, ""

    def evaluate_positive_numeric_data(self, dict_data, numeric_fields):
        for field in numeric_fields:
            if field in dict_data.keys():
                if int(dict_data[field]) <= 0:
                    print('hello')
                    response = Response({'detail': f'field \'{field}\' should be positive.'},
                                    status=status.HTTP_400_BAD_REQUEST)
                    return False, response
        return True, ""
