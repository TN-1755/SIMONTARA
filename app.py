import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SIMONTARA",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

components.html("""
<script>
var meta = document.createElement('meta');
meta.name = "viewport";
meta.content =
"width=1400, initial-scale=0.25, maximum-scale=5.0, user-scalable=yes";
document.head.appendChild(meta);
</script>
""", height=0)

from components.styles import load_css
from utils.data_loader import (
    load_kpi,
    load_tabel_akun,
    load_tabel_kluster,
    load_detail_kluster,
    load_chart_kluster,
    load_komposisi_realisasi,
)
from components.kpi_cards import show_kpi_cards
from components.header import show_header
from components.deviasi import show_deviasi
from components.monitoring_status import show_monitoring_status
from components.detail_table import show_detail_table
from components.charts import (
    show_comparison_chart,
    show_donut_chart,
)

load_css()

show_header()

kpi = load_kpi()

show_kpi_cards(kpi)

show_deviasi(kpi["selisih"])
show_monitoring_status(kpi["selisih"])



# =====================================
# GRAFIK
# =====================================

df_chart = load_chart_kluster()

show_comparison_chart(df_chart)


# =====================================
# DETAIL
# =====================================

bottom_left, bottom_right = st.columns([2.3, 1])

with bottom_left:

    st.markdown("""
<div style="
font-size:22px;
font-weight:700;
color:white;
margin-bottom:10px;
">
📋 DETAIL REALISASI
</div>
""", unsafe_allow_html=True)

    df_detail = load_detail_kluster()

    show_detail_table(df_detail)

with bottom_right:

    st.markdown("""
<div style="
font-size:22px;
font-weight:700;
color:white;
text-align:center;
margin-top:5px;
margin-bottom:18px;
">
🍩 KOMPOSISI REALISASI
</div>
""", unsafe_allow_html=True)

    df_komposisi = load_komposisi_realisasi()

    show_donut_chart(df_komposisi)


st.markdown("""
<div style="
margin-top:35px;
padding-top:18px;
border-top:1px solid rgba(96,165,250,.18);
text-align:center;
color:#7f94bb;
font-size:13px;
">
Designed & Developed by <b>Axel Sensei</b> • SIMONTARA V2.0
</div>
""", unsafe_allow_html=True)