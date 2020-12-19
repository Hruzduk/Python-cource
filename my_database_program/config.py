import os

COLUMNS_OF_TABLES = {
    'Some_nominations': ['Id', 'Type', 'Year', 'Category', 'Status', 'FilmId'],
    'Films': ['Id', 'Name', 'Year']
}

APP_DIR = os.getcwd()
DATA_DIR = os.path.join(APP_DIR, "data")

DB_PATH = os.path.join(DATA_DIR, "Nicolas_Cage.db")



