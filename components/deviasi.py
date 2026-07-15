import streamlit as st


def format_rupiah(value):
    return f"Rp {value:,.0f}".replace(",", ".")


def show_deviasi(deviasi):

    border_color = "#ef4444" if deviasi < 0 else "#22c55e"

    st.markdown(
        f"""
<div class="card deviasi-card"
     style="
        border:2px solid {border_color};
        border-radius:20px;
        padding:25px;
        margin:20px 0;
        text-align:center;
        background:#111827;
">

<h3 style="color:{border_color};
           margin-bottom:10px;">
⚠️ DEVIASI
</h3>

<h1 class="deviasi-value"
    style="
        color:white;
        margin:0;
">
{format_rupiah(deviasi)}
</h1>

</div>
""",
        unsafe_allow_html=True,
    )