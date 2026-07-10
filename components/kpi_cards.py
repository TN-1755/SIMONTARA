import streamlit as st


def format_rupiah(value):
    return f"Rp {value:,.0f}".replace(",", ".")


def show_kpi_cards(kpi):

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            label="🏛️ PAGU",
            value=format_rupiah(kpi["pagu"])
        )

    with c2:
        st.metric(
            label="💰 RPD",
            value=format_rupiah(kpi["rpd"])
        )

    with c3:
        st.metric(
            label="✅ REALISASI",
            value=format_rupiah(kpi["realisasi"])
        )

    with c4:
        st.metric(
            label="📈 PERSENTASE",
            value=kpi["persentase"]
        )