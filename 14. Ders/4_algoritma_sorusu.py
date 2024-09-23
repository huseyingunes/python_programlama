"""
Corro, bilge bir halk kahramanıdır.
Bilgeliğini de çoğunlukla kitaplara borçludur.
Corro bilgeliğini arttırmak için 50 tane kitap daha okumaya karar vermiştir.
Corro bu 50 kitabı bilgeliğine en çok katkıyı sağlayacak şekilde seçmek istiyor.
Fakat Corro biraz sakar ve rafın ortasından bir kitap alırkan kitapları döküyor.
Bunun için rafın en sağından ve en solundan kitap alabiliyor(Yani bir kitabı alması için o kitabın sağındaki ya da solundaki bütün kitapları önceden almış olması gerekiyor).
Corro’nun kitaplığında 60 tane raf var.
Kitaplıkta her rafta 20 kitap var.
Bu 20 kitabında rastgele bilgelik değerleri var.
Verilen kitaplık bilgisi için Corro’nun bilgeliğini en fazla ne kadar arttırabileceğini bulan bir program yazınız.

"""




import random
import numpy as np
import time
import os
import json
import copy

def get_random_bookshelf():
    bookshelf = []
    for i in range(60):
        bookshelf.append([])
        for j in range(20):
            bookshelf[i].append(random.randint(1, 100))
    return bookshelf

def get_bookshelf():
    with open("bookshelf.txt", "r") as file:
        bookshelf = json.load(file)
    return bookshelf

def get_bookshelf_value(bookshelf):
    value = 0
    for i in range(60):
        for j in range(20):
            value += bookshelf[i][j]
    return value

