import csv
import sqlite3

COLUMNS_OF_TABLES = {'Some_nominations': ('Id', 'Type', 'Year'),
                     'Films': ('Id', 'Name', 'Year')
                     }


def _execute_from_base(query):
    conn = sqlite3.connect("../data/Nicolas_Cage.db")
    cursor = conn.cursor()
    cursor.execute(query)
    result_list = cursor.fetchall()
    return result_list


def get_data_from_table(table, columns="*", filters=dict()):
    data = [COLUMNS_OF_TABLES[table]]
    where_filter = ''
    if filters:
        for key in filters.keys():
            where_filter = create_where(where_filter, key, filters[key])
    query = f'''SELECT {columns} FROM {table}
                {where_filter}'''
    data += _execute_from_base(query)
    return data


def create_where(where_filter, key, value):
    if len(where_filter) > 0:
        where_filter += f' and {key} = {value}'
    else:
        where_filter += f'where {key} = {value}'
    return where_filter


def to_csv(data, file_name):
    with open(file_name, mode='w', newline='') as data_file:
        data_writer = csv.writer(data_file, delimiter=',', quotechar='"'
                                 )
        data_writer.writerows(data)




to_csv(get_data_from_table(table="Some_nominations"), file_name='../data/test.csv')
#
#
# def get_nominations(columns="*", filters=dict()):
#     where_filter = ''
#     if filters:
#         for key in filters.keys():
#             where_filter = create_where(where_filter, key, filters[key])
#     query = f'''SELECT {columns} FROM Some_nominations
#                 {where_filter}'''
#     print(query)
#     return _execute_from_base(query)


print()

