import random

import requests
import streamlit as st

# ---------- Konfigurasi ----------
BASE_URL = "https://ghibliapi.dev"


def ke_int(teks):
    """'1,000' -> 1000, '124' -> 124. Kembalikan None jika bukan angka ('', 'NA', None)."""
    try:
        return int(str(teks).replace(",", "").strip())
    except ValueError:
        return None


# ---------- Bagian 1: Mengambil data dari API ----------
def ambil_semua_film():
    """GET https://ghibliapi.dev/films -> list berisi 25 film (dict). None jika gagal."""
    url = f"{BASE_URL}/films"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def ambil_detail_film(id_film):
    """GET https://ghibliapi.dev/films/{id_film} -> 1 film (dict). None jika gagal / tidak ditemukan.
    Catatan: id yang salah tetap dibalas status 200, tetapi isinya {"status": 404}."""
    url = f"{BASE_URL}/films/{id_film}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "status" in data:
            return None
        return data
    return None


# ---------- Bagian 2: Mengolah JSON menjadi dict ----------
def ringkas_film(film):
    """Ambil field yang ditampilkan dari 1 film (dict JSON); angka (string) diubah menjadi int."""
    return {
        "id": film["id"],
        "judul": film["title"],
        "judul_asli": film["original_title"],
        "judul_romaji": film["original_title_romanised"],
        "sutradara": film["director"],
        "produser": film["producer"],
        "tahun": ke_int(film["release_date"]),
        "durasi": ke_int(film["running_time"]),
        "rt_score": ke_int(film["rt_score"]),
        "poster": film["image"],
        "banner": film["movie_banner"],
        "sinopsis": film["description"],
    }


def label_rating(rt_score):
    """>= 95 'Wajib Tonton', >= 85 'Sangat Bagus', >= 70 'Bagus', selain itu 'Biasa Saja'."""
    if rt_score >= 95:
        return "Wajib Tonton"
    elif rt_score >= 85:
        return "Sangat Bagus"
    elif rt_score >= 70:
        return "Bagus"
    else:
        return "Biasa Saja"


# ---------- Bagian 3: Rekomendasi ----------
def filter_film(daftar, sutradara, rt_min, tahun_min, tahun_max):
    """Film yang sutradaranya cocok ('Semua' = semua sutradara), rt_score >= rt_min,
    dan tahun_min <= tahun <= tahun_max."""
    hasil = []
    for film in daftar:
        cocok_sutradara = sutradara == "Semua" or film["sutradara"] == sutradara
        cocok_rating = film["rt_score"] >= rt_min
        cocok_tahun = tahun_min <= film["tahun"] <= tahun_max
        if cocok_sutradara and cocok_rating and cocok_tahun:
            hasil.append(film)
    return hasil


def rekomendasi_acak(kandidat, id_sebelumnya):
    """Pilih 1 film acak dari kandidat, selain film dengan id id_sebelumnya
    (kecuali hanya film itu satu-satunya kandidat). None jika kandidat kosong."""
    if len(kandidat) == 0:
        return None
    pilihan = [film for film in kandidat if film["id"] != id_sebelumnya]
    if len(pilihan) == 0:
        pilihan = kandidat
    return random.choice(pilihan)


# ---------- Tampilan Streamlit (tidak perlu diubah) ----------
@st.cache_data(ttl=600, show_spinner="Mengambil data dari API...")
def muat_semua_film():
    try:
        return ambil_semua_film()
    except requests.exceptions.RequestException:
        return None


@st.cache_data(ttl=600, show_spinner="Mengambil detail film...")
def muat_detail_film(id_film):
    try:
        return ambil_detail_film(id_film)
    except requests.exceptions.RequestException:
        return None


def tampilkan_film(film):
    st.image(film["banner"], width="stretch")
    col_poster, col_info = st.columns([1, 2])
    col_poster.image(film["poster"], caption=film["judul"], width="stretch")
    with col_info:
        st.header(film["judul"])
        st.caption(f"{film['judul_asli']} · {film['judul_romaji']}")
        label = label_rating(film["rt_score"])
        if label is None:
            st.warning("Selesaikan TODO 4 (label_rating) dulu.")
        else:
            st.markdown(f"**🏷️ {label}**")
        m1, m2, m3 = st.columns(3)
        m1.metric("Tahun", film["tahun"])
        m2.metric("Durasi", f"{film['durasi']} menit")
        m3.metric("RT Score", f"{film['rt_score']}%")
        st.write(f"**Sutradara**: {film['sutradara']}")
        st.write(f"**Produser**: {film['produser']}")
        st.subheader("📖 Sinopsis")
        st.write(film["sinopsis"])


def main():
    st.set_page_config(page_title="Ghibli Movie Recommender", page_icon="🎲", layout="wide")
    st.title("🎲 Ghibli Movie Recommender")
    st.caption(f"Bingung mau nonton apa? Biar aplikasi yang memilihkan. Sumber data: {BASE_URL}")

    films = muat_semua_film()
    if not films:
        st.error("Gagal mengambil data film. Cek koneksi internet atau TODO 1 (ambil_semua_film).")
        st.stop()

    daftar = [ringkas_film(f) for f in films]
    if daftar[0] is None:
        st.warning("Selesaikan TODO 3 (ringkas_film) dulu.")
        st.stop()

    # Filter di sidebar
    st.sidebar.header("🎛️ Filter")
    semua_sutradara = sorted({f["sutradara"] for f in daftar})
    sutradara = st.sidebar.selectbox("Sutradara", ["Semua"] + semua_sutradara)
    rt_min = st.sidebar.slider("RT Score minimal", 0, 100, 0, step=5)
    semua_tahun = [f["tahun"] for f in daftar]
    tahun_min, tahun_max = st.sidebar.slider(
        "Rentang tahun rilis", min(semua_tahun), max(semua_tahun), (min(semua_tahun), max(semua_tahun))
    )
    kandidat = filter_film(daftar, sutradara, rt_min, tahun_min, tahun_max)
    if kandidat is None:
        st.warning("Selesaikan TODO 5 (filter_film) dulu.")
        st.stop()
    st.sidebar.caption(f"{len(kandidat)} dari {len(daftar)} film cocok dengan filter.")

    if st.button("🎲 Rekomendasikan Film", type="primary"):
        pilih = rekomendasi_acak(kandidat, st.session_state.get("film_id"))
        if pilih is None:
            st.session_state.pop("film_id", None)
            st.warning("Tidak ada film yang cocok dengan filter (atau TODO 6 belum selesai).")
        else:
            st.session_state["film_id"] = pilih["id"]

    if "film_id" in st.session_state:
        detail = muat_detail_film(st.session_state["film_id"])
        if not detail:
            st.error("Gagal mengambil detail film. Cek TODO 2 (ambil_detail_film).")
        else:
            tampilkan_film(ringkas_film(detail))


if __name__ == "__main__":
    main()
