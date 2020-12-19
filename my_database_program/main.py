import sys
import json
from my_database_program.utils import show_all_tables, get_table, add_new_value, delete_value_from_table


def main():
    actions = {
        1: "show_table",
        2: "add_record_to_table",
        3: "delete_record_from_table",
        4: "import_table_to_csv"
    }
    print("Welcome to Nicolas Cage database. Please choose the next action:")
    for k, v in actions.items():
        print(f"{k} : {v}")
    input_value = input("Your choice: ")

    try:
        action = actions[int(input_value)]
    except (ValueError, KeyError):
        # ValuerError -- для случаев если у нас не получилос конвертнуть в инт
        # KeyError --  для случаев если input_value отсутствует в actions
        print("There is no such action. Exiting...")
        sys.exit()  # close program at all

    tables = show_all_tables()
    if action == "show_table":
        print("Here is the list of all tables:")
        print(tables)
        table_name = input("Which table do you want to see: ")
        while True:
            if table_name in tables:
                break
            else:
                table_name = input("Wrong table name. Try more: ")
        df = get_table(table_name)
        print(df)

    elif action == "add_record_to_table":
        example = {
            "Name": "Name",
            "Year": 2000
        }
        print("Here is the example how input should look like:")
        print(example)
        while True:  # check if table name exists
            table_name = input("Enter table name: ")
            if table_name in tables:
                break
            else:
                print("Wrong table name.")
        while True:  # check the values format. It should be only json in example
            values = input("Enter values in dict format: ")
            values = values.replace("'", '"')  # исправляем одинарные скобки на двойные
            try:
                values = json.loads(values)  # example: {"Name": "123", "Year": 1984}
                                             # {"Type": "BAFTA", "Year": 1984, "Category": "Best actor", "Status": "WON", "FilmId": 42}
                res = add_new_value(values=values, table=table_name)
                # trying to insert records to db. If the column names wrong, we will fail
                if res == "Done!":
                    print("Records successfully inserted to DB")
                    break
                else:
                    continue
            except json.decoder.JSONDecodeError:
                print(f"Wrong values={values}")
                continue

    elif action == "delete_record_from_table":
        while True:
            try:
                id_ = int(input("Enter film id which you want to delete: "))
                res = delete_value_from_table(tale_name="Films", value_id=id_)
                if res == 'Done!':
                    break
                else:
                    continue
            except (ValueError, KeyError):
                print("Wrong id, try more...")

    elif action == "import_table_to_csv":
        print(f"Here is the list of available tables: {tables}")
        table_name = input("Which table would you like to save to csv? ")
        while True:
            if table_name in tables:
                break
            else:
                table_name = input("Wrong table name. Try more: ")
        df = get_table(table_name)
        save_path = input("Enter path to file: ")
        while True:
            try:
                df.to_csv(save_path, index=False)
                break
            except FileNotFoundError:
                save_path = input("Wrong save path. Try more: ")


if __name__ == '__main__':
    main()
