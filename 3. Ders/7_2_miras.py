class Dede:
    yas = 75

"""
yukarıdaki sınıfı miras alan sınıf
"""
class Baba(Dede):
    yas = 50

class Ogul(Baba):
    yas = 25

class Torun(Ogul):
    yas = 15

torun = Torun()
print(torun.yas)

"""
torunun dedesinin yaşı
"""

print(torun.__class__.__bases__[0].__bases__[0].__bases__[0].yas)
