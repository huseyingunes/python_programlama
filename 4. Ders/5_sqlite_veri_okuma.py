import sqlite3

bag = sqlite3.connect("a.vt")
# Tabloya bağlanıyoruz.

cursor = bag.cursor()

cursor.execute("SELECT * FROM kitap")
# Tüm verileri seçiyoruz.

veriler = cursor.fetchall()
# Verileri alıyoruz.

for veri in veriler:
    print(veri)
    # Verileri yazdırıyoruz.
    
bag.close()