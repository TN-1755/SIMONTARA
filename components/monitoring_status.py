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

    st.subheader("🚨 Status Monitoring")

    st.markdown(
        f"""
<div class="card status-card"
     style="
background:{bg};
border-left:8px solid {border};
padding:20px;
border-radius:15px;
margin-bottom:30px;
">

<h3 style="
color:white;
margin:0;
font-size:22px;
font-weight:700;
">
{title}
</h3>

</div>
""",
        unsafe_allow_html=True
    )