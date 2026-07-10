import streamlit as st

def show_kpi_cards(kpi):

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.metric(
            label="🏛️ PAGU",
            value=kpi["pagu"]
        )

    with c2:
        st.metric(
            label="💰 RPD",
            value=kpi["rpd"]
        )

    with c3:
        st.metric(
            label="✅ REALISASI",
            value=kpi["realisasi"]
        )

    with c4:
        st.metric(
            label="📈 PERSENTASE",
            value=kpi["persentase"]
        )

    with c5:
        st.metric(
            label="⚠️ SELISIH",
            value=kpi["selisih"]
        )