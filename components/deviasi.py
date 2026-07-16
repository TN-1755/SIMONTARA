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
        border-radius:18px;
        padding:10px 20px;
        margin:14px 0;
        text-align:center;
        background:#111827;
">

<div
style="
font-size:18px;
font-weight:700;
color:{border_color};
margin-bottom:4px;
">
⚠️ DEVIASI
</div>

<div
class="deviasi-value"
style="
font-size:40px;
font-weight:700;
color:white;
line-height:1.1;
">
{format_rupiah(deviasi)}
</div>

</div>
""",
    unsafe_allow_html=True,
)