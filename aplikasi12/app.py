import streamlit as st

# Side Bar
dashboard = st.Page("./fitur/dashboard.py", title="dashboard")
nabung = st.Page("./fitur/nabung.py", title="nabung.py")
penarikan = st.Page("./fitur/penarikan.py", title="penarikan.py")

pg = st.navigation(
    {

        "Dashboard": [dashboard],
        "Transaksi": [nabung,penarikan],


    }


)

if 'jumlah' not in st.session_state:
    st.session_state['jumlah'] = []

pg.run()



#fungsi untuk menyimpan dan menghitung total nabung
