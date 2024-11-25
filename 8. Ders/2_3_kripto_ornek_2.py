'''
Kendisine girilen 2 hafta parametresi
    arasında kalan haftaların (2022) yılı
    tüm paritelerin en düşük ve en yüksek
    değerlerini json olarak döndüren api yi yazınız.
http://localhost:5478/getir/30/50
    bu url e girildiğinde
    30 ile 50. haftalar arasındaki
    tüm paritelerin en düşük ve en yüksek
    değerlerini döndürecektir
'''

import sqlite3
from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)



@app.route("/getir/<int:hafta1>/<int:hafta2>")
def getir(hafta1, hafta2):
    bag = sqlite3.connect("kripto.vt")
    cursor = bag.cursor()
    sorgu = "SELECT parite, MIN(low), MAX(high) FROM parite " \
            "WHERE strftime('%W', date(otime)) " \
            "BETWEEN '{:02d}' AND '{:02d}' " \
            "GROUP BY parite".format(hafta1, hafta2)
    cursor.execute(sorgu)
    sonuc = cursor.fetchall()
    bag.close()
    return json.dumps(sonuc)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5478)
