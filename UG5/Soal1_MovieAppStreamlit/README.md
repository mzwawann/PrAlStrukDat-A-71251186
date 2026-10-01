# Modul Praktikum Struktur Data Pertemuan 7
## Dashboard Eksplorasi Katalog Film dengan Streamlit

### Deskripsi Skenario
Pada praktikum kali ini, Anda ditugaskan untuk mengimplementasikan antarmuka interaktif pada aplikasi web sederhana. Aplikasi ini merupakan sebuah Dashboard Eksplorasi Katalog Film yang mengambil data lokal dari file `movies_data.json`. Data yang diolah mencakup struktur atribut dasar: `id`, `title`, `genre`, `year`, `rating`, dan `duration_min`.

Fokus utama pada modul ini adalah mengimplementasikan **Widget Input**, **Widget Output**, dan memahami **Model Eksekusi Top-to-Bottom/Rerun** pada library Streamlit yang dijelaskan di halaman 8-10 pada buku modul.

### Aturan Pengerjaan
Anda telah disediakan file kerangka kode (`movie_app.py`) yang strukturnya telah dibagi menjadi beberapa bagian utama:
- **BAGIAN A & Logika Filtering**: Operasi I/O file, pengambilan list genre unik, serta logika penyaringan data (menggunakan Pandas) **telah disediakan secara lengkap**.
- **BAGIAN B & C**: Tugas Anda 100% difokuskan untuk mengganti variabel-variabel `None` dan blok `pass` yang ditandai `# TODO` dengan fungsi pemanggilan *widget* Streamlit yang bersesuaian.

---

### Spesifikasi Tugas

#### BAGIAN B: Tugas Widget Input Praktikan
Pada bagian ini, Anda akan membuat komponen input yang diletakkan di *sidebar* (`st.sidebar`), serta satu komponen output untuk menampilkan data mentah:
- **Pencarian Judul**: Gunakan widget input teks. (Label: `"Cari Judul Film:"`)
- **Pilihan Genre**: Gunakan widget input pilihan/dropdown. (Label: `"Pilih Genre:"`). **Penting:** Opsi pilihan wajib mem-passing variabel `genre_options` yang sudah terdefinisi di kode.
- **Batas Rating Minimum**: Gunakan widget input numerik bergeser (slider).
  - Label: `"Batas Rating Minimal:"`
  - Rentang: `0.0` sampai `10.0`
  - Nilai Default: `7.0`
  - Skala (*Step*): `0.1`
- **Sakelar Data Mentah**: Gunakan widget sakelar *toggle* biner. (Label: `"Tampilkan Raw Data JSON"`)
- **Tampilan Raw Data**: (Berada tepat setelah toggle) Jika nilai sakelar *toggle* di atas adalah `True`, render struktur data JSON mentah (`raw_data`) menggunakan widget output khusus JSON.

#### BAGIAN C: Tugas Widget Output Praktikan
Pada bagian ini, Anda akan menampilkan hasil penyaringan data di area utama (*main area*) aplikasi:
- **Peringatan Data Kosong**: Jika data hasil filter ternyata kosong (`filtered_df.empty`), keluarkan widget output status berupa kotak peringatan berwarna kuning (`warning`).
- **Notifikasi Sukses**: Jika data hasil filter tidak kosong, keluarkan widget output status sukses berwarna hijau.
- **Ringkasan Metrik**: Tampilkan informasi agregat menggunakan widget ringkasan metrik untuk **"Jumlah Film"** dan **"Rata-rata Rating"**. (Tips: Gunakan `st.columns(2)` agar posisinya dapat diatur bersebelahan secara horizontal).
- **Tabel Interaktif**: Render variabel struktur DataFrame hasil penyaringan (`filtered_df`) menggunakan widget output tabel interaktif (*dataframe*).

---

### Cara Menjalankan Aplikasi
Setelah Anda melengkapi instruksi `# TODO`, Anda dapat melihat hasilnya secara langsung dengan mengeksekusi perintah terminal berikut:

```bash
streamlit run movie_app.py
```
Perhatikan bagaimana Streamlit secara otomatis menjalankan ulang (*rerun*) seluruh baris kode Anda secara berurutan dari atas ke bawah (*top-to-bottom*) setiap kali Anda memodifikasi nilai pada widget input.
