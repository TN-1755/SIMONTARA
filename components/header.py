import streamlit as st
from datetime import datetime


def show_header():

    now = datetime.now()

    tanggal = now.strftime("%d %b %Y")
    jam = now.strftime("%H:%M WIB")

    st.markdown(
        f"""
<div style="
background:linear-gradient(135deg,#1e3a8a,#0f172a);
padding:28px 32px;
border-radius:20px;
border:1px solid #274472;
box-shadow:0 10px 28px rgba(0,0,0,.35);
margin-bottom:25px;
">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
">

<div>

<div style="
font-size:34px;
font-weight:700;
color:white;
">

📊 SIMONTARA

</div>

<div style="
margin-top:6px;
font-size:20px;
color:#cbd5e1;
">

Sistem Monitoring Tagihan dan Realisasi Anggaran

</div>

</div>

<div style="
text-align:right;
">

<div style="
display:inline-block;
padding:6px 14px;
border-radius:999px;
background:#14532d;
color:#bbf7d0;
font-size:13px;
font-weight:600;
margin-bottom:10px;
">

🟢 GOOGLE SHEETS

</div>

<div style="
font-size:15px;
color:white;
font-weight:600;
">

{tanggal}

</div>

<div style="
font-size:14px;
color:#cbd5e1;
">

{jam}

</div>

</div>

</div>

</div>
""",
        unsafe_allow_html=True,
    )