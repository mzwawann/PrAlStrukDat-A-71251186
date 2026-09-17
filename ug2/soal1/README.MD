# Antara Kevin dan Spotify

Kevin adalah orang yang **tergila-gila dengan Spotify**. Hampir setiap hari, Kevin mendengarkan berbagai macam lagu untuk menemani aktivitasnya. Karena terlalu banyak lagu yang ia sukai, Kevin mulai kesulitan menentukan lagu mana yang ingin didengarkan.

Untuk membantu Kevin mengatur daftar lagunya, dibuatlah sebuah program sederhana yang menyimpan informasi setiap lagu berupa **judul, artis, genre, dan jumlah views**.

```python
songs = [
    {"title": "Golden Hour", "artist": "JVKE", "genre": "Pop", "views": 980000},
    {"title": "Blinding Lights", "artist": "The Weeknd", "genre": "Pop", "views": 2500000},
    {"title": "Snooze", "artist": "SZA", "genre": "R&B", "views": 1200000},
    {"title": "N95", "artist": "Kendrick Lamar", "genre": "Hip-Hop", "views": 850000},
    {"title": "As It Was", "artist": "Harry Styles", "genre": "Pop", "views": 2100000},
    {"title": "Kill Bill", "artist": "SZA", "genre": "R&B", "views": 1750000}
]
```

Kevin ingin memiliki **dua fitur sorting** pada program tersebut.

## 1. Sorting Berdasarkan Jumlah Views

Kevin ingin mengetahui lagu mana yang paling populer.

Buatlah fungsi:

```python
def sort_by_views(songs):
    pass
```

Fungsi tersebut harus mengurutkan lagu berdasarkan **jumlah views dari terbesar ke terkecil**.

Contoh hasil:

```text
Blinding Lights - 2500000 views
As It Was - 2100000 views
Kill Bill - 1750000 views
Snooze - 1200000 views
Golden Hour - 980000 views
N95 - 850000 views
```

## 2. Sorting Berdasarkan Genre Favorit

Selain melihat lagu yang populer, Kevin juga memiliki **genre favorit**.

Misalnya, genre favorit Kevin adalah:

```python
favourite_genre = "R&B"
```

Kevin ingin agar lagu dengan genre favoritnya **muncul terlebih dahulu**, sedangkan lagu dari genre lain tetap ditampilkan setelahnya.

Buatlah fungsi:

```python
def sort_by_favourite_genre(songs, favourite_genre):
    pass
```

Jika genre favorit Kevin adalah `"R&B"`, maka lagu dengan genre `R&B` harus berada di bagian paling atas.

Contoh hasil:

```text
Snooze - SZA - R&B
Kill Bill - SZA - R&B
Golden Hour - JVKE - Pop
Blinding Lights - The Weeknd - Pop
N95 - Kendrick Lamar - Hip-Hop
As It Was - Harry Styles - Pop
```

## Ketentuan

* Gunakan algoritma **sorting** yang telah dipelajari.
* **Jangan menggunakan** fungsi bawaan seperti `sorted()` atau `.sort()`.
* Buatlah **dua fungsi terpisah** sesuai kebutuhan.
* `sort_by_views()` mengurutkan lagu berdasarkan jumlah views dari **terbesar ke terkecil**.
* `sort_by_favourite_genre()` memprioritaskan lagu dengan **genre favorit**.
* Semua lagu yang bukan genre favorit tetap harus ditampilkan.
