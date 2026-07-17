import streamlit as st

def load_css():

    st.markdown("""
<style>

/* =====================================
   MAIN PAGE
===================================== */

.stApp{

    background:
        radial-gradient(
            circle at top left,
            rgba(59,130,246,.10),
            transparent 35%
        ),

        radial-gradient(
            circle at top right,
            rgba(14,165,233,.08),
            transparent 30%
        ),

        linear-gradient(
            180deg,
            #0f172a,
            #111827
        );

    color:white;

}

.main .block-container{

    width:1400px !important;
    max-width:1400px !important;
    min-width:1400px !important;

    margin:auto;

    padding-top:0 !important;
    padding-left:2rem;
    padding-right:2rem;

}
                
section.main > div{
    padding-top:0 !important;
}
                
[data-testid="stAppViewContainer"]{
    padding-top:0 !important;
}                

section[data-testid="stMain"]{
    padding-top:0 !important;
}

section[data-testid="stMain"] > div{
    padding-top:0 !important;
}

div[data-testid="stMainBlockContainer"]{
    padding-top:0 !important;
}
                
                
[data-testid="stHorizontalBlock"]{

    display:flex !important;

    flex-wrap:nowrap !important;

    align-items:stretch !important;

    gap:1rem;

}

[data-testid="column"]{

    flex:1 1 0 !important;

    min-width:0 !important;

    overflow:visible !important;

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
   KPI CARD HOVER
===================================== */

.kpi-card{

    transition:
        transform .25s ease,
        box-shadow .25s ease,
        border-color .25s ease;
    box-shadow:
        0 6px 18px rgba(0,0,0,.25),
        0 0 12px rgba(59,130,246,.08);

    cursor:pointer;
    position:relative;
    overflow:hidden;
    .kpi-card::before{

    content:"";

    position:absolute;

    top:0;

    left:0;

    width:100%;

    height:1px;

    background:rgba(255,255,255,.12);

}
}

.kpi-card:hover{

    transform:
    translateY(-6px)
    scale(1.01);

border-color:rgba(96,165,250,.45);

box-shadow:
    0 18px 36px rgba(0,0,0,.42),
    0 0 22px rgba(96,165,250,.18);

}
                
.kpi-value{

    transition:transform .25s ease;

}

.kpi-card:hover .kpi-value{

    transform:scale(1.05);

}
                     
/* Label KPI */

div[data-testid="stMetricLabel"]{
    justify-content:center !important;
}

div[data-testid="stMetricLabel"] > div{
    justify-content:center !important;
}

div[data-testid="stMetricLabel"] p{
    font-size:18px !important;
    font-weight:800 !important;
    color:#9fb3d9 !important;
    letter-spacing:.6px;
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
    background:linear-gradient(
    180deg,
    #162445 0%,
    #111c36 100%
    );
    border:1px solid rgba(96,165,250,.22);
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
    0 6px 18px rgba(0,0,0,.25),
    0 0 12px rgba(59,130,246,.08);

}

.deviasi-card:hover{

    transform:
    translateY(-6px)
    scale(1.01);

box-shadow:
    0 18px 36px rgba(0,0,0,.42);

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
    0 6px 18px rgba(0,0,0,.25),
    0 0 12px rgba(59,130,246,.08);

}

.status-card:hover{

    transform:
    translateY(-6px)
    scale(1.01);

box-shadow:
    0 18px 36px rgba(0,0,0,.42);

}

/* =====================================
   UNIVERSAL CARD
===================================== */

.card{

    background:linear-gradient(
    180deg,
    #162445 0%,
    #111c36 100%
    );
    border-radius:18px;
    border:1px solid rgba(96,165,250,.22);
    box-shadow:
    0 6px 18px rgba(0,0,0,.25),
    0 0 12px rgba(59,130,246,.08);
    transition:
        transform .25s ease,
        box-shadow .25s ease,
        border-color .25s ease;
    position:relative;
    overflow:hidden;
    .card::before{

    content:"";

    position:absolute;

    top:0;

    left:0;

    width:100%;

    height:1px;

    background:rgba(255,255,255,.12);

}
                
}

.card:hover{

    transform:
    translateY(-6px)
    scale(1.01);

border-color:rgba(96,165,250,.45);

box-shadow:
    0 18px 36px rgba(0,0,0,.42),
    0 0 22px rgba(96,165,250,.18);

}

                
                                      
</style>
""", unsafe_allow_html=True)

