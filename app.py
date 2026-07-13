import streamlit as st

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
from components.charts import (
    show_comparison_chart,
    show_donut_chart,
)



show_header()

load_css()

kpi = load_kpi()

show_kpi_cards(kpi)

show_deviasi(kpi["selisih"])
show_monitoring_status(kpi["selisih"])

st.divider()

# =====================================
# GRAFIK
# =====================================

df_chart = load_chart_kluster()
st.write(df_chart.columns.tolist())
st.dataframe(df_chart)

show_comparison_chart(df_chart)

# =====================================
# DETAIL
# =====================================

bottom_left, bottom_right = st.columns(2)

with bottom_left:

    st.subheader("📋 Detail Realisasi per Kluster")

    df_detail = load_detail_kluster()

    st.dataframe(
        df_detail,
        use_container_width=True,
        hide_index=True,
    )

with bottom_right:

    st.subheader("🍩 Komposisi Realisasi")

    df_komposisi = load_komposisi_realisasi()

    show_donut_chart(df_komposisi)