x = "asd"

try:
    y = 5 + x
except TypeError:
    print("Tip Hatası : 'int' and 'str'")
except:
    print("Bilinmeyen Hata")
