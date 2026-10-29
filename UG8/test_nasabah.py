import json
import csv
import os
import shutil
import tempfile

try:
    import soal_nasabah as solusi
except ImportError:
    print("[FATAL] Berkas 'soal_nasabah.py' tidak ditemukan di direktori ini.")
    exit(1)


def identifikasi_penyebab(e: Exception) -> str:
    # Identifikasi dan format penyebab kegagalan pengujian secara informatif dan profesional
    if isinstance(e, AssertionError):
        return str(e)
    elif isinstance(e, TypeError):
        return f"Kesalahan tipe data atau operasi aritmatika ({e}). Periksa tipe data dan pastikan operasi perhitungan sesuai spesifikasi."
    elif isinstance(e, ValueError):
        return f"Kesalahan nilai atau format konversi data ({e}). Pastikan nilai numerik seperti saldo dapat dikonversi ke float."
    elif isinstance(e, KeyError):
        return f"Kunci dictionary tidak ditemukan: {e}. Periksa penulisan nama kunci ('norekening', 'nama', 'saldo', 'matauang')."
    elif isinstance(e, FileNotFoundError):
        return f"Berkas tidak ditemukan pada path yang ditentukan ({e}). Periksa penanganan path berkas."
    elif isinstance(e, AttributeError):
        return f"Atribut atau metode objek tidak ditemukan ({e}). Periksa pemanggilan fungsi atau manipulasi objek data."
    else:
        return f"Terjadi kesalahan saat pengeksekusian kode ({type(e).__name__}: {e}). Pastikan bagian ini telah diimplementasikan dengan benar."


