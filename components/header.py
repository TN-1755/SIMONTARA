import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo


def show_header():

    now = datetime.now(ZoneInfo("Asia/Jakarta"))

    tanggal = now.strftime("%d %b %Y")
    jam = now.strftime("%H:%M WIB")

    st.markdown(
        f"""
<div style="
background:linear-gradient(135deg,#1e3a8a,#0f172a);
padding:16px 28px;
border-radius:20px;
border:1px solid #274472;
box-shadow:0 10px 28px rgba(0,0,0,.35);
margin-top:32px;
margin-bottom:18px;
">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
">

<div>

<div style="
display:flex;
align-items:center;
gap:14px;
">

<div style="
font-size:44px;
line-height:1;
">
📊
</div>

<div style="
font-size:40px;
font-weight:800;
letter-spacing:1px;
color:white;
line-height:1;
">
SIMONTARA
</div>

</div>

<div style="
margin-top:4px;
font-size:16px;
letter-spacing:.3px;
color:#cbd5e1;
">
Sistem Monitoring Tagihan dan Realisasi Anggaran
</div>

</div>

<div style="
text-align:right;
">

<div style="
font-size:16px;
font-weight:600;
color:white;
">
{tanggal}
</div>

<div style="
font-size:15px;
color:#cbd5e1;
margin-top:2px;
">
{jam}
</div>

</div>

</div>

</div>
""",
    unsafe_allow_html=True,
)