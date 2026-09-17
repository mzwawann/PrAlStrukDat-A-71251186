# PT Sorting — Pengurutan Data Mahasiswa

## Deskripsi Soal

Diberikan sejumlah data mahasiswa yang berisi **NIM** dan **Nama**. Tugas yang harus dikerjakan adalah mengurutkan data mahasiswa berdasarkan kriteria tertentu **tanpa menggunakan fungsi `sorted`** atau fungsi pengurutan bawaan Python lainnya (seperti `.sort()` pada list).

## Data Mahasiswa

Data mahasiswa tersimpan dalam bentuk list of list, dengan struktur sebagai berikut:

```python
data = [
    ['NIM', 'Nama'],
    ['71241135', 'Marvin Patric Theodorus'],
    ['71251202', 'Brillyan Herlambang Anugerah Seleng'],
    # ... dst.
]
```

Setiap elemen data mahasiswa memiliki format:
- **Index 0**: NIM (Nomor Induk Mahasiswa) — bertipe `str`
- **Index 1**: Nama Lengkap Mahasiswa — bertipe `str`
- **Index 2**: Nilai Presensi — bertipe `int` (ditambahkan secara dummy)

## Fungsi yang Tersedia

### `presensi_dummy(data)`
Menambahkan nilai presensi dummy (random antara 70–100) ke setiap elemen data mahasiswa.

### `acak_data(data)`
Mengacak urutan data mahasiswa secara acak menggunakan `random.shuffle()`.

### `show_data(data)`
Menampilkan data mahasiswa dalam bentuk tabel yang rapi.

## Tugas

1. Buat fungsi `sort_by(data, index, rev=False)` yang mengurutkan data mahasiswa berdasarkan kolom yang ditentukan:
   - `"nim"` — berdasarkan NIM
   - `"nama"` — berdasarkan Nama
   - `"presensi"` — berdasarkan nilai Presensi
2. Parameter `rev`:
   - `False` → pengurutan ascending (menaik)
   - `True` → pengurutan descending (menurun)
3. **Dilarang keras menggunakan fungsi `sorted()` atau metode `.sort()`** untuk mengurutkan data. Implementasikan algoritma pengurutan secara manual (misalnya: Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, dll).

## Contoh Pemanggilan

```python
sort_by(data, "presensi")       # Urutkan berdasarkan presensi (ascending)
sort_by(data, "nim", rev=True)  # Urutkan berdasarkan NIM (descending)
sort_by(data, "nama")           # Urutkan berdasarkan nama (ascending)
```

## Contoh Output

```
====================================================
|   NIM   |          Nama           | Presensi |
====================================================
| 71241089|   Edbert Fernando       |   85     |
| 71241104|   Morets Hayasi Ninef   |   92     |
| ...     |   ...                   |   ...    |
====================================================
```

## File Struktur Proyek

```
PT-Sorting/
├── README.md          # Dokumentasi soal dan panduan
├── dataMahasiswa.py   # Data mahasiswa (list of list)
├── fungsiMahasiswa.py # Fungsi helper (presensi, acak, tampil)
└── SortMahasiswa.py   # Skrip utama (implementasi sorting)
```

## Ketentuan Tambahan

- Pastikan data yang ditampilkan setelah pengurutan masih memuat seluruh mahasiswa tanpa ada yang terlewat.
- Fungsi `show_data()` hanya menampilkan 3 kata pertama dari nama mahasiswa (berdasarkan spasi).
- Nilai presensi dihasilkan secara random antara 70 hingga 100 setiap program dijalankan.
