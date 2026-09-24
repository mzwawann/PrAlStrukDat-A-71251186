# Data mahasiswa dan 5 nilai UG
mahasiswa = [
    {"nama": "Andi", "nilai": [80, 75, 90, 70, 85]},
    {"nama": "Budi", "nilai": [60, 65, 70, 55, 60]},
    {"nama": "Citra", "nilai": [90, 85, 95, 88, 92]},
    {"nama": "Deni", "nilai": [70, 75, 65, 72, 68]},
    {"nama": "Eka", "nilai": [85, 80, 78, 90, 87]},
    {"nama": "Fajar", "nilai": [65, 70, 68, 60, 72]},
    {"nama": "Gina", "nilai": [88, 92, 85, 90, 87]},
    {"nama": "Hadi", "nilai": [75, 80, 70, 78, 72]},
    {"nama": "Intan", "nilai": [55, 60, 65, 58, 62]},
    {"nama": "Joko", "nilai": [78, 82, 75, 80, 85]}
]


# Menghitung rata-rata nilai setiap mahasiswa
for mhs in mahasiswa:
    mhs["rata_rata"] = sum(mhs["nilai"]) / len(mhs["nilai"])


# Divide and Conquer - Merge Sort
def merge_sort(data): 
    if len(data) <= 1:  
        return data  
 
    tengah = len(data) // 2  
    kiri = data[:tengah]  
    kanan = data[tengah:]  
 
    kiri = merge_sort(kiri)  
    kanan = merge_sort(kanan)  
 
    return merge(kiri, kanan)


def merge(kiri, kanan): 
    hasil = []  

    i = 0  
    j = 0

    while i < len(kiri) and j < len(kanan):  
        if kiri[i]["rata_rata"] >= kanan[j]["rata_rata"]:  
            hasil.append(kiri[i])  
            i += 1  
        else:  
            hasil.append(kanan[j])  
            j += 1  

    while i < len(kiri):
        hasil.append(kiri[i])  
        i += 1 

    while j < len(kanan):
        hasil.append(kanan[j])  
        j += 1

    return hasil


# Menghitung rata-rata keseluruhan
total_rata_rata = 0

for mhs in mahasiswa:
    total_rata_rata += mhs["rata_rata"]

rata_rata_keseluruhan = total_rata_rata / len(mahasiswa)

# Mengurutkan mahasiswa menggunakan Merge Sort
mahasiswa_urut = merge_sort(mahasiswa)


# Menampilkan hasil rata-rata keseluruhan
print("Rata rata keseluruhan:", rata_rata_keseluruhan)

print("\n=== DI ATAS / SAMA DENGAN RATA-RATA ===")

nomor = 1

for mhs in mahasiswa_urut:
    if mhs["rata_rata"] >= rata_rata_keseluruhan:
        print(
            nomor,
            ".",
            mhs["nama"],
            "- Nilai:",
            mhs['nilai'],
            "- Rata-rata:",
            mhs["rata_rata"]
        )
        nomor += 1

# Tampilkan List di atas / sama dengan rata-rata


print("\n=== DI BAWAH RATA-RATA ===")

nomor = 1

for mhs in mahasiswa_urut:
    if mhs["rata_rata"] < rata_rata_keseluruhan:
        print(
            nomor,
            ".",
            mhs["nama"],
            "- Nilai:",
            mhs['nilai'],
            "- Rata-rata:",
            mhs["rata_rata"]
        )
        nomor += 1

# Tampilkan List di bawah rata-rata