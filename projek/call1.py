import streamlit as st

# Side Bar
dashboard = st.Page("./fitur/dashboard.py", title="dashboard")
pemasukan = st.Page("./fitur/pemasukan.py", title="pemasukan.py")
pengeluaran = st.Page("./fitur/pengeluaran.py", title="pengeluaran.py")
donatur = st.Page("./fitur/donatur.py", title="donatur.py")

st.set_page_config(
    page_title="keuangan yayasan",
    page_icon="./img/logo.jpeg"
)
pg = st.navigation(
    {

        "Dashboard": [dashboard],
        "Transaksi": [pemasukan,pengeluaran,donatur]


    }


)

class Keuangan:
    def __init__(self):
        self.pemasukan_list = []

    def tambah_pemasukan(self, pemasukan):
        self.pemasukan_list.append(pemasukan)

    def total_pemasukan(self):
        return sum(pemasukan.nilai for pemasukan in self.pemasukan_list )

    def laporan_pemasukan(self):
        return [
            {"Keterangan": pemasukan.keterangan, "Nilai Pemasukan": pemasukan.nilai}
            for pemasukan in self.pemasukan_list
        ]

if "keuangan" not in st.session_state:
    st.session_state.keuangan = Keuangan()


pg.run()
