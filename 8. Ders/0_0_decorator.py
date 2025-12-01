"""
En basit tabiriyle dekoratör; bir fonksiyonun kodunu değiştirmeden
    onun davranışını genişletmeye veya değiştirmeye yarayan bir yapıdır.

Dekoratörler çalışma mantığı:
    Bir fonksiyonu alırlar, içine "öncesi" veya "sonrası" için ekstra kod eklerler ve yeni fonksiyonu geri verirler.


Temel Sözdizimi (@ İşareti)
    Dekoratörleri genellikle fonksiyonun tepesinde @dekorator_adi şeklinde görürsün.
    Bu "Syntactic Sugar" (Sözdizimsel Şeker) denilen bir kısayoldur.
"""

# 1. Dekoratörümüzü tanımlayalım
def duyuru_yap(fonksiyon):
    def sarmalayici():  # Wrapper (Sarmalayıcı) fonksiyon
        print("--- Başlıyor! ---")
        fonksiyon()     # Asıl fonksiyon burada çalışır
        print("--- Bitti! ---")
    return sarmalayici

# 2. Dekoratörü kullanalım
@duyuru_yap
def selamla():
    print("Merhaba Dünya!")

# 3. Fonksiyonu çağıralım
selamla()