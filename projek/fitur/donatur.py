import streamlit as st
import datetime
import pandas as pd

# Inisialisasi session_state jika belum ada
if 'donatur' not in st.session_state:
    st.session_state['donatur'] = []

# Konfigurasi Halaman
st.title("🌟Donasi")
st.write("Bantu kami untuk terus memberikan dampak positif melalui donasi Anda. Setiap kontribusi sangat berarti!")

# Form Donasi
with st.form("donasi_form"):
    nama = st.text_input("Nama Lengkap", placeholder="Masukkan nama Anda")
    email = st.text_input("Email", placeholder="Masukkan email Anda")
    jumlah_donasi = st.number_input("Jumlah Donasi (Rp)", min_value=10000, step=10000)
    metode_pembayaran = st.selectbox("Metode Pembayaran", ["Transfer Bank", "Kartu Kredit", "E-Wallet", "PayPal"])
    pesan = st.text_area("Pesan untuk kami (Opsional)")

    # Tombol Submit
    submit_button = st.form_submit_button("Donasi Sekarang")

    # Jika tombol ditekan
    if submit_button:
        if nama and email and jumlah_donasi:
            # Menambahkan data donasi ke session_state['donatur']
            st.session_state['donatur'].append({
                'nama': nama,
                'email': email,
                'jumlah_donasi': jumlah_donasi,
                'metode_pembayaran': metode_pembayaran,
                'pesan': pesan
            })
            
            # Simpan data donasi ke file
            with open("donasi_log.txt", "a") as file:
                file.write(f"{datetime.datetime.now()}, {nama}, {email}, Rp{jumlah_donasi}, {metode_pembayaran}, {pesan}\n")
            
            st.success("Donasi Anda berhasil! Terima kasih atas dukungan Anda.")
        else:
            st.error("Harap lengkapi semua informasi yang diperlukan!")

# Footer
st.markdown("---")
st.write("💖 Terima kasih atas dukungan dan kebaikan Anda.")

# Menampilkan laporan pemasukan
st.header("Data Donatur")
donatur = st.session_state['donatur']
if donatur:
    df = pd.DataFrame(donatur)
    st.dataframe(df)
else:
    st.info("Belum ada data donatur.")
