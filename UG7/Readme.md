# Peminjaman Buku Perpustakaan

Perpustakaan kampus ingin berhenti mencatat peminjaman dan pengembalian buku di buku tulis. Petugas cukup membuka sebuah aplikasi, mengisi **nama peminjam**, memilih **buku**, lalu menekan tombol **Pinjam** atau **Kembalikan**. Aplikasi langsung menampilkan stok buku, daftar buku yang sedang dipinjam, dan rekap buku per peminjam.

Bantulah perpustakaan menyelesaikan **logika inti aplikasinya** dalam bentuk aplikasi **Streamlit**. Tampilan, form input, dan penyimpanan data sudah disediakan di kerangka program, jadi kalian cukup fokus pada pengolahan datanya dengan struktur data *built-in* Python.

## Tugas

Lengkapi bagian yang bertanda `kerjakan di sini` pada file `soal_perpustakaan.py`:

1. Fungsi `pinjam_buku(katalog, pinjaman, nama, kode)`
2. Fungsi `kembalikan_buku(katalog, pinjaman, nama, kode)`
3. Fungsi `rekap_per_peminjam(pinjaman)`
4. Lengkapi fungsi `form_buku`
4. Bagian **B** pada alur aplikasi (menangani tombol **Pinjam** dan **Kembalikan**)

**Aturan perpustakaan:**
1. Nama peminjam **wajib diisi**.
2. Buku yang **stoknya habis** tidak bisa dipinjam.
3. Satu orang **tidak boleh meminjam buku yang sama** dua kali sebelum mengembalikannya.
4. Buku hanya bisa dikembalikan jika memang **sedang dipinjam** oleh orang tersebut.

### 1. `pinjam_buku(katalog, pinjaman, nama, kode)`
Mengembalikan **pesan error** (string) jika gagal, atau `None` jika berhasil. Pengecekan dilakukan **secara berurutan**:

| Urutan | Kondisi | Pesan |
|---|---|---|
| 1 | `nama` kosong (`""`) | `Nama peminjam wajib diisi!` |
| 2 | Pasangan `nama` dan `kode` sudah ada di `pinjaman` | `Buku ini sudah kamu pinjam!` |
| 3 | Stok buku 0 | `Stok buku habis!` |

Jika berhasil: stok buku berkurang 1, dan `{"nama": nama, "kode": kode}` ditambahkan ke `pinjaman`.

### 2. `kembalikan_buku(katalog, pinjaman, nama, kode)`
Mengembalikan **pesan error** (string) jika gagal, atau `None` jika berhasil.

| Kondisi | Pesan |
|---|---|
| `nama` kosong (`""`) | `Nama peminjam wajib diisi!` |
| Tidak ada data peminjaman dengan `nama` dan `kode` tersebut | `Data peminjaman tidak ditemukan!` |

Jika berhasil: data peminjaman tersebut dihapus dari `pinjaman`, dan stok buku bertambah 1.

### 3. `rekap_per_peminjam(pinjaman)`
Mengembalikan **dictionary** `{nama: set kode buku yang sedang dipinjam}`. Jika `pinjaman` kosong, hasilnya `{}`.

Contoh: `[{"nama": "Kiya", "kode": "B02"}, {"nama": "Citey", "kode": "B01"}, {"nama": "Kiya", "kode": "B05"}]`
menghasilkan `{"Kiya": {"B02", "B05"}, "Citey": {"B01"}}`

### 4. Bagian tombol (Bagian B)
- Jika tombol **Pinjam** ditekan, panggil `pinjam_buku(...)`.
- Jika tombol **Kembalikan** ditekan, panggil `kembalikan_buku(...)`.
- Untuk keduanya: jika ada pesan error, tampilkan dengan `st.error(pesan)`. Jika tidak ada, tampilkan `st.success(...)` yang menyebutkan **nama peminjam** dan **judul buku**, misalnya `Kiya berhasil meminjam Struktur Data Python ✅`.

## Ketentuan

1. Cukup menggunakan `streamlit` (sudah di-*import* di kerangka program). **Dilarang** menambah library lain.
2. **Dilarang** mengubah bagian data, form input, fungsi tampilan, dan penyimpanan `st.session_state` yang sudah disediakan.
3. Gunakan struktur data sesuai peruntukannya: **dictionary** untuk `katalog` dan `rekap`, **list of dictionary** untuk `pinjaman`, serta **set** untuk kumpulan kode buku per peminjam.
4. Fungsi `pinjam_buku` dan `kembalikan_buku` harus **mengubah `katalog` dan `pinjaman` secara langsung** (bukan membuat salinan baru).
5. Kalian harus bisa menjelaskan ke asisten dosen mengapa `katalog` dan `pinjaman` disimpan di `st.session_state` dan bukan di variabel biasa.

