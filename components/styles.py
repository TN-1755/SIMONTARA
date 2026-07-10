import streamlit as st

def load_css():

    st.markdown("""
<style>

/* =====================================
   MAIN PAGE
===================================== */

.stApp{
    background:#0f172a;
    color:white;
}

.block-container{
    padding-top:2rem;
    max-width:1400px;
}

/* =====================================
   TEXT
===================================== */

h1,h2,h3,h4,h5,h6,p,label{
    color:white !important;
}

hr{
    border-color:#1e293b;
}

/* =====================================
   KPI CARD
===================================== */

div[data-testid="stMetric"]{
    background:#111c36;
    border:1px solid #274472;
    border-radius:18px;
    padding:22px;
    text-align:center;
    box-shadow:0 0 20px rgba(0,0,0,.25);
}

/* Label KPI */

div[data-testid="stMetricLabel"]{
    justify-content:center;
    color:#9fb3d9 !important;
    font-weight:700;
}

/* Nilai KPI */

div[data-testid="stMetricValue"]{
    justify-content:center;
    color:white !important;
    font-size:34px;
}

/* =====================================
   DATAFRAME
===================================== */

div[data-testid="stDataFrame"]{
    border-radius:16px;
    overflow:hidden;
}

/* =====================================
   DIVIDER
===================================== */

hr{
    margin-top:40px;
    margin-bottom:40px;
    border:1px solid #243b63;
}

/* =====================================
   CHART CARD
===================================== */

.chart-card{
    background:#111c36;
    border:1px solid #274472;
    border-radius:18px;
    padding:20px;
    margin-bottom:20px;
    box-shadow:0 0 20px rgba(0,0,0,.20);
}

</style>
""", unsafe_allow_html=True)