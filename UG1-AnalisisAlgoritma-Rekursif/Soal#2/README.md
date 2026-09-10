# **Sistem KopDes Merah Putih**

Tedy adalah seorang programmer yang sedang mengembangkan sebuah sistem sederhana untuk membantu manajer KopDes Merah Putih menganalisis data penjualan.

Setiap hari, KopDes tersebut mencatat jumlah barang yang berhasil terjual. Data penjualan tersebut disimpan dalam sebuah **dictionary berisi nama barang dan jumlah penjualan**. Sebagai contoh:

```python
penjualan = {
    "Beras": 120,
    "Minyak": 250,
    "Gula": 175,
    "Telur": 300,
    "Kopi": 225,
    "Teh": 150
}
```

Manajer KopDes ingin mengetahui beberapa informasi dari data tersebut, yaitu:

- Total seluruh barang yang terjual.
- Nama barang dan jumlah penjualan tertinggi.
- Jumlah barang yang memiliki penjualan di atas rata-rata.

Untuk menghitung **total penjualan** dan **nilai penjualan tertinggi**, Tedy menggunakan **fungsi rekursif**. Fungsi rekursif adalah fungsi yang memanggil dirinya sendiri untuk menyelesaikan permasalahan yang lebih kecil hingga mencapai kondisi berhenti (*base case*).

Sedangkan untuk menghitung **jumlah barang yang memiliki penjualan di atas rata-rata**, Tedy menggunakan algoritma iteratif dengan memeriksa setiap data penjualan yang terdapat dalam dictionary.

Tedy kemudian meminta bantuan kalian untuk menyelesaikan program tersebut. Program tersebut memiliki 3 fungsi utama:

1. `totalPenjualan()` untuk menghitung total seluruh penjualan menggunakan rekursi.
2. `penjualanTertinggi()` untuk mencari nama barang dan jumlah penjualan terbesar menggunakan rekursi.
3. `diAtasRataRata()` untuk menghitung jumlah barang yang memiliki penjualan di atas rata-rata menggunakan pendekatan iteratif.


## Ketentuan

1. Fungsi `totalPenjualan()` **WAJIB menggunakan fungsi rekursif** dan tidak boleh menggunakan perulangan `for` atau `while`.
2. Fungsi `penjualanTertinggi()` **WAJIB menggunakan fungsi rekursif** dan tidak boleh menggunakan perulangan `for` atau `while`.
3. Fungsi `diAtasRataRata()` menggunakan **pendekatan iteratif** dengan perulangan `for` atau `while`.
4. **Jangan mengubah** struktur utama fungsi yang telah diberikan.


## Penjelasan Parameter

Terdapat 3 parameter yang digunakan pada fungsi-fungsi dalam program ini: 

1. `penjualan` = Tipe data **Dictionary**, berisi nama barang sebagai `key` dan jumlah penjualan sebagai `value`.
2. `data` = Tipe data **List**, berisi pasangan nama barang dan jumlah penjualan yang digunakan untuk proses rekursif.
3. `n` = Tipe data **Integer**, menunjukkan jumlah data penjualan yang sedang diproses.
4. `rataRata` = Tipe data **Float**, menunjukkan nilai rata-rata penjualan yang digunakan untuk menentukan barang yang memiliki penjualan di atas rata-rata.


## Test Case

Anda akan diminta memasukkan NIM, dan test case akan dirandom berdasarkan NIM Anda. Jadi, setiap orang akan memiliki test case yang berbeda.

Contoh:

```text
NIM: 71230986

===== Data Penjualan =====
Beras : 465
Minyak : 227
Gula : 399
Telur : 351
Kopi : 440
Teh : 388

===== Hasil Analisis =====
Total penjualan        : 2270
Penjualan tertinggi    : Beras ( 465 )
Rata-rata penjualan    : 378.33
Di atas rata-rata      : 4 barang
```

## Catatan Tambahan

- Mohon **BACA SOAL** terlebih dahulu. Apabila masih tidak jelas, baru ditanyakan kepada asdos.
- Fungsi `totalPenjualan()` dan `penjualanTertinggi()` **WAJIB menggunakan rekursi**.
- Fungsi `diAtasRataRata()` **WAJIB menggunakan perulangan**.
- Tidak diperbolehkan menggunakan fungsi bawaan seperti `sum()`, `max()`, atau fungsi bawaan sejenis untuk menyelesaikan bagian yang diminta.
- Perhatikan penggunaan **key** dan **value** pada dictionary.
- Perhatikan kembali *base case* dan *recursive case* pada fungsi rekursif.
- Program harus dapat menghasilkan output yang sesuai dengan format yang telah ditentukan.
- **Anda harus dapat menjelaskan alur kerja program Anda dengan benar**.
