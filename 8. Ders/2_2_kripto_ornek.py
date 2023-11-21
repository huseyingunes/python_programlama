'''
Kendisine girilen 2 ay parametresi
    arasında kalan tarihlerde
    tüm paritelerin en yüksek değerlerini
    json olarak döndüren api yi yazınız.
http://localhost:5478/getir/3/5
    bu url e girildiğinde
    mart ile mayıs ayları arasındaki
    tüm paritelerin en yüksek
    değerlerini döndürecektir
'''

import sqlite3
from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)


@app.route("/getir")
def getir():
    bag = sqlite3.connect("kripto.vt")
    cursor = bag.cursor()
    sorgu = "SELECT * FROM parite WHERE " \
            "(otime BETWEEN '2022-02-03' " \
            "AND '2022-02-04') " \
            "AND parite='AVAXUSDT'"
    cursor.execute(sorgu)
    sonuc = cursor.fetchall()
    bag.close()
    return sonuc


@app.route("/saglam_getir/<int:ay1>/<int:ay2>")
def saglam_getir(ay1, ay2):
    bag = sqlite3.connect("kripto.vt")
    cursor = bag.cursor()
    sorgu = "SELECT parite, MAX(close) FROM parite " \
            "WHERE strftime('%m', date(otime)) " \
            "BETWEEN '{:02d}' AND '{:02d}' " \
            "GROUP BY parite".format(ay1, ay2)
    cursor.execute(sorgu)
    sonuc = cursor.fetchall()
    bag.close()
    return json.dumps(sonuc)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5478)
