"""
fibonacci sayılarını bulan program yazınız.
"""

a = 1
b = 1
print(a)
print(b)
for i in range(10):
    a, b = b, a + b
    print(b)
    