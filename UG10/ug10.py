import pandas as pd
import streamlit as st

# 1. SETUP PAGE & JUDUL APLIKASI
st.set_page_config(page_title="Dashboard Retail", layout="wide")
st.title("Dashboard Analisis Penjualan & Inventaris Toko Retail")

# 2. DATASET (JANGAN DIUBAH)
data_transaksi = {
    "id_transaksi": ["T001", "T002", "T003", "T004", "T005", "T006", "T007"],
    "nama_produk": [
        "Laptop Ultra",
        "Mouse Wireless",
        "Keyboard Mekanikal",
        "Monitor 24 Inch",
        "Meja Belajar",
        "Kursi Kerja",
        "Headset Gaming",
    ],
    "kategori": [
        "Elektronik",
        "Aksesori",
        "Aksesori",
        "Elektronik",
        "Furniture",
        "Furniture",
        "Aksesori",
    ],
    "jumlah_terjual": [3, 10, 5, 2, 4, 6, 8],
    "harga_satuan": [8000000, 150000, 400000, 2000000, 500000, 750000, 300000],
}

data_stok = {
    "nama_produk": [
        "Laptop Ultra",
        "Mouse Wireless",
        "Keyboard Mekanikal",
        "Monitor 24 Inch",
        "Meja Belajar",
        "Kursi Kerja",
        "Headset Gaming",
    ],
    "stok_gudang": [10, 50, 20, 5, 12, 15, 30],
}

# TODO 1: Ubah dictionary data_transaksi dan data_stok menjadi DataFrame Pandas
df_transaksi = pd.DataFrame(data_transaksi)
df_stok = pd.DataFrame(data_stok)


# 3. PERSIAPAN DATA & TAMPILAN AWAL
st.header("1. Data Transaksi Penjualan")

df_transaksi['total_penjualan'] = df_transaksi['jumlah_terjual'] * df_transaksi['harga_satuan']
st.dataframe(df_transaksi, use_container_width=True)

st.divider()


# 4. FILTERING & SORTING INTERAKTIF
st.header("2. Filter & Pengurutan Data Transaksi")

# Mengambil list kategori unik
kategori_list = ["Semua"] + list(df_transaksi["kategori"].unique()) if df_transaksi is not None else []
kategori_terpilih = st.selectbox("Pilih Kategori Produk:", kategori_list)

# TODO 4: Lakukan filtering data berdasarkan 'kategori_terpilih'
if kategori_terpilih == "Semua":
    df_filtered = df_transaksi.copy()
else:
    df_filtered = df_transaksi[df_transaksi["kategori"] == kategori_terpilih]

# TODO 5: Urutkan df_filtered berdasarkan kolom 'total_penjualan' secara descending (terbesar ke terkecil)
df_sorted = df_filtered.sort_values(by="total_penjualan", ascending=False)

st.subheader(f"Hasil Filter Kategori: {kategori_terpilih} (Urut Penjualan Terbanyak)")
st.dataframe(df_sorted, use_container_width=True)

st.divider()


# 5. RINGKASAN ANALISIS & VISUALISASI
st.header("3. Ringkasan Analisis & Visualisasi Pendapatan")

# TODO 7: Hitung total pendapatan keseluruhan dari kolom 'total_penjualan'
total_pendapatan = df_transaksi['total_penjualan'].sum()

st.metric(label="Total Pendapatan Toko", value=f"Rp {total_pendapatan:,.0f}")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Total Pendapatan per Kategori")
    # TODO 8: Gunakan groupby() berdasarkan 'kategori' dan hitung total sum() dari 'total_penjualan'
    pendapatan_kategori = (
            df_transaksi.groupby("kategori")["total_penjualan"]
            .sum()
            .reset_index()
        )
    
    st.dataframe(pendapatan_kategori, use_container_width=True)

with col2:
    st.subheader("Grafik Pendapatan per Kategori")
    st.bar_chart(pendapatan_kategori, x='kategori', y='total_penjualan')

st.divider()


# 6. MERGING DATA & INTEGRASI STOK GUDANG
st.header("4. Penggabungan Data Transaksi & Stok Gudang")

# TODO 11: Gabungkan df_transaksi dan df_stok berdasarkan kolom 'nama_produk' menggunakan pd.merge()
df_merged = pd.merge(df_transaksi, df_stok, on="nama_produk", how="inner")

df_merged['sisa_stok'] = df_merged['stok_gudang'] - df_merged['jumlah_terjual']

st.subheader("Data Inventaris Gabungan Akhir")
st.dataframe(df_merged, use_container_width=True)