"""
b.vt veri tabanını oluşturunuz

iris isminde bir tablo oluşturunuz

bu tabloyu iris.data dosyasındaki verilere uygun şekilde alanlar
oluşturunuz

iris.data dosyasındaki verileri iris tablosuna ekleyiniz
"""

import csv
import sqlite3

bag = sqlite3.connect("b.vt")
cursor = bag.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS iris "
               "(id INTEGER NOT NULL PRIMARY KEY,"
               "species TEXT, sepal_length FLOAT, "
               "sepal_width FLOAT, "
               "petal_length FLOAT, "
               "petal_width FLOAT)")


with open('iris.data', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute("INSERT INTO iris (species, sepal_length, sepal_width, petal_length, petal_width) "
                       "VALUES(?, ?, ?, ?, ?)", (row["species"], row["sepal_length"], row["sepal_width"], row["petal_length"], row["petal_width"]))
bag.commit()
bag.close()