"""
https://leetcode.com/problems/largest-number/description/
Given a list of non-negative integers nums,
arrange them such that they form the largest
number and return it.

Since the result may be very large,
so you need to return a string instead of an integer.

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
"""

def cevir(sayi, hane):
    eksik_hane = hane - len(str(sayi))
    return str(sayi) + (str(sayi)[-1]*eksik_hane)

_sayi_listesi = [3, 30, 34, 5, 9, 96, 823497]
sayi_listesi = [3, 30, 34, 5, 9, 96, 823497]
max_hane = 0
for i in sayi_listesi:
    max_hane = len(str(i)) if len(str(i)) > max_hane else max_hane

for i, sayi in enumerate(sayi_listesi):
    sayi_listesi[i] = cevir(sayi, max_hane)


Z = [x for _,x in sorted(zip(sayi_listesi, _sayi_listesi))]
for i in Z[::-1]:
    print(i, end="", sep="")






