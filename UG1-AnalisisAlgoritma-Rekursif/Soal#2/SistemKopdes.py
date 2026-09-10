# import ini jangan dihapus/diedit yak
import random

def totalPenjualan(data, n):
    if n == 0:  
        return 0
    return data[n-1][1] + totalPenjualan(data, n-1) #data[n-1][1] = mengambil nilai penjualan dari elemen terakhir, n adalah jumlah elemen yang sedang diproses

# Fungsi rekursif untuk mencari penjualan tertinggi
def penjualanTertinggi(data, n):
    if n == 1:  # base case
        return data[0]
    
    tertinggi_sebelum = penjualanTertinggi(data, n-1)
    if data[n-1][1] > tertinggi_sebelum[1]:
        return data[n-1]
    else:
        return tertinggi_sebelum

# Fungsi iteratif untuk menghitung jumlah barang di atas rata-rata
def diAtasRataRata(penjualan, rataRata):
    count = 0
    for jumlah in penjualan.values():
        if jumlah > rataRata:
            count += 1
    return count

# Program Utama - Jangan dihapus/diedit yak
angka = int(input("NIM: "))
random.seed(angka)

barang = [
    "Beras",
    "Minyak",
    "Gula",
    "Telur",
    "Kopi",
    "Teh"
]

penjualan = {}

for namaBarang in barang:
    penjualan[namaBarang] = random.randint(100, 500)

data = list(penjualan.items())
n = len(data)

print("\n===== Data Penjualan =====")
for namaBarang, jumlah in penjualan.items():
    print(namaBarang, ":", jumlah)

total = totalPenjualan(data, n)
tertinggi = penjualanTertinggi(data, n)
rataRata = total / n
jumlahDiAtasRataRata = diAtasRataRata(penjualan, rataRata)

print("\n===== Hasil Analisis =====")
print("Total penjualan        :", total)
print("Penjualan tertinggi    :", tertinggi[0], "(", tertinggi[1], ")")
print("Rata-rata penjualan    :", round(rataRata, 2))
print("Di atas rata-rata      :", jumlahDiAtasRataRata, "barang")