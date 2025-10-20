x = "asd"
#y = 5 + x
try:
    y = 5 + x
except TypeError as e:
    print("Tip Hatası : 'int' and 'str' :", e)
except:
    print("Bilinmeyen Hata")

print("Hata da olsa devam")