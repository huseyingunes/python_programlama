'''
A palindromic number reads the same both ways. The largest palindrome
made from the product of two-digit numbers is
9009 = 91 * 99

Find the largest palindrome made from the product of two
    3-digit
numbers.
'''
palindrom_mu = lambda sayi: True if str(sayi) == str(sayi)[::-1] else False
en_buyuk_palindrom = 0
for i in range(100, 1000):
    for s in range(100, 1000):
        en_buyuk_palindrom = i * s if palindrom_mu(i * s) and (i*s) > en_buyuk_palindrom else en_buyuk_palindrom

print("En büyük palindrom : ", en_buyuk_palindrom)
