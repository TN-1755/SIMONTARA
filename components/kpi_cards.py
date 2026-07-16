import streamlit as st


def format_rupiah(value):
    return f"Rp {value:,.0f}".replace(",", ".")


def show_kpi_card(icon, title, value):

    st.markdown(
    f"""
<div class="kpi-card"
style="
background:#111c36;
border:1px solid #274472;
border-radius:18px;
padding:18px 22px;
text-align:center;
">

<div style="
color:#9fb3d9;
font-size:18px;
font-weight:800;
margin-bottom:10px;
">
{icon} {title}
</div>

<div style="
color:white;
font-size:30px;
font-weight:700;
white-space:nowrap;
overflow:hidden;
text-overflow:ellipsis;
">
{value}
</div>

</div>
""",
    unsafe_allow_html=True,
)


def show_kpi_cards(kpi):

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        show_kpi_card(
            "🏛️",
            "PAGU",
            format_rupiah(kpi["pagu"])
        )

    with c2:
        show_kpi_card(
            "💰",
            "RPD",
            format_rupiah(kpi["rpd"])
        )

    with c3:
        show_kpi_card(
            "✅",
            "REALISASI",
            format_rupiah(kpi["realisasi"])
        )

    with c4:
        show_kpi_card(
            "📈",
            "PERSENTASE",
            kpi["persentase"]
        )