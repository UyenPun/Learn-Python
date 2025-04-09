import sqlite3

# connect:
conn = sqlite3.connect('car.db')

c = conn.cursor()

sql_create_table = """
    CREATE TABLE cars (
        name TEXT
    )

"""