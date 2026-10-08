import streamlit as st
from user import user_data_by_username

# CEK APAKAH SUDAH LOGIN
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")

user = user_data_by_username()

st.text("Ganti password")

# hint untuk mematikan text input ada di -> https://docs.streamlit.io/develop/api-reference/widgets/st.text_input
# BUAT 2 INPUT TEXT 1 Username 1 Password namun disable/matikan field Username dan yang password harus tipe password
username = st.session_state.username
st.text_input("Username", value=username, disabled=True)
new_password = st.text_input("Password", type="password")

# Silahkan kalau mau baca baca ini hehe ga wajib ya-> https://discuss.streamlit.io/t/buttons-alignment/51929
col1, space, col2 = st.columns([1,3,1])
with col1:
    # Buat tombol logout st.button("logout", type="primary") keluar ke app.py
    if st.button("logout", type="primary"):
        st.session_state.username = ""
        st.session_state.password = ""
        st.session_state.logged_in = False
        st.switch_page("app.py")
        
with col2:
    # Ini untuk ubah password st.button("Ganti Data", type="secondary", width=400)
    # Kondisi -> Password baru dan lama ga boleh sama 
    # Jika sama -> st.error("ga boleh sama wok")
    # jika beda ubah melalui variabel 'user' lalu tampilkan st.success("Berhasil")
    if st.button("Ganti Password", type="secondary", width=400):
        old_password = user[username]["password"]
        if new_password == old_password:
            st.error("ga boleh sama wok")
        elif new_password == "":
            st.error("Password baru tidak boleh kosong")
        else:
            user[username]["password"] = new_password
            st.session_state.password = new_password
            st.success("Berhasil")
    
