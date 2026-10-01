import streamlit as st
import pandas as pd

# --- Title ---
st.title("Pengeluaran Anak Kos")


# --- Input Uang Bulanan ---
st.subheader("Uang Bulanan")
uang_bulanan = st.number_input(
    "Masukkan uang bulanan:",
    min_value=0,
    value=0,
    step=10000
)


# --- Input Pengeluaran ---
st.subheader("Pengeluaran Bulanan")
makanan = st.number_input("Makanan", min_value=0, value=0, step=10000)
kos = st.number_input("Kos", min_value=0, value=0, step=10000)
transportasi = st.number_input("Transportasi", min_value=0, value=0, step=10000)
internet = st.number_input("Internet/Pulsa", min_value=0, value=0, step=10000)
hiburan = st.number_input("Hiburan", min_value=0, value=0, step=10000)


# --- Tombol Ngitung Pengeluaran ---
if st.button("Hitung Pengeluaran"):

    # --- Ngitung Total Pengeluaran ---
    total_pengeluaran = makanan + kos + transportasi + internet + hiburan

    # --- Ngitung Sisa Uang ---
    sisa_uang = uang_bulanan - total_pengeluaran


    # --- Menampilkan Hasil Perhitungan ---
    st.subheader("Ringkasan Keuangan")
    kolom1, kolom2, kolom3 = st.columns(3)
    with kolom1:
        st.metric(
            "Uang Bulanan",
            f"Rp{uang_bulanan:,.0f}"
        )
    with kolom2:
        st.metric(
            "Total Pengeluaran",
            f"Rp{total_pengeluaran:,.0f}"
        )
    with kolom3:
        st.metric(
            "Sisa Uang",
            f"Rp{sisa_uang:,.0f}"
        )


    # --- Kondisi Keuangan ---
    st.subheader("Kondisi Keuangan")

    # Kondisi 1
    if sisa_uang > 0:
        st.success("Keuanganmu masih aman bulan ini!")

    # Kondisi 2
    elif sisa_uang == 0:
        st.warning("Uangmu habis..")

    # Kondisi 3
    else:
        st.error("Pengeluaranmu melebihi uang bulanan!")


    # --- Data Pengeluaran ---
    # Ini gausah diubah!
    # Udah kubantu bikinin, tinggal dipake aja
    data_pengeluaran = {
        "Kategori": [
            "Makanan",
            "Kos",
            "Transportasi",
            "Internet/Pulsa",
            "Hiburan"
        ],
        "Pengeluaran": [
            makanan,
            kos,
            transportasi,
            internet,
            hiburan
        ]
    }

    df_pengeluaran = pd.DataFrame(data_pengeluaran)

    # --- Pengeluaran Terbesar ---
    pengeluaran_terbesar = df_pengeluaran["Pengeluaran"].max()
    kategori_terbesar = df_pengeluaran.loc[
        df_pengeluaran["Pengeluaran"] == pengeluaran_terbesar,
        "Kategori"
    ].tolist()

    st.subheader("Pengeluaran Terbesar")
    st.write("Pengeluaran terbesar kamu adalah:")
    st.write(", ".join(kategori_terbesar))
    st.write(f"Rp{pengeluaran_terbesar:,.0f}")


    # --- Grafik Pengeluaran ---
    st.subheader("Grafik Pengeluaran")
    st.bar_chart(df_pengeluaran.set_index("Kategori"))