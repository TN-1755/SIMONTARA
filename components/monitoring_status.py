import streamlit as st


def format_rupiah(value):
    return f"Rp {abs(value):,.0f}".replace(",", ".")


def show_monitoring_status(deviasi):

    if deviasi < 0:

        bg = "#4b2328"
        border = "#ef4444"

        title = "🔴 DI BAWAH TARGET"

        subtitle = f"Kekurangan Realisasi {format_rupiah(deviasi)}"

    elif deviasi > 0:

        bg = "#1b4332"
        border = "#22c55e"

        title = "🟢 DI ATAS TARGET"

        subtitle = f"Kelebihan Realisasi {format_rupiah(deviasi)}"

    else:

        bg = "#1e293b"
        border = "#64748b"

        title = "🟡 SESUAI TARGET"

        subtitle = "Realisasi sesuai RPD"

    st.subheader("🚨 Status Monitoring")

    st.markdown(
        f"""
<div style="
background:{bg};
border-left:8px solid {border};
padding:20px;
border-radius:15px;
margin-bottom:30px;
">

<h3 style="color:white;margin:0;">
{title}
</h3>

<p style="
margin-top:8px;
font-size:20px;
color:#f8fafc;
">
{subtitle}
</p>

</div>
""",
        unsafe_allow_html=True
    )