## Penjelasan Parameter

Terdapat beberapa parameter yang digunakan pada fungsi-fungsi dalam program ini:

1. `katalog` = Tipe data **Dictionary Bersarang** berisi data buku `{"B01": {"judul": "Algoritma Dasar", "stok": 2}, ...}`. Key-nya adalah kode buku.
2. `pinjaman` = Tipe data **List** berisi kumpulan **Dictionary** data peminjaman yang sedang berjalan `{"nama": ..., "kode": ...}`.
3. `nama` = Tipe data **String**, nama peminjam yang diinput petugas.
4. `kode` = Tipe data **String**, kode buku yang dipilih petugas (misalnya `"B02"`).

**Data katalog awal:**

| Kode | Judul | Stok |
|---|---|---|
| B01 | Algoritma Dasar | 2 |
| B02 | Struktur Data Python | 1 |
| B03 | Basis Data Relasional | 2 |
| B04 | Statistika Dasar | 1 |
| B05 | Kalkulus 1 | 3 |

**Catatan tentang kolom nama:** nama dibaca **apa adanya** (*case-sensitive*). Jika diketik huruf kecil semua tetap huruf kecil, jika diketik huruf kapital semua tetap huruf kapital. Artinya `kiya`, `Kiya`, dan `KIYA` dianggap **tiga orang yang berbeda**. Hanya spasi di awal dan akhir yang dibuang oleh kerangka program.

## Cara Menjalankan

```bash
pip install streamlit
streamlit run soal_perpustakaan.py
```

## Test Case & Format Output

Pada program ini tidak ada *test case* yang di-*hardcode*. Kalian mengujinya langsung dari halaman Streamlit. Berikut urutan input beserta hasil yang diharapkan (stok awal `B01` = 2, `B02` = 1, `B05` = 3).

**Contoh Penggunaan yang Diharapkan:**

| No | Input | Hasil di layar |
|---|---|---|
| 1 | `Kiya`, B02, **Pinjam** | ✅ Kiya berhasil meminjam Struktur Data Python. Stok B02 menjadi 0 |
| 2 | `Citey`, B02, **Pinjam** | ❌ Stok buku habis! |
| 3 | `Kiya`, B02, **Pinjam** | ❌ Buku ini sudah kamu pinjam! |
| 4 | (nama kosong), B01, **Pinjam** | ❌ Nama peminjam wajib diisi! |
| 5 | `Citey`, B02, **Kembalikan** | ❌ Data peminjaman tidak ditemukan! |
| 6 | `Kiya`, B01, **Pinjam** | ✅ Kiya berhasil meminjam Algoritma Dasar |
| 7 | `Kiya`, B05, **Pinjam** | ✅ Kiya berhasil meminjam Kalkulus 1 |
| 8 | `Kiya`, B02, **Kembalikan** | ✅ Kiya berhasil mengembalikan Struktur Data Python. Stok B02 kembali menjadi 1 |

**Tampilan Akhir yang Diharapkan (setelah langkah 1 sampai 8):**

*Stok Buku*

| Kode | Judul | Stok |
|---|---|---|
| B01 | Algoritma Dasar | 1 |
| B02 | Struktur Data Python | 1 |
| B03 | Basis Data Relasional | 2 |
| B04 | Statistika Dasar | 1 |
| B05 | Kalkulus 1 | 2 |

*Sedang Dipinjam*

| nama | kode |
|---|---|
| Kiya | B01 |
| Kiya | B05 |

*Rekap Per Peminjam*

| Nama | Buku | Jumlah |
|---|---|---|
| Kiya | B01, B05 | 2 |

## Catatan Tambahan

- Mohon baca soal sampai selesai sebelum bertanya.
- Perhatikan **urutan pengecekan** pada `pinjam_buku`. Kasus nomor 3 pada tabel di atas (nama yang sama meminjam buku yang stoknya sudah habis) harus menghasilkan pesan `Buku ini sudah kamu pinjam!`, bukan `Stok buku habis!`.
- Pastikan fungsi `rekap_per_peminjam` tetap aman dipanggil ketika `pinjaman` masih kosong.
- Kode difokuskan pada pemahaman struktur data *built-in* Python (**list**, **set**, **dictionary**, dan **dictionary bersarang**), bukan sekadar tampilan yang benar.
