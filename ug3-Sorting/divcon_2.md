# Pengolahan Nilai Mahasiswa

## Deskripsi

Program ini dibuat untuk mengolah data nilai **UG (Ujian/UG)** dari 5 mahasiswa menggunakan konsep **Divide and Conquer**.

Setiap mahasiswa memiliki **5 nilai UG**. Program akan menghitung rata-rata nilai setiap mahasiswa, kemudian mengurutkan mahasiswa berdasarkan rata-rata nilai menggunakan algoritma **Merge Sort**.

Setelah itu, program menghitung rata-rata keseluruhan mahasiswa dan membagi mahasiswa menjadi dua kelompok:

* **Di Atas / Sama Dengan Rata-rata**
* **Di Bawah Rata-rata**

Setiap kelompok diberikan nomor urut mulai dari 1.

---

## Data Mahasiswa

Program menggunakan data berikut:

| No | Nama  | Nilai UG               |
| -- | ----- | ---------------------- |
| 1  | Andi  | `[80, 75, 90, 70, 85]` |
| 2  | Budi  | `[60, 65, 70, 55, 60]` |
| 3  | Citra | `[90, 85, 95, 88, 92]` |
| 4  | Deni  | `[70, 75, 65, 72, 68]` |
| 5  | Eka   | `etc` |

---

## Tujuan Program

Program memiliki beberapa tujuan:

1. Menyimpan data mahasiswa dan 5 nilai UG.
2. Menghitung rata-rata nilai masing-masing mahasiswa.
3. Menghitung rata-rata keseluruhan mahasiswa.
4. Mengurutkan mahasiswa berdasarkan rata-rata nilai dari **tertinggi ke terendah**.
5. Mengelompokkan mahasiswa berdasarkan rata-rata keseluruhan.
6. Memberikan nomor urut pada setiap kelompok.

---

## Konsep Divide and Conquer

Program menggunakan algoritma **Merge Sort**, yang merupakan salah satu contoh algoritma Divide and Conquer.

Divide and Conquer terdiri dari tiga tahap utama:

### 1. Divide

Data mahasiswa dibagi menjadi dua bagian.

Contoh:

```text
[Andi, Budi, Citra, Deni, Eka]

              ↓

[Andi, Budi]     [Citra, Deni, Eka]
```

Pembagian dilakukan terus secara rekursif sampai setiap bagian hanya memiliki satu data.

### 2. Conquer

Setiap bagian kecil kemudian diurutkan secara rekursif berdasarkan rata-rata nilai mahasiswa.

### 3. Combine

Bagian-bagian yang sudah terurut kemudian digabungkan kembali sehingga menghasilkan data yang terurut.

Contoh:

```text
[Andi] [Budi] → [Andi, Budi]

[Citra] [Deni] [Eka] → [Citra, Eka, Deni]

              ↓

[ Citra, Eka, Andi, Deni, Budi ]
```

Urutan tersebut berdasarkan rata-rata nilai dari yang terbesar ke yang terkecil.

---

Jika:

```text
Rata-rata keseluruhan = 50
```

---

## Pengelompokan Mahasiswa

Mahasiswa dengan rata-rata **lebih besar atau sama dengan 50** masuk ke kelompok:

```text
DI ATAS / SAMA DENGAN RATA-RATA
```

Sedangkan mahasiswa dengan rata-rata **kurang dari 50** masuk ke kelompok:

```text
DI BAWAH RATA-RATA
```

Hasil pengelompokan:

### Di Atas / Sama Dengan Rata-rata

```text
1. Citra - 90
2. Eka   - 84
3. Andi  - 80
```

### Di Bawah Rata-rata

```text
1. Deni - 70
2. Budi - 62
```
---
Contoh hasil:

```text
Rata-rata keseluruhan: 76.84

=== DI ATAS / SAMA DENGAN RATA-RATA ===
1 . Citra - Nilai: [90, 85, 95, 88, 92] - Rata-rata: 90.0
2 . Eka - Nilai: [85, 80, 78, 90, 87] - Rata-rata: 84.0
3 . Andi - Nilai: [80, 75, 90, 70, 85] - Rata-rata: 80.0

=== DI BAWAH RATA-RATA ===
1 . Deni - Nilai: [70, 75, 65, 72, 68] - Rata-rata: 70.0
2 . Budi - Nilai: [60, 65, 70, 55, 60] - Rata-rata: 62.0
```

Program TIDAK BOLEH menggunakan fungsi sorting bawaan seperti `sort()` atau `sorted()`, proses pengurutan dilakukan secara manual menggunakan konsep **Divide and Conquer**.
