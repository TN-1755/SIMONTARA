import streamlit as st


def format_rupiah(value):
    return f"Rp {abs(value):,.0f}".replace(",", ".")


def show_monitoring_status(deviasi):

    if deviasi < 0:

        bg = "#4b2328"
        border = "#ef4444"
        title = "🔴 DI BAWAH TARGET"

    elif deviasi > 0:

        bg = "#1b4332"
        border = "#22c55e"
        title = "🟢 DI ATAS TARGET"

    else:

        bg = "#1e293b"
        border = "#64748b"
        title = "🟡 SESUAI TARGET"

    st.markdown("""
<div style="
font-size:26px;
font-weight:700;
color:white;
margin-bottom:6px;
">
🚨 Status Monitoring
</div>
""", unsafe_allow_html=True)

    st.markdown(
    f"""
<div class="card status-card"
     style="
background:{bg};
border-left:6px solid {border};
padding:10px 18px;
border-radius:18px;
margin-bottom:14px;
display:flex;
justify-content:center;
align-items:center;
min-height:42px;
">

<div
style="
color:white;
font-size:22px;
font-weight:700;
">
{title}
</div>

</div>
""",
    unsafe_allow_html=True,
)