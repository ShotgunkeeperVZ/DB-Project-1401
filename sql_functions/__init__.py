from django.db import connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


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
