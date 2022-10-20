dosya = open("kod.txt", 'w')
print("print('efsane python')", file=dosya)
dosya.close()

dosya = open("kod.txt", 'r')
satir = dosya.readline()
eval(satir)
