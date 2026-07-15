import streamlit as st


def show_detail_table(df):

    html = """
    <style>

    .simontara-table{
        width:100%;
        border-collapse:collapse;
        font-family:'Segoe UI',sans-serif;
        font-size:14px;
        overflow:hidden;
        border-radius:12px;
    }

    .simontara-table th{
        background:#1E293B;
        color:white;
        padding:12px;
        text-align:center;
        font-weight:600;
        border-bottom:1px solid #334155;
    }

    .simontara-table td{
        background:#111827;
        color:white;
        padding:10px 12px;
        border-bottom:1px solid rgba(255,255,255,.06);
    }

    .simontara-table td:first-child{
        text-align:left;
        font-weight:600;
    }

    .simontara-table td:not(:first-child){
        text-align:right;
    }

    .simontara-table tr:nth-child(even) td{
        background:#172033;
    }

    .simontara-table tr:hover td{
        background:#22314F;
    }

    .total-row td{
        background:#0F766E !important;
        font-weight:bold;
        color:white;
    }

    </style>

    <table class="simontara-table">

        <thead>
            <tr>
    """

    for col in df.columns:
        html += f"<th>{col}</th>"

    html += "</tr></thead><tbody>"

    for _, row in df.iterrows():

        cls = ""

        if str(row.iloc[0]).upper() == "TOTAL":
            cls = "total-row"

        html += f'<tr class="{cls}">'

        for value in row:
            html += f"<td>{value}</td>"

        html += "</tr>"

    html += "</tbody></table>"

    st.markdown(html, unsafe_allow_html=True)