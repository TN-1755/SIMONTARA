import streamlit as st


def show_detail_table(df):

    df = df[df["KLUSTER"] != "TOTAL"].reset_index(drop=True)

    css = """
    <style>

    .simontara-table{
        width:100%;
        border-collapse:collapse;
        font-family:"Segoe UI",sans-serif;
        font-size:14px;
        overflow:hidden;
        border-radius:12px;
    }

    .simontara-table th{
    background:#223454;
    color:white;
    padding:10px 10px;
    text-align:center;
    font-weight:700;
    border-bottom:1px solid #3B82F6;
    }

    .simontara-table td{
        padding:8px 12px;
        color:white;
        border-bottom:1px solid rgba(255,255,255,.05);
    }

    .simontara-table tbody tr:nth-child(odd){
        background:#111827;
    }

    .simontara-table tbody tr:nth-child(even){
        background:#172033;
    }

    .simontara-table tbody tr:hover{
        background:#22314F;
    }

    .simontara-table td:first-child{
        text-align:left;
        font-weight:600;
        white-space:nowrap;
    }

    .simontara-table td:not(:first-child){
        text-align:right;
    }

    .total-header,
    .total-column{
        border-left:3px solid #22C55E;
    }

    .total-header{
        color:#BBF7D0;
    }

    .total-column{
        color:#BBF7D0;
        font-weight:700;
    }

    </style>
    """

    header = "<tr>"

    for col in df.columns:

        if col == "TOTAL":
            header += '<th class="total-header">TOTAL</th>'
        else:
            header += f"<th>{col}</th>"

    header += "</tr>"

    body = ""

    for _, row in df.iterrows():

        body += "<tr>"

        for i, value in enumerate(row):

            if i == len(df.columns) - 1:
                body += f'<td class="total-column">{value}</td>'
            else:
                body += f"<td>{value}</td>"

        body += "</tr>"

    table = f"""
<table class="simontara-table">
    <thead>
        {header}
    </thead>
    <tbody>
        {body}
    </tbody>
</table>
"""

    st.markdown(css + table, unsafe_allow_html=True)