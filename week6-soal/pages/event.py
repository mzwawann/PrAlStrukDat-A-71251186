import streamlit as st
from pathlib import Path

# cek apakah sudah login
if "logged_in" not in st.session_state or not st.session_state.logged_in == True:
    st.switch_page("app.py")

# BAWAH INI JANGAN DIUBAH YA PENTING INI -3000 KALAU NGUBAH
st.set_page_config(page_title="JAPFEST 2026")

st.title("🎌 JAPFEST 2026")
st.caption("UKDW Japanese Festival")

# hero img
image = Path(__file__).parent.parent / "japfest.png"
col1, col2, col3 = st.columns([1,3,1])
with col2:
    st.image(str(image), width=400, caption="JAPFEST UKDW")
    
# Isi 
st.header("TENTANG JAPFEST", divider="green", text_alignment="center")
st.markdown("""
JAPFEST 2026 adalah festival budaya Jepang yang menghadirkan
hiburan, kompetisi, kreativitas, dan berbagai aktivitas menarik.

**📅 Minggu, 6 Desember 2026**  
**📍 Gedung Koinonia, UKDW — Yogyakarta**
---

""")
st.header("APA AJA DI JAPFEST", divider="green", text_alignment="center")
st.markdown(
    """
    **🎮 Tekken Tournament**  
Kompetisi fighting game untuk para pemain dan komunitas.

**🎤 Live Performance**  
Berbagai penampilan dengan nuansa Jepang dan pop culture.

**🍜 Japanese Food & Tenant**  
Berbagai makanan, produk, dan booth menarik.

**🎌 Japanese Culture Activities**  
Aktivitas interaktif untuk mengenal budaya Jepang.
---

""")
st.header("TIKET", divider="green", text_alignment="center")
st.markdown(
'''
    **Presale — Rp15.000**

    <a href="https://yourtix.co.id/event/japfest-ukdw-2026" target="_blank">
        <button style="
            background-color:#FF4B4B;
            color:white;
            padding:10px 24px;
            border:none;
            border-radius:8px;
            font-size:16px;
            font-weight:bold;
            cursor:pointer;
        ">
            🎟️ Beli Tiket
        </button>
    </a>
    <br>
    📱 Instagram: @japfestukdw       
''', unsafe_allow_html=True)