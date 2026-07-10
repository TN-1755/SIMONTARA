import streamlit as st


def load_css():

    st.markdown("""
<style>

/* Hilangkan padding atas */
.block-container{
    padding-top:2rem;
}

/* KPI Cards */
div[data-testid="stMetric"]{

    background:white;

    border:1px solid #dce6f2;

    border-radius:14px;

    padding:18px;

    box-shadow:0 3px 10px rgba(0,0,0,.08);

    text-align:center;
}

/* Label KPI */
div[data-testid="stMetricLabel"]{

    justify-content:center;

    font-weight:700;

    color:#4b5563;
}

/* Nilai KPI */
div[data-testid="stMetricValue"]{

    justify-content:center;

    color:#0f172a;

    font-size:28px;
}

</style>
""", unsafe_allow_html=True)