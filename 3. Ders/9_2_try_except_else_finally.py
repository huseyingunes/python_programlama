x = 7
try:
    y = 5 + x
except:
    print("Hata")
else:
    print("Hata yok yola devam")
print("------------------------------------")
x = "asd"
try:
    y = 5 + x
except:
    print("Hata")
finally:
    print("Ben her sekilde calisirim")