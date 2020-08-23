import sqlite3

class ItemModel:
    DATAFILE = 'data.db'
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def find_item_by_name(cls, name):
        connection = sqlite3.connect(cls.DATAFILE)
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE name=?"
        sql_result = cursor.execute(query, (name,))
        row = sql_result.fetchone()
        connection.close()
        if row:
            return cls(*row)
        return None
    
    @classmethod
    def find_item_all(cls):
        connection = sqlite3.connect(cls.DATAFILE)
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        sql_result = cursor.execute(query)
        items = sql_result.fetchall()
        connection.close()
        itemlist = [{"name":item[0], "price":item[1]} for item in items]
        return itemlist

    def insert(self):
        connection = sqlite3.connect(self.DATAFILE)
        cursor = connection.cursor()
        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (self.name, self.price))
        connection.commit()
        connection.close()
        # no return value

    def delete(self):
        connection = sqlite3.connect(self.DATAFILE)
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE name=?"  
        result = cursor.execute(query, (self.name,))
        connection.commit()
        connection.close()
        # no return value

    def update(self):
        connection = sqlite3.connect(self.DATAFILE)
        cursor = connection.cursor()
        query = "UPDATE items SET price=? WHERE name=?"
        result = cursor.execute(query, (self.price, self.name))
        # verify the result
        connection.commit()
        connection.close()