import streamlit as st

from components.styles import load_css
from utils.data_loader import (
    load_kpi,
    load_tabel_akun,
    load_tabel_kluster,
    load_detail_kluster,
)
from components.kpi_cards import show_kpi_cards
from components.header import show_header

show_header()

load_css()

kpi = load_kpi()
show_kpi_cards(kpi)

st.divider()

# ==========================
# Tabel Akun
# ==========================
df_akun = load_tabel_akun()
st.dataframe(df_akun)

st.divider()

# ==========================
# Tabel Kluster
# ==========================
df_kluster = load_tabel_kluster()
st.dataframe(df_kluster)

st.divider()

# ==========================
# Detail Kluster
# ==========================
df_detail = load_detail_kluster()
st.dataframe(df_detail)