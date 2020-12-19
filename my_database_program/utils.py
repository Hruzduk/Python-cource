import sqlite3
import pandas as pd

from my_database_program import config


def execute_query(query):
    conn = sqlite3.connect(config.DB_PATH)
    cursor = conn.cursor()

    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()


def get_table(table_name):
    """ Select table from database """
    db_con = sqlite3.connect(config.DB_PATH)
    df = pd.read_sql_query(f"""SELECT * FROM {table_name}""", db_con)
    db_con.close()
    return df


def show_all_tables():
    query = """
            SELECT name
            FROM sqlite_master 
            WHERE type='table' AND 
                  name != 'sqlite_sequence'
            """
    conn = sqlite3.connect(config.DB_PATH)
    cursor = conn.cursor()
    cursor.execute(query)
    result_list = cursor.fetchall()  # this is how it looks like: [('Films',), ('Some_nominations',)]
    result_list = [item[0] for item in result_list]  # this is how it looks now: ["Films", "Some_nominations"]
    return result_list


# def sort_df_by_value(df, value):                    Пока не реализовал этот функционал
#     if not (value in df.columns):
#         print(f"value={value} is not correct")
#     else:
#         res = df.sort_values(by=[value])
#         return res


def add_new_value(values, table):
    """
        We compare columns in db (COLUMNS OF TABLES) with columns in `values`.
        If they are the same, then we execute insert query
    """
    columns_db = set(config.COLUMNS_OF_TABLES[table][1:])  # we start from 1 because 0 is Id and we need to ignore it
    columns_val = set(values.keys())
    if columns_db == columns_val:
        query = f"""INSERT INTO {table} {tuple(values.keys())} VALUES {tuple(values.values())}"""
        execute_query(query)
        return "Done!"
    else:
        print(f"Wrong values={values}")
        return "Failed!"


def delete_value_from_table(tale_name, value_id):
    if isinstance(value_id, int):
        execute_query(f"""DELETE FROM {tale_name} WHERE Id = {value_id}""")
        return "Done!"
    else:
        print(f"Wrong value_id = {value_id}")
        return "Failed!"


# def save_df_to_csv(df, path):
#     df.to_csv(path, index=False)


# if __name__ == '__main__':
#
#     values = {
#         "Id": 123,
#         "Name": "Ololosh",
#         "Year": 1984
#     }
#     add_new_value(values=values, table="Films")
#
#     delete_value_from_table(tale_name="Films", value_id=100)
#     df = get_table("Films")
#     print(df)
#     df = sort_df_by_value(df, value="Year")
#     print(df)
