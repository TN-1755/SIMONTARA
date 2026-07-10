import streamlit as st
from datetime import datetime

def show_header():

    kiri, kanan = st.columns([3, 1])

    with kiri:
        st.title("📊 SIMONTARA 2.0")
        st.caption("Sistem Monitoring Tagihan dan Realisasi Anggaran")

    with kanan:
        st.metric(
            "Last Update",
            datetime.now().strftime("%d-%m-%Y %H:%M")
        )

    st.divider()