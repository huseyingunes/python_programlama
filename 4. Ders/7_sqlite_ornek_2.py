"""
https://jsonplaceholder.typicode.com/todos
adresindeki tüm yapılacakları bir sqlite
veri tabanı oluşturup içinde uygun bir tabloya
ekleyiniz
"""
import csv
import sqlite3
import urllib.request
import json

bag = sqlite3.connect("c.vt")
cursor = bag.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS todos "
               "(id INTEGER NOT NULL PRIMARY KEY,"
               "userId INT, title TEXT, "
               "completed BOOLEAN)")


with urllib.request.urlopen("https://jsonplaceholder.typicode.com/todos") as url:
    datas = json.loads(url.read().decode())
    for data in datas:
        cursor.execute("INSERT INTO todos (userId, title, completed) "
                       "VALUES(?, ?, ?)", (data["userId"], data["title"], data["completed"]))

bag.commit()
bag.close()