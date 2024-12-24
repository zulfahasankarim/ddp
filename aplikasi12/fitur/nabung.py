import streamlit as st

st.title("Halaman Menabung")

#halaman formulir
with st.form("Menabung"):
    nama = st.text_input("nama antum")
    pekerjaan = st.text_input("pekerjaan")
    jumlah = st.number_input("jumlah (Rp.)", min_value=0)
    submit_button = st.form_submit_button(label="Menabung")
    if submit_button:
        st.session_state['jumlah'].append({
            "Tipe" : "Menabung",
            "Nama" : nama,
            "Pekerjaan" : pekerjaan,
            "jumlah" : jumlah



        })
        st.success("anda berhasil")
    else:
        st.error("anda gagal")