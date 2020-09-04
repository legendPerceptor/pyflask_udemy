import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table_query = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username text, password text)"
cursor.execute(create_table_query)

create_table_query = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, price real)"
cursor.execute(create_table_query)


cursor.execute("INSERT INTO items (name, price) VALUES ('test',10.99)")
cursor.execute("INSERT INTO users (username, password) VALUES ('jose', 1234)")

connection.commit()
connection.close()