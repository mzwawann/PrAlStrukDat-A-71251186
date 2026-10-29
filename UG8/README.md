# UG8: Pengolahan String dan File - Manajemen Nasabah

Praktikum ini menguji pemahaman mengenai penanganan file teks terstruktur, meliputi pembacaan (deserialisasi) dan pembaruan (serialisasi) berkas JSON serta penulisan data tabular ke format CSV.

---

## Struktur Berkas

* `README.md`: Panduan alur pengerjaan dan spesifikasi teknis fungsi.
* `nasabah.json`: Berkas data awal yang berisi daftar rekening nasabah.
* `soal_nasabah.py`: Berkas kode program yang wajib dilengkapi.
* `test_nasabah.py`: Skrip pengujian otomatis (*auto-grader*) untuk memeriksa kebenaran fungsi dan menghitung skor akhir.

---

## Alur Pengerjaan

1. Buka berkas `soal_nasabah.py`.
2. Lengkapi ketiga fungsi di dalamnya: `baca_nasabah()`, `update_saldo()`, dan `ekspor_ke_csv()` sesuai spesifikasi teknis di bawah.
3. Jangan mengubah nama fungsi maupun urutan parameternya.
4. Jalankan pengujian mandiri di terminal melalui perintah:
   ```bash
   python test_nasabah.py
   ```
5. Periksa hasil di terminal. Jika terdapat pengujian yang gagal (`FAIL`), baca petunjuk pada bagian `Solusi` untuk memperbaiki kode Anda.
6. Kumpulkan berkas `soal_nasabah.py` setelah mendapatkan skor `100 / 100`.

---

## Spesifikasi Fungsi

### 1. `baca_nasabah(filepath: str) -> list[dict]`
* **Tujuan**: Membaca berkas JSON dari path `filepath` dan mengubahnya menjadi struktur data Python (`list` berisi `dict`).
* **Proses**:
  * Buka berkas menggunakan mode baca (`"r"`).
  * Lakukan deserialisasi menggunakan `json.load()`.
* **Return Value**: `list[dict]` berisi seluruh data nasabah. Jika berkas tidak ditemukan atau formatnya rusak, kembalikan list kosong `[]`.

### 2. `update_saldo(filepath: str, norekening: int, perubahan: float) -> bool`
* **Tujuan**: Mencari nasabah berdasarkan `norekening` (integer) dan memperbarui nilai saldonya.
* **Proses & Aturan**:
  * Baca seluruh data dari berkas JSON `filepath`.
  * Cari data nasabah yang memiliki `"norekening"` sesuai dengan parameter `norekening`.
  * **Jika ditemukan**:
    1. Konversi nilai `"saldo"` nasabah tersebut ke `float`, lalu tambahkan dengan nilai `float(perubahan)`.
    2. Simpan kembali seluruh list data nasabah ke berkas `filepath` menggunakan `json.dump()` dengan parameter `indent=2`.
    3. Kembalikan nilai `True`.
  * **Jika tidak ditemukan**:
    1. Jangan ubah atau tulis ulang berkas JSON.
    2. Kembalikan nilai `False`.

### 3. `ekspor_ke_csv(json_path: str, csv_path: str) -> int`
* **Tujuan**: Membaca data nasabah dari berkas JSON `json_path` dan menuliskannya ke berkas CSV `csv_path`.
* **Proses & Aturan**:
  * Buka berkas CSV menggunakan mode tulis (`"w"`) dan parameter `newline=""`.
  * Baris pertama CSV wajib berupa header dengan nama kolom persis: `norekening,nama,saldo,matauang`.
  * Tulis seluruh baris data nasabah sesuai urutan kolom tersebut menggunakan modul `csv` (`csv.DictWriter` atau `csv.writer`).
* **Return Value**: `int` berupa jumlah baris data nasabah yang berhasil ditulis (tidak termasuk baris header).

---

## Skema Penilaian (Total: 100 Poin)

| Komponen Uji | Bobot | Kriteria Evaluasi |
| :--- | :---: | :--- |
| **TEST 1**: `baca_nasabah` | 25 Poin | Keberhasilan deserialisasi JSON menjadi `list of dict` dengan isi yang tepat. |
| **TEST 2**: `update_saldo` (Rekening Valid) | 25 Poin | Perhitungan penambahan saldo akurat, tersimpan ke JSON, dan me-return `True`. |
| **TEST 3**: `update_saldo` (Rekening Tidak Valid) | 25 Poin | Me-return `False` dan isi berkas JSON tidak berubah jika rekening tidak terdaftar. |
| **TEST 4**: `ekspor_ke_csv` | 25 Poin | Keberadaan berkas CSV, ketepatan header, isi data per baris, dan jumlah return baris tepat. |
