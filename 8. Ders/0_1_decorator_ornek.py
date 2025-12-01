import time


def zaman_olcer(fonksiyon):
    def sarmalayici(*args, **kwargs):
        baslangic = time.time()  # Kronometreyi başlat

        sonuc = fonksiyon(*args, **kwargs)  # Asıl fonksiyonu çalıştır

        bitis = time.time()  # Kronometreyi durdur
        print(f"{fonksiyon.__name__} fonksiyonu {bitis - baslangic:.4f} saniye sürdü.")

        return sonuc  # Fonksiyonun orijinal sonucunu geri döndür

    return sarmalayici


@zaman_olcer
def agir_islem_yap(sayi):
    time.sleep(1)  # İşlemi simüle etmek için 1 saniye bekletiyoruz
    return sayi * 2


# Test edelim
print(agir_islem_yap(10))