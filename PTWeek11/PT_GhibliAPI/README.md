# Post Test: Ghibli Movie Recommender

Malam minggu, kamu dan teman-teman mau nonton film Studio Ghibli, tapi selalu berakhir debat "nonton apa ya?". Supaya tidak bingung lagi, kamu membuat aplikasi yang **merekomendasikan satu film Ghibli secara acak**, lengkap dengan **poster**, **informasi film**, dan **sinopsis**. Datanya diambil langsung dari **Studio Ghibli API** (https://ghibliapi.dev).

Tampilan Streamlit sudah disiapkan di `soal.py`. Tugasmu melengkapi 6 fungsi bertanda `TODO` supaya aplikasi bisa:

- Mengambil data film dari API (`requests.get`, `response.json()`)
- Mengolah JSON menjadi dictionary
- Memberi label rating dan memfilter film sesuai selera
- Memilih film secara acak (`random`)

## Persiapan

```bash
uv init posttest-ghibli
cd posttest-ghibli
uv add requests streamlit
```

Atau dengan pip: `pip install requests streamlit`.

Salin `soal.py` ke folder tersebut, kerjakan TODO-nya, lalu jalankan:

```bash
uv run streamlit run soal.py
```

Selama TODO 1 belum selesai, aplikasi hanya menampilkan pesan error. Kerjakan berurutan dan jalankan ulang aplikasi setiap selesai satu TODO.

## Struktur Folder

```
PT_GhibliAPI/
├── soal.py       # kerangka aplikasi, kerjakan TODO 1-6 di sini
└── README.md     # soal + dokumentasi API
```

## Alur Aplikasi

1. Aplikasi mengambil semua film dari `https://ghibliapi.dev/films` (`ambil_semua_film`), lalu meringkas tiap film (`ringkas_film`).
2. Di sidebar, pengguna mengatur filter: sutradara, RT Score minimal, dan rentang tahun. Film yang cocok dicari dengan `filter_film`.
3. Tombol **🎲 Rekomendasikan Film** memilih 1 film acak dari film yang cocok (`rekomendasi_acak`), berbeda dari rekomendasi sebelumnya.
4. Detail film yang terpilih diambil dari `https://ghibliapi.dev/films/{id}` (`ambil_detail_film`), lalu ditampilkan: banner, poster, judul (Inggris, Jepang, romaji), label rating (`label_rating`), tahun, durasi, RT Score, sutradara, produser, dan sinopsis.

## Soal

Yang sudah disediakan di `soal.py`:

- `BASE_URL = "https://ghibliapi.dev"`, alamat dasar API.
- Fungsi `ke_int(teks)`: mengubah string angka menjadi `int` (`"124"` jadi `124`, `"1,000"` jadi `1000`) dan mengembalikan `None` untuk nilai yang bukan angka (`""`, `"NA"`).

Setiap TODO punya contoh pemanggilan dengan tanda `>>>`. Kamu bisa mencobanya sendiri di Python interaktif, dari folder yang sama dengan `soal.py`:

```bash
uv run python
```

```python
>>> from soal import *
>>> films = ambil_semua_film()
>>> len(films)
25
```

Ketik `exit()` untuk keluar. Setiap kali `soal.py` diubah, keluar lalu masuk lagi supaya perubahannya terbaca.

Contoh output di bawah dibuat dari data API per November 2026. Jika data API berubah, hasilnya bisa sedikit berbeda.

### TODO 1: `ambil_semua_film()` (15 poin)

Ambil semua film dari `https://ghibliapi.dev/films`. Polanya sama seperti contoh PokéAPI di modul:

1. Buat URL: `f"{BASE_URL}/films"`
2. Kirim request: `response = requests.get(url)`
3. Jika `response.status_code == 200`, kembalikan `response.json()`. Hasilnya **list** berisi 25 film (setiap film berupa dict).
4. Selain itu, kembalikan `None`.

```python
>>> films = ambil_semua_film()
>>> len(films)
25
>>> films[0]["title"]
'Nausicaä of the Valley of the Wind'
```

### TODO 2: `ambil_detail_film(id_film)` (15 poin)

Ambil **1 film** berdasarkan id-nya dari `https://ghibliapi.dev/films/{id_film}`. Hasilnya **dict** satu film.

1. Buat URL: `f"{BASE_URL}/films/{id_film}"`
2. Kirim request dengan `requests.get(url)`.
3. Jika `status_code == 200`, ubah ke JSON: `data = response.json()`.
4. **Perhatikan**: API ini membalas id yang salah dengan status **200** juga, tetapi isinya `{"status": 404}`. Jadi:
   - jika key `"status"` ada di `data` (`"status" in data`), kembalikan `None`
   - jika tidak ada, kembalikan `data`
5. Jika `status_code` bukan 200, kembalikan `None`.

```python
>>> spirited = ambil_detail_film("dc2e6bd1-8156-4886-adff-b39e6043af0c")
>>> spirited["title"], spirited["director"]
('Spirited Away', 'Hayao Miyazaki')
>>> print(ambil_detail_film("tidak-ada"))   # API membalas {"status": 404}
None
```

### TODO 3: `ringkas_film(film)` (20 poin)

Ubah satu film (dict dari API) menjadi dict baru dengan key berbahasa Indonesia:

| Key hasil | Ambil dari | Tipe hasil |
| --- | --- | --- |
| `id` | `film["id"]` | str |
| `judul` | `film["title"]` | str |
| `judul_asli` | `film["original_title"]` | str |
| `judul_romaji` | `film["original_title_romanised"]` | str |
| `sutradara` | `film["director"]` | str |
| `produser` | `film["producer"]` | str |
| `tahun` | `ke_int(film["release_date"])` | int |
| `durasi` | `ke_int(film["running_time"])` | int |
| `rt_score` | `ke_int(film["rt_score"])` | int |
| `poster` | `film["image"]` | str (URL) |
| `banner` | `film["movie_banner"]` | str (URL) |
| `sinopsis` | `film["description"]` | str |

`tahun`, `durasi`, dan `rt_score` dikirim API sebagai string (`"2001"`), jadi diubah ke `int` dengan `ke_int` supaya bisa dibandingkan di TODO 5.

```python
>>> ringkas_film(spirited)
{'id': 'dc2e6bd1-8156-4886-adff-b39e6043af0c', 'judul': 'Spirited Away', 'judul_asli': '千と千尋の神隠し',
 'judul_romaji': 'Sen to Chihiro no kamikakushi', 'sutradara': 'Hayao Miyazaki', 'produser': 'Toshio Suzuki',
 'tahun': 2001, 'durasi': 124, 'rt_score': 97,
 'poster': 'https://image.tmdb.org/t/p/w600_and_h900_bestv2/39wmItIWsg5sZMyRUHLkWBcuVCM.jpg',
 'banner': 'https://image.tmdb.org/t/p/original/bSXfU4dwZyBA1vMmXvejdRXBvuF.jpg',
 'sinopsis': 'Spirited Away is an Oscar winning Japanese animated film abo...'}
```

(`sinopsis` dipotong di contoh ini supaya ringkas.)

### TODO 4: `label_rating(rt_score)` (15 poin)

Gunakan `if` / `elif` / `else`:

| `rt_score` | Label |
| --- | --- |
| >= 95 | `Wajib Tonton` |
| >= 85 | `Sangat Bagus` |
| >= 70 | `Bagus` |
| di bawahnya | `Biasa Saja` |

```python
>>> label_rating(95), label_rating(94), label_rating(70), label_rating(29)
('Wajib Tonton', 'Sangat Bagus', 'Bagus', 'Biasa Saja')
```

### TODO 5: `filter_film(daftar, sutradara, rt_min, tahun_min, tahun_max)` (20 poin)

`daftar` adalah list film hasil `ringkas_film`. Buat list kosong `hasil`, lalu periksa setiap film dengan `for`. Film dimasukkan ke `hasil` (`append`) jika memenuhi **ketiga** syarat:

- `sutradara == "Semua"`, **atau** `film["sutradara"]` sama dengan `sutradara`
- `film["rt_score"] >= rt_min`
- `tahun_min <= film["tahun"] <= tahun_max`

Kembalikan `hasil`.

Kenapa difilter di Python? Karena API ini **tidak bisa** memfilter: `?director=...` diabaikan dan API selalu mengirim semua film.

```python
>>> daftar = [ringkas_film(f) for f in films]
>>> [f["judul"] for f in filter_film(daftar, "Hayao Miyazaki", 95, 1984, 2023)]
['Castle in the Sky', "Kiki's Delivery Service", 'Porco Rosso', 'Spirited Away', 'The Boy and the Heron']
>>> [f["judul"] for f in filter_film(daftar, "Semua", 90, 2000, 2015)]
['Spirited Away', 'Ponyo', 'Arrietty', 'The Tale of the Princess Kaguya', 'When Marnie Was There']
>>> filter_film(daftar, "Semua", 101, 1984, 2023)
[]
```

### TODO 6: `rekomendasi_acak(kandidat, id_sebelumnya)` (15 poin)

Pilih 1 film secara acak dari `kandidat` (hasil `filter_film`). `id_sebelumnya` adalah id film yang direkomendasikan sebelumnya (`None` jika belum pernah).

1. Jika `kandidat` kosong (`len(kandidat) == 0`), kembalikan `None`.
2. Buat list `pilihan` berisi film di `kandidat` yang `film["id"]`-nya **tidak sama** dengan `id_sebelumnya`, supaya tombol 🎲 tidak memberi film yang sama dua kali berturut-turut.
3. Jika `pilihan` kosong (kandidat cuma berisi film sebelumnya), isi `pilihan = kandidat`.
4. Kembalikan `random.choice(pilihan)`.

`random.choice(list)` dari library bawaan `random` mengambil 1 elemen acak dari sebuah list:

```python
import random
random.choice(["apel", "jeruk", "mangga"])   # 'jeruk' (bisa berbeda setiap dijalankan)
```

```python
>>> print(rekomendasi_acak([], None))
None
>>> kandidat = filter_film(daftar, "Hayao Miyazaki", 95, 1984, 2023)
>>> rekomendasi_acak(kandidat, None)["judul"]                 # hasil acak
'Porco Rosso'
>>> rekomendasi_acak(kandidat, spirited["id"])["judul"]       # tidak pernah 'Spirited Away'
'Castle in the Sky'
>>> goro = filter_film(daftar, "Gorō Miyazaki", 50, 1984, 2023)   # hanya 1 film
>>> rekomendasi_acak(goro, goro[0]["id"])["judul"]
'From Up on Poppy Hill'
```

## Penilaian

| Bagian | Poin |
| --- | --- |
| TODO 1 `ambil_semua_film` | 15 |
| TODO 2 `ambil_detail_film` | 15 |
| TODO 3 `ringkas_film` | 20 |
| TODO 4 `label_rating` | 15 |
| TODO 5 `filter_film` | 20 |
| TODO 6 `rekomendasi_acak` | 15 |
| **Total** | **100** |

Ketentuan:

- Jangan mengubah nama fungsi, parameter, dan bagian **Tampilan Streamlit**.
- Hanya boleh memakai library `requests`, `random`, dan `streamlit`. Pandas tidak boleh dipakai.
- Aplikasi harus bisa dijalankan dengan `streamlit run soal.py` tanpa error.

---

# Dokumentasi Studio Ghibli API

Studio Ghibli API adalah API publik (REST, hanya `GET`) berisi data film, karakter, lokasi, spesies, dan kendaraan dari film-film Studio Ghibli. API ini **tidak membutuhkan API key**, dan semua respons berupa JSON.

| | |
| --- | --- |
| Base URL | `https://ghibliapi.dev` |
| Method | `GET` |
| Autentikasi | Tidak ada |
| Format respons | JSON (`Content-Type: application/json;charset=UTF-8`) |

## Endpoint

| Endpoint | Hasil | Jumlah data |
| --- | --- | --- |
| `/films` | list semua film | 25 |
| `/films/{id}` | 1 film (dict) | |
| `/people` | list semua karakter | 57 |
| `/people/{id}` | 1 karakter | |
| `/locations` | list semua lokasi | 25 |
| `/locations/{id}` | 1 lokasi | |
| `/species` | list semua spesies | 7 |
| `/species/{id}` | 1 spesies | |
| `/vehicles` | list semua kendaraan | 3 |
| `/vehicles/{id}` | 1 kendaraan | |

`{id}` berupa UUID, misalnya `58611129-2dbc-4a81-a72f-77ddfc1b1b49`.

Soal ini hanya memakai `/films` dan `/films/{id}`. Endpoint lain dicantumkan sebagai referensi.

## Contoh Pemakaian di Python

Langkahnya sama seperti modul (OMDb API dan PokéAPI): kirim request, cek status, ubah ke JSON, lalu akses seperti dictionary.

```python
import requests

BASE_URL = "https://ghibliapi.dev"

# 1. Ambil semua film (hasilnya list of dict)
response = requests.get(f"{BASE_URL}/films")
if response.status_code == 200:
    films = response.json()
    print(len(films))                   # 25
    print(films[0]["title"])            # Nausicaä of the Valley of the Wind
    for film in films[:3]:
        print(film["release_date"], film["title"], film["rt_score"])

# 2. Ambil 1 film berdasarkan id (hasilnya dict)
response = requests.get(f"{BASE_URL}/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49")
if response.status_code == 200:
    totoro = response.json()
    print(totoro["title"], totoro["director"])   # My Neighbor Totoro Hayao Miyazaki
```

## Gambar Poster dan Banner

Field `image` (poster, rasio potret) dan `movie_banner` (gambar lebar) pada film berisi URL gambar JPEG dari TMDB (`image.tmdb.org` atau `www.themoviedb.org`). Beberapa URL `www.themoviedb.org` akan di-*redirect* ke `image.tmdb.org`, tetapi tetap bisa ditampilkan. Semua 25 URL poster aktif.

URL gambar bisa langsung dipakai di Streamlit tanpa diunduh dulu: `st.image(film["image"])`.

## Struktur Data

Semua field bertipe **string**, termasuk angka (`"1988"`, `"86"`, `"93"`), kecuali field relasi yang berupa list URL.

### Film (`/films`)

```json
{
  "id": "58611129-2dbc-4a81-a72f-77ddfc1b1b49",
  "title": "My Neighbor Totoro",
  "original_title": "となりのトトロ",
  "original_title_romanised": "Tonari no Totoro",
  "image": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/rtGDOeG9LzoerkDGZF9dnVeLppL.jpg",
  "movie_banner": "https://image.tmdb.org/t/p/original/etqr6fOOCXQOgwrQXaKwenTSuzx.jpg",
  "description": "Two sisters move to the country with their father ...",
  "director": "Hayao Miyazaki",
  "producer": "Hayao Miyazaki",
  "release_date": "1988",
  "running_time": "86",
  "rt_score": "93",
  "people": ["https://ghibliapi.dev/people/986faac6-67e3-4fb8-a9ee-bad077c2e7fe", "..."],
  "species": ["https://ghibliapi.dev/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2", "..."],
  "locations": ["https://ghibliapi.dev/locations/"],
  "vehicles": ["https://ghibliapi.dev/vehicles/"],
  "url": "https://ghibliapi.dev/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49"
}
```

| Field | Keterangan |
| --- | --- |
| `id` | UUID film |
| `title` | Judul bahasa Inggris |
| `original_title` | Judul asli (huruf Jepang) |
| `original_title_romanised` | Judul asli dalam huruf latin |
| `image` | URL poster |
| `movie_banner` | URL gambar banner |
| `description` | Sinopsis singkat |
| `director` | Sutradara |
| `producer` | Produser |
| `release_date` | Tahun rilis |
| `running_time` | Durasi (menit) |
| `rt_score` | Skor kritikus Rotten Tomatoes (0-100) |
| `people`, `species`, `locations`, `vehicles` | List URL data terkait |
| `url` | URL film ini sendiri |

### Karakter (`/people`)

```json
{
  "id": "267649ac-fb1b-11eb-9a03-0242ac130003",
  "name": "Haku",
  "gender": "Male",
  "age": "12",
  "eye_color": "Green",
  "hair_color": "Green",
  "films": ["https://ghibliapi.dev/films/dc2e6bd1-8156-4886-adff-b39e6043af0c"],
  "species": "https://ghibliapi.dev/species/e2cfaa78-fb19-11eb-9a03-0242ac130003",
  "url": "https://ghibliapi.dev/people/267649ac-fb1b-11eb-9a03-0242ac130003"
}
```

| Field | Keterangan |
| --- | --- |
| `name` | Nama karakter |
| `gender` | `Male`, `Female`, atau `NA` |
| `age` | Umur. Bisa angka (`"13"`) atau teks (`"NA"`, `"Adult"`, `"Unspecified/Adult"`, `""`) |
| `eye_color`, `hair_color` | Warna mata dan rambut |
| `films` | List URL film tempat karakter muncul |
| `species` | URL spesies (string, **bukan** list) |

### Lokasi (`/locations`)

| Field | Keterangan |
| --- | --- |
| `name` | Nama lokasi |
| `climate` | Iklim (`Continental`, `Mild`, `Tropical`, ...) |
| `terrain` | Medan (`Hill`, `City`, `River`, ...) |
| `surface_water` | Persentase air permukaan (string) |
| `residents` | List URL karakter penghuni |
| `films` | List URL film |

### Spesies (`/species`)

| Field | Keterangan |
| --- | --- |
| `name` | Nama spesies (`Human`, `Cat`, `Totoro`, ...) |
| `classification` | Klasifikasi (`Mammal`, `Spirit`, ...) |
| `eye_colors`, `hair_colors` | Daftar warna dalam 1 string, dipisah koma |
| `people` | List URL karakter |
| `films` | List URL film |

### Kendaraan (`/vehicles`)

| Field | Keterangan |
| --- | --- |
| `name` | Nama kendaraan |
| `description` | Deskripsi |
| `vehicle_class` | Jenis (`Airship`, `Airplane`, `Boat`) |
| `length` | Panjang, bisa memakai koma ribuan (`"1,000"`) |
| `pilot` | URL karakter pengemudi (string) |
| `films` | List URL film |

## Respons Error

API ini **tidak** memakai status code HTTP untuk menandai data tidak ditemukan. Request ke id atau endpoint yang salah tetap dibalas **HTTP 200** dengan body:

```json
{"status": 404}
```

| Request | HTTP status | Body |
| --- | --- | --- |
| `GET /films` | 200 | list film |
| `GET /films/58611129-...` | 200 | dict film |
| `GET /films/tidak-ada` | **200** | `{"status": 404}` |
| `GET /endpoint-salah` | **200** | `{"status": 404}` |

Jadi, mengecek `response.status_code == 200` saja tidak cukup. Cek juga apakah JSON-nya punya key `"status"`. Data film yang benar tidak pernah punya key `"status"`:

```python
data = response.json()
if "status" in data:
    print("Data tidak ditemukan")
else:
    print(data["title"])
```

## Catatan Data

Hal-hal yang perlu diperhatikan saat mengolah data dari API ini:

1. **Angka berupa string.** `release_date`, `running_time`, `rt_score`, `age`, `surface_water`, dan `length` harus dikonversi dulu (`int(...)`) sebelum dihitung atau dibandingkan.
2. **Query parameter diabaikan.** `/films?title=Ponyo` atau `/films?limit=2` tetap mengembalikan 25 film. Pencarian dan filter harus dilakukan sendiri di Python.
3. **URL relasi kosong.** Banyak film yang field `people`, `locations`, atau `vehicles`-nya hanya berisi `["https://ghibliapi.dev/people/"]` (tanpa id). Relasi film-karakter lebih lengkap jika dicari dari sisi karakter (`people[i]["films"]`). Contoh: *The Cat Returns* punya 6 karakter jika dicari lewat `/people`, tetapi `film["people"]` hanya berisi URL kosong.
4. **Nilai tidak lengkap.** Beberapa data berisi `"NA"`, `"TODO"`, atau string kosong `""` (misalnya `age`, `climate`, `terrain`).
5. **Hanya baca.** API hanya mendukung `GET`. Tidak ada `POST`, `PUT`, atau `DELETE`.
