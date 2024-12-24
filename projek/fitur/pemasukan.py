import streamlit as st

class Pemasukan:
    def __init__(self, nilai, keterangan):
        self.nilai = nilai 
        self.keterangan = keterangan

st.title("🪙Berikut adalah pemasukan Yayasan Darussakinah")

st.header("Jumlah pemasukan:")
nilai_pemasukan = st.number_input("Jumlah pemasukan:", min_value=0)
keterangan_pemasukan = st.text_input("Masukkan Keterangan Pemasukan")

if st.button("Kirim Pemasukan"):
    # Validasi input: Hanya tambahkan jika nilai lebih besar dari 0
    if nilai_pemasukan > 0 and keterangan_pemasukan.strip():  # Pastikan keterangan tidak kosong
        pemasukan = Pemasukan(nilai_pemasukan, keterangan_pemasukan)
        # st.write(pemasukan)
        st.session_state.keuangan.tambah_pemasukan(pemasukan)
        st.success("Pemasukan berhasil dicatat!")
    else:
        st.error("Silakan masukkan nilai pemasukan lebih dari 0 dan lengkapi keterangan!")

# Menampilkan total pemasukan
st.header("Total Pemasukan")    
st.write(f"Total Pemasukan: {st.session_state.keuangan.total_pemasukan()}")

# Menampilkan laporan pemasukan
st.header("Laporan Pemasukan")
laporan_pemasukan = st.session_state.keuangan.laporan_pemasukan()
if laporan_pemasukan:
    # Menampilkan laporan dalam bentuk tabel
    st.table(laporan_pemasukan)
else:
    st.info("Belum ada data pemasukan.")