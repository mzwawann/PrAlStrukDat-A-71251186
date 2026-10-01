import streamlit as st
import pandas as pd
import json

# Konfigurasi Halaman
st.set_page_config(page_title="Movie Explorer", layout="wide")
st.title("Movie Catalog Explorer")
st.markdown("Aplikasi interaktif untuk mengeksplorasi data film.")

@st.cache_data
def load_data():
    """Membaca file data mentah JSON."""
    with open("movies_data.json", "r") as file:
        data = json.load(file)
    return data

# Membaca data dan inisialisasi DataFrame
raw_data = load_data()
df = pd.DataFrame(raw_data)

st.sidebar.header("Filter Data")

# TODO: Gunakan widget teks untuk pencarian judul (Label: "Cari Judul Film:")
search_title = st.sidebar.text_input("Cari judul film")

# Ekstraksi genre dari DataFrame untuk opsi dropdown
genre_options = ["All"] + sorted(df["genre"].dropna().unique().tolist())

# TODO: Gunakan widget dropdown untuk pilihan genre. Masukkan variabel `genre_options` ke parameternya (Label: "Pilih Genre:")
selected_genre = st.sidebar.selectbox("Pilih genre:", genre_options)

# TODO: Gunakan widget slider. (Label: "Batas Rating Minimal:", Rentang 0.0-10.0, Default 7.0, Step 0.1)
min_rating = st.sidebar.slider(
    "Batas rating minimal",
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
)

# TODO: Gunakan widget sakelar toggle biner. (Label: "Tampilkan Raw Data JSON")
show_raw = st.sidebar.toggle("Tampilkan data JSON")

# TODO: Tampilkan struktur raw_data JSON
if show_raw:
    st.json(raw_data)

filtered_df = df.copy()

if search_title:
    filtered_df = filtered_df[filtered_df['title'].str.contains(search_title, case=False, na=False)]

if selected_genre and selected_genre != "All":
    filtered_df = filtered_df[filtered_df['genre'] == selected_genre]

if min_rating is not None:
    filtered_df = filtered_df[filtered_df['rating'] >= min_rating]

st.markdown("---")
st.subheader("Hasil Eksplorasi")

if filtered_df.empty:
    # TODO: Tampilkan widget status peringatan kuning jika hasil filter kosong
    st.warning("Tidak ada film yang sesuai dengan filter")
else:
    # TODO: Tampilkan widget status sukses hijau (Tampilkan kalimat seperti: "Berhasil menemukan X film!")
    st.success(
        f"Berhasil menemukan {len(filtered_df)} film!"
    )
    kolom1, kolom2 = st.columns(2)
    
    # TODO: Tampilkan widget ringkasan metrik (Jumlah Film dan Rata-rata Rating)
    with kolom1:
        st.metric(
            "Jumlah film",
            len(filtered_df)
        )
    
    # TODO: Tampilkan widget tabel terstruktur interaktif menggunakan variabel `filtered_df`
    with kolom2:
        st.metric(
            "Rata-rata rating",
            f"{filtered_df['rating'].mean():.2f}"
        )

    st.dataframe(filtered_df)
