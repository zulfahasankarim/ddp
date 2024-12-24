import streamlit as st

class Pengeluaran:
    def __init__(self, nilai, keterangan):
        self.nilai = nilai 
        self.keterangan = keterangan

class Uang:
    def __init__(self):
        self.pengeluaran_list = []

    def tambah_pengeluaran(self, pengeluaran):
        self.pengeluaran_list.append(pengeluaran)

    def total_pengeluaran(self):
        return sum(pengeluaran.nilai for pengeluaran in self.pengeluaran_list )

    def laporan_pengeluaran(self):
        return [
            {"Keterangan": pengeluaran.keterangan, "Nilai pengeluaran": pengeluaran.nilai}
            for pengeluaran in self.pengeluaran_list
        ]

if "uang" not in st.session_state:
    st.session_state.uang = Uang()

st.title("Berikut adalah pengeluaran Yayasan Darussakinah")

st.header("Jumlah pengeluaran:")
nilai_pengeluaran = st.number_input("Jumlah pengeluaran:", min_value=0)
keterangan_pengeluaran = st.text_input("Masukkan Keterangan pengeluaran")

if st.button("Kirim pengeluaran"):
    # Validasi input: Hanya tambahkan jika nilai lebih besar dari 0
    if nilai_pengeluaran > 0 and keterangan_pengeluaran.strip():  # Pastikan keterangan tidak kosong
        pengeluaran = Pengeluaran(nilai_pengeluaran, keterangan_pengeluaran)
        st.session_state.uang.tambah_pengeluaran(pengeluaran)
        st.success("pengeluaran berhasil dicatat!")
    else:
        st.error("Silakan masukkan nilai pengeluaran lebih dari 0 dan lengkapi keterangan!")

# Menampilkan total pengeluaran
st.header("Total pengeluaran")
st.write(f"Total pengeluaran: {st.session_state.uang.total_pengeluaran()}")

# Menampilkan laporan pengeluaran
st.header("Laporan pengeluaran")
laporan_pengeluaran = st.session_state.uang.laporan_pengeluaran()
if laporan_pengeluaran:
    # Menampilkan laporan dalam bentuk tabel
    st.table(laporan_pengeluaran)
else:
    st.info("Belum ada data pengeluaran.")