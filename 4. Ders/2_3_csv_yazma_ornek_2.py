"""
iris.data dosyasında yer alan ondalıklı verileri
tam sayıya yuvarlayarak iris_tamsayi.csv dosyasına yazınız.
"""








import csv

basliklar = None
veriler = []

with open('iris.data', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for i, row in enumerate(reader):
        if i == 0:
            basliklar = row.keys()
        veriler.append([round(float(row["sepal_length"])),
                        round(float(row["sepal_width"])),
                        round(float(row["petal_length"])),
                        round(float(row["petal_width"])),
                        row["species"]])

with open('iris_tamsayi.csv',
          'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(basliklar)
    writer.writerows(veriler)