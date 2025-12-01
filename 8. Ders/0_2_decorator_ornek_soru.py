"""

Görev: "Sadece Sayılar" Dekoratörü
Diyelim ki bir matematik kütüphanesi yazıyorsun. Fonksiyonlarının sadece sayı
    (int veya float) kabul etmesini, eğer araya bir metin (string) veya
    başka bir tür karışırsa işlemi durdurup bir uyarı vermesini istiyorsun.

İstenenler:

@sadece_sayilar adında bir dekoratör yaz.

Bu dekoratör, süslediği fonksiyona gelen argümanları (*args) kontrol etsin.

Eğer bütün argümanlar sayı ise asıl fonksiyon çalışsın ve sonucu döndürsün.

Eğer herhangi biri sayı değilse (örneğin "5" gibi bir string ise)
    asıl fonksiyonu çalıştırmasın ve geriye "Hata: Lütfen sadece sayı giriniz!"
    metnini döndürsün.

"""

# 1. Dekoratörü buraya yaz
def sadece_sayilar(fonksiyon):
    # Burayı doldur...
    pass

# 2. Dekoratörü uygula
@sadece_sayilar
def topla(a, b, c):
    return a + b + c

# 3. Testler
print(topla(5, 10, 20))       # Beklenen çıktı: 35
print(topla(5, "on", 20))     # Beklenen çıktı: Hata: Lütfen sadece sayı giriniz!
































# Cevap

def sadece_sayilar(fonksiyon):
    def sarmalayici(*args):
        # 1. Gelen argümanları (args) tek tek kontrol et
        for arguman in args:
            # isinstance komutu, bir verinin tipini kontrol eder
            # Eğer sayı (int veya float) DEĞİLSE hemen dur ve hata dön.
            if not isinstance(arguman, (int, float)):
                return "Hata: Lütfen sadece sayı giriniz!"

        # 2. Döngüden sağ salim çıkıldıysa hepsi sayıdır.
        # Asıl fonksiyonu çalıştır ve sonucu döndür.
        return fonksiyon(*args)

    return sarmalayici


# --- Test Edelim ---

@sadece_sayilar
def topla(a, b, c):
    return a + b + c


# Senaryo 1: Hepsi sayı (Başarılı)
print("Senaryo 1:", topla(5, 10, 20))

# Senaryo 2: Araya string karışmış (Hata Yakalama)
print("Senaryo 2:", topla(5, "on", 20))



"""
if not all(isinstance(x, (int, float)) for x in args):
    return "Hata..."
"""