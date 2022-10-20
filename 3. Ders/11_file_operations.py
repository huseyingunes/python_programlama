dosya = open("metin.txt", 'r')

for satir in dosya:
    print(satir[:-1])
