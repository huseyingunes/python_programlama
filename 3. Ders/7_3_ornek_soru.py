class MaximumPathSum18ProjectEuler:
    sayi = [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65]]

    def coz(self):
        for i in range(len(self.sayi)-2, -1, -1):
            for s in range(len(self.sayi[i])):
                self.sayi[i][s] += max(self.sayi[i+1][s],self.sayi[i+1][s+1])

    def __str__(self):
        return str(self.sayi[0][0])

nesne = MaximumPathSum18ProjectEuler()
nesne.coz()
print("En Yüksek Toplam =", nesne)