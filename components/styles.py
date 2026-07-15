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
    padding-bottom:2rem;
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
   SUBHEADER
===================================== */

h3{

    font-weight:700 !important;

    letter-spacing:.3px;

    margin-top:8px !important;

    margin-bottom:18px !important;

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

    box-shadow:0 6px 18px rgba(0,0,0,.25);

    transition:
        transform .25s ease,
        box-shadow .25s ease,
        border-color .25s ease;

    cursor:pointer;
}
                
div[data-testid="stMetric"]:hover{

    transform:translateY(-6px) scale(1.02);

    border-color:#60A5FA;

    box-shadow:
        0 18px 40px rgba(0,0,0,.45),
        0 0 25px rgba(96,165,250,.25);

}

div[data-testid="stMetricValue"]{
    justify-content:center;
    color:white !important;
    font-size:34px;

    transition:transform .25s ease;
}

div[data-testid="stMetric"]:hover div[data-testid="stMetricValue"]{
    transform:scale(1.08);
}

div[data-testid="stMetric"] *{
    transition:all .25s ease;
}

div[data-testid="stMetric"]:hover div[data-testid="stMetricValue"]{

    transform:scale(1.05);

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

    margin-top:48px;

    margin-bottom:48px;

    border:none;

    height:1px;

    background:#243b63;

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

/* =====================================
   DEVIASI CARD
===================================== */

.deviasi-card{

    transition:
        transform .25s ease,
        box-shadow .25s ease;

    box-shadow:
        0 6px 18px rgba(0,0,0,.25);

}

.deviasi-card:hover{

    transform:translateY(-5px);

    box-shadow:
        0 14px 32px rgba(0,0,0,.40);

}

.deviasi-value{

    transition:transform .25s ease;

}

.deviasi-card:hover .deviasi-value{

    transform:scale(1.05);

}

                
/* =====================================
   STATUS MONITORING
===================================== */

.status-card{

    transition:
        transform .25s ease,
        box-shadow .25s ease;

    box-shadow:
        0 6px 18px rgba(0,0,0,.25);

}

.status-card:hover{

    transform:translateY(-5px);

    box-shadow:
        0 14px 32px rgba(0,0,0,.40);

}

/* =====================================
   UNIVERSAL CARD
===================================== */

.card{

    background:#111c36;

    border-radius:18px;

    border:1px solid #274472;

    box-shadow:
        0 6px 18px rgba(0,0,0,.25);

    transition:
        transform .25s ease,
        box-shadow .25s ease,
        border-color .25s ease;

}

.card:hover{

    transform:translateY(-5px);

    border-color:#4f8dfd;

    box-shadow:
        0 14px 32px rgba(0,0,0,.40),
        0 0 18px rgba(79,141,253,.18);

}
                       
</style>
""", unsafe_allow_html=True)

