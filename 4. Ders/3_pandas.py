import pandas as pd

veri = pd.read_csv("iris.data")

print(veri.head())

print(veri.columns)

print(veri[3:5])

veri = veri.sort_values(by="sepal_length")
print(veri.head())

toplam_veri = veri["sepal_length"].sum()
ortalama_veri = veri["sepal_length"].mean()
ortanca_veri = veri["sepal_length"].median()

print("Sum:", toplam_veri,
      "\nMean:", ortalama_veri,
      "\nMedian:", ortanca_veri)

## https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
