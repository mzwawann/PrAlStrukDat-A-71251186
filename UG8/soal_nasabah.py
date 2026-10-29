import json
import csv

def baca_nasabah(filepath: str) -> list[dict]:
    # Hint: Tangani kemungkinan berkas tidak ditemukan atau rusak menggunakan try-except
    try:
        # Buka berkas JSON dalam mode baca ('r') dengan encoding 'utf-8'
        with open(filepath, "r", encoding="utf-8") as file:
            # TODO: Lakukan deserialisasi menggunakan json.load() lalu kembalikan hasilnya
             return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Kembalikan list kosong jika berkas tidak ditemukan atau format tidak valid
        return []


def update_saldo(filepath: str, norekening: int, perubahan: float) -> bool:
    # Template: Baca data dari berkas JSON
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return False

    ditemukan = False
    # Template: Iterasi list nasabah untuk mencocokkan nomor rekening
    for nasabah in data:
        if nasabah.get("norekening") == norekening:
            # Hint: Ambil nilai saldo lama nasabah, konversi ke float,
            #       lalu tambahkan dengan nilai perubahan (float)
            nasabah["saldo"] = float(nasabah["saldo"]) + float(perubahan)
            ditemukan = True
            break

    # Hint: Jika rekening tidak terdaftar, jangan ubah berkas dan kembalikan False
    if not ditemukan:
        # TODO: Kembalikan nilai boolean False
        return False

    # Hint: Buka kembali berkas dalam mode tulis ('w') dan simpan data dengan json.dump(..., indent=2)
    with open(filepath, "w", encoding="utf-8") as file:
         json.dump(data, file, indent=2)

    # TODO: Kembalikan nilai boolean True setelah berkas berhasil diperbarui
    return True


def ekspor_ke_csv(json_path: str, csv_path: str) -> int:
    # Template: Baca data nasabah dari berkas sumber JSON
    try:
        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0

    # Template: Kolom yang wajib ada pada header CSV sesuai urutan
    fieldnames = ["norekening", "nama", "saldo", "matauang"]

    # Hint: Buka berkas CSV tujuan dengan mode 'w', newline='', dan encoding 'utf-8'
    #       Gunakan csv.DictWriter(csvfile, fieldnames=fieldnames)
    #       Panggil method writeheader(), lalu lakukan perulangan untuk writerow()
    with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for nasabah in data:
            writer.writerow(nasabah)

    # TODO: Kembalikan jumlah baris data nasabah yang berhasil ditulis (tipe integer)
    return len(data)