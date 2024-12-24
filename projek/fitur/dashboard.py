import streamlit as st
import datetime
import pandas as pd

# Inisialisasi session_state jika belum ada
if 'donatur' not in st.session_state:
    st.session_state['donatur'] = []
if 'keuangan' not in st.session_state:
    st.session_state['keuangan'] = []  # Untuk data pemasukan
if 'pengeluaran' not in st.session_state:
    st.session_state['pengeluaran'] = []  # Untuk data pengeluaran

# Konfigurasi Halaman
st.title("Dashboard🌙")
st.subheader("Ini adalah aplikasi alat hitung sederhana yang di khususkan untuk menghitung keuangan yayasan")
st.image("./img/logo.jpeg")

st.write("======================================================================================")
st.write("")

# Daftar Anggota Kelompok 2
st.subheader("Daftar Kelompok 2")
image_files = [
    {'img': './img/zul.jpeg', 'name': 'Zulfa Hasanul Karim'},
    {'img': './img/ham.jpeg', 'name': 'Muhammad Ilham Ramadan'},
    {'img': './img/din.jpeg', 'name': 'Andini'},
    {'img': './img/qai.jpeg', 'name': 'Kamila Qaisara Batrisyia'},
]

cols = st.columns(2)
for idx, image_info in enumerate(image_files):
    img_path = image_info['img']
    col_idx = idx % 2
    with cols[col_idx]:
        st.image(img_path, caption=image_info['name'])
    if col_idx == 1 and idx < len(image_files) - 1:
        cols = st.columns(2)


# ========================= Rincian Pemasukan =========================
st.subheader("Rincian Pemasukan")
# st.write(st.session_state.keuangan)
if st.session_state.keuangan:
    laporan_pemasukan = st.session_state.keuangan.laporan_pemasukan()
    if laporan_pemasukan:
        # Menampilkan laporan dalam bentuk tabel
        st.table(laporan_pemasukan)
    else:
        st.info("Belum ada data pemasukan.")
else:
    st.info("Belum ada data pemasukan.")

# ========================= Rincian Pengeluaran =========================
st.subheader("Rincian Pengeluaran")
if st.session_state.uang:
    laporan_pengeluaran = st.session_state.uang.laporan_pengeluaran()
    if laporan_pengeluaran:
        # Menampilkan laporan dalam bentuk tabel
        st.table(laporan_pengeluaran)
    else:
        st.info("Belum ada data pengeluaran.")
else:
    st.info("Belum ada data pengeluaran.")

# ========================= Data Donatur =========================
st.subheader("Data Donatur")
if st.session_state.donatur:
    data_donatur = st.session_state['donatur']
    if data_donatur:
        # Menampilkan  laporan dalam bentuk tabel
        st.table(data_donatur)
    else:
        st.info("Belum ada data donatur.")
else:
    st.info("Belum ada data donatur.")