def run_grader():
    score = 0
    total_score = 100
    points_per_test = 25

    print("=" * 65)
    print("        AUTO-GRADER: PENGOLAHAN FILE JSON & CSV (NASABAH)        ")
    print("=" * 65)

    temp_dir = tempfile.mkdtemp()
    json_path = os.path.join(temp_dir, "nasabah.json")
    csv_path = os.path.join(temp_dir, "nasabah.csv")

    dummy_data = [
        {"norekening": 8199918188, "nama": "Lumine", "saldo": 19.57, "matauang": "USD"},
        {"norekening": 9288818881, "nama": "Aether", "saldo": 123000.0, "matauang": "Yen"}
    ]

    def reset_json():
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(dummy_data, f, indent=2)

    # TEST 1: baca_nasabah
    print("\n[TEST 1] Menguji fungsi baca_nasabah()...")
    reset_json()
    try:
        hasil = solusi.baca_nasabah(json_path)
        assert hasil is not None, "Bagian fungsi baca_nasabah() belum diimplementasikan atau tidak mengembalikan nilai (return None)."
        assert isinstance(hasil, list), f"Return value harus bertipe list, ditemukan tipe: {type(hasil).__name__}."
        assert len(hasil) == 2, f"Jumlah elemen list harus 2, ditemukan: {len(hasil)}"
        assert isinstance(hasil[0], dict) and isinstance(hasil[1], dict), "Elemen di dalam list data nasabah harus bertipe dictionary."
        assert hasil[0].get("nama") == "Lumine" and hasil[1].get("nama") == "Aether", "Data nama nasabah tidak sesuai dengan isi berkas JSON sumber."
        score += points_per_test
        print(f"-> PASS (+{points_per_test} Poin)")
    except Exception as e:
        print("-> FAIL: Fungsi baca_nasabah() belum berjalan sesuai spesifikasi.")
        print(f"   Penyebab : {identifikasi_penyebab(e)}")
        print("   Solusi   : Buka berkas dengan 'with open(filepath, \"r\", encoding=\"utf-8\") as f:' lalu kembalikan hasil 'json.load(f)'.")

    # TEST 2: update_saldo (Rekening Ditemukan)
    print("\n[TEST 2] Menguji update_saldo() untuk nomor rekening terdaftar...")
    reset_json()
    try:
        status = solusi.update_saldo(json_path, 8199918188, 100.0)
        assert status is not None, "Bagian fungsi update_saldo() belum diimplementasikan atau tidak mengembalikan nilai (return None)."
        assert isinstance(status, bool), f"Return value harus bertipe boolean (True/False), ditemukan tipe: {type(status).__name__}."
        assert status is True, f"Fungsi harus mengembalikan True saat nomor rekening ditemukan, diperoleh: {status}."

        with open(json_path, "r", encoding="utf-8") as f:
            data_cek = json.load(f)

        assert isinstance(data_cek, list) and len(data_cek) > 0, "Format data berkas JSON setelah diperbarui tidak valid."
        assert "saldo" in data_cek[0], "Kunci 'saldo' tidak ditemukan pada data nasabah di berkas JSON."
        saldo_terbaru = float(data_cek[0]["saldo"])
        assert abs(saldo_terbaru - 119.57) < 0.001, f"Kesalahan perhitungan penjumlahan saldo: saldo awal 19.57 + 100.0 seharusnya menghasilkan 119.57, namun tercatat {saldo_terbaru}."
        score += points_per_test
        print(f"-> PASS (+{points_per_test} Poin)")
    except Exception as e:
        print("-> FAIL: Pembaruan saldo untuk rekening terdaftar belum tepat.")
        print(f"   Penyebab : {identifikasi_penyebab(e)}")
        print("   Solusi   : Cari nasabah yang cocok, ubah saldo dengan 'float(nasabah[\"saldo\"]) + float(perubahan)', tulis ulang ke berkas dengan 'json.dump(data, f, indent=2)', lalu return True.")

    # TEST 3: update_saldo (Rekening Tidak Ditemukan)
    print("\n[TEST 3] Menguji update_saldo() untuk nomor rekening tidak terdaftar...")
    reset_json()
    try:
        status = solusi.update_saldo(json_path, 9999999999, 50000.0)
        assert status is not None, "Bagian penanganan rekening tidak terdaftar belum mengembalikan nilai (return None)."
        assert isinstance(status, bool), f"Return value harus bertipe boolean (True/False), ditemukan tipe: {type(status).__name__}."
        assert status is False, f"Fungsi harus mengembalikan False jika nomor rekening tidak ditemukan, diperoleh: {status}."

        with open(json_path, "r", encoding="utf-8") as f:
            data_cek = json.load(f)

        assert data_cek == dummy_data, "Isi berkas JSON tidak boleh berubah jika nomor rekening tidak ditemukan."
        score += points_per_test
        print(f"-> PASS (+{points_per_test} Poin)")
    except Exception as e:
        print("-> FAIL: Penanganan nomor rekening tidak terdaftar belum tepat.")
        print(f"   Penyebab : {identifikasi_penyebab(e)}")
        print("   Solusi   : Gunakan variabel penanda (flag). Jika setelah loop selesai rekening tidak ditemukan, langsung 'return False' tanpa membuka file dalam mode tulis ('w').")

    # TEST 4: ekspor_ke_csv
    print("\n[TEST 4] Menguji fungsi ekspor_ke_csv()...")
    reset_json()
    try:
        jumlah_baris = solusi.ekspor_ke_csv(json_path, csv_path)
        assert jumlah_baris is not None, "Bagian fungsi ekspor_ke_csv() belum diimplementasikan atau tidak mengembalikan nilai (return None)."
        assert isinstance(jumlah_baris, int) and not isinstance(jumlah_baris, bool), f"Return value harus bertipe int (jumlah baris data), ditemukan tipe: {type(jumlah_baris).__name__}."
        assert jumlah_baris == 2, f"Jumlah baris data yang diekspor seharusnya 2, namun fungsi me-return: {jumlah_baris}."
        assert os.path.exists(csv_path), "Berkas CSV output tidak ditemukan setelah fungsi dijalankan."

        with open(csv_path, "r", newline="", encoding="utf-8") as f:
            baris_csv = list(csv.reader(f))

        assert len(baris_csv) == 3, f"Total baris di CSV harus 3 (1 header + 2 data), ditemukan: {len(baris_csv)}."
        assert baris_csv[0] == ["norekening", "nama", "saldo", "matauang"], f"Header CSV salah: {baris_csv[0]}."
        assert len(baris_csv) >= 3 and baris_csv[1][1] == "Lumine" and baris_csv[2][1] == "Aether", "Data kolom nama di CSV tidak cocok."
        score += points_per_test
        print(f"-> PASS (+{points_per_test} Poin)")
    except Exception as e:
        print("-> FAIL: Ekspor data ke CSV belum sesuai format.")
        print(f"   Penyebab : {identifikasi_penyebab(e)}")
        print("   Solusi   : Buka berkas CSV dengan mode 'w' dan newline='', gunakan csv.DictWriter dengan fieldnames=['norekening', 'nama', 'saldo', 'matauang'], panggil writeheader(), tulis tiap baris nasabah, dan return jumlah baris data.")

    shutil.rmtree(temp_dir)

    print("\n" + "=" * 65)
    print(f"TOTAL NILAI AKHIR: {score} / {total_score}")
    print("=" * 65)

if __name__ == "__main__":
    run_grader()
