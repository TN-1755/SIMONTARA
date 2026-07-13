import streamlit as st

print("=== CHARTS LOADED ===")

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def show_realisasi_chart(df):

    chart = df.copy()

    chart["PERSENTASE"] = (
        chart["PERSENTASE"]
        .str.replace("%", "", regex=False)
        .astype(float)
    )

    fig = px.bar(
        chart,
        x="PERSENTASE",
        y="KLUSTER",
        orientation="h",
        text="PERSENTASE",
    )

    fig.update_traces(
    marker_color="#60A5FA",
    texttemplate="%{text:.0f}%",
    textposition="inside",
    insidetextanchor="middle",
    textfont=dict(
        color="white",
        size=14,
    ),
)

    fig.update_layout(
    title="📊 Capaian Realisasi (%)",
    template="plotly_dark",
    plot_bgcolor="#0f172a",
    paper_bgcolor="#0f172a",
    height=430,

    xaxis=dict(
        visible=False,
    ),

    yaxis=dict(
        showticklabels=False,
        showgrid=False,
        zeroline=False,
        title="",
    ),

    margin=dict(
    l=10,
    r=20,
    t=50,
    b=10,
),
)

    fig.update_yaxes(
    showticklabels=False,
    categoryorder="array",
    categoryarray=chart["KLUSTER"].tolist(),
)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

def show_deviasi_chart(df):

    chart = df.copy()

    # Hapus TOTAL
    chart = chart[chart["KLUSTER"] != "TOTAL"].reset_index(drop=True)

    # Konversi ke angka
    chart["SELISIH"] = (
        chart["SELISIH"]
        .str.replace("(", "-", regex=False)
        .str.replace(")", "", regex=False)
        .str.replace(".", "", regex=False)
        .astype(int)
    )

    # Label Rupiah
    chart["LABEL"] = (
        chart["SELISIH"]
        .abs()
        .map(lambda x: f"{x:,.0f}".replace(",", "."))
    )

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=chart["SELISIH"],
            y=list(range(len(chart))),      # ← pakai index, bukan nama kluster
            orientation="h",

            marker_color="#ef4444",

            text=chart["LABEL"],
            textposition="outside",

            textfont=dict(
                color="white",
                size=13,
            ),

            cliponaxis=False,
            hovertemplate="<b>%{customdata}</b><br>Rp %{text}<extra></extra>",
            customdata=chart["KLUSTER"],
        )
    )

    fig.update_layout(
        title="📉 Kekurangan Realisasi",
        template="plotly_dark",
        plot_bgcolor="#0f172a",
        paper_bgcolor="#0f172a",
        height=430,

        margin=dict(
        l=5,
        r=20,
        t=50,
        b=10,
    ),

        xaxis=dict(
            visible=False,
            zeroline=False,
        ),

        yaxis=dict(
            showticklabels=False,
            showgrid=False,
            zeroline=False,
            title="",
        ),
    )

    fig.update_yaxes(
    showticklabels=False,
    categoryorder="array",
    categoryarray=chart["KLUSTER"].tolist(),
)

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

def show_donut_chart(df):

    chart = df.copy()

    # Ubah kolom REALISASI menjadi angka
    chart["REALISASI"] = (
        chart["REALISASI"]
        .str.replace(".", "", regex=False)
        .astype(int)
    )

    fig = px.pie(
    chart,
    names="Akun",
    values="REALISASI",
    hole=0.60,
)

    fig.update_layout(
        showlegend=True,
        legend=dict(
            font=dict(
                color="white",
                size=16,
            )
        )
    )

    fig.update_traces(
    textinfo="percent",
    texttemplate="%{percent:.1%}",
    textposition="inside",
    insidetextorientation="horizontal",
    textfont=dict(
        color="white",
        size=22,
        family="Segoe UI",
    ),
    hovertemplate="<b>Realisasi</b><br>Rp %{value:,.0f}<extra></extra>",
)

    fig.update_layout(
        title="🍩 Komposisi Realisasi per Akun",
        template="plotly_dark",
        plot_bgcolor="#0f172a",
        paper_bgcolor="#0f172a",
        height=430,
        margin=dict(
            l=10,
            r=10,
            t=50,
            b=10,
        ),
        showlegend=True,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )    

def show_kluster(df):

    chart = df.copy()
    chart = chart[chart["KLUSTER"] != "TOTAL"]

    st.markdown(
        """
        <div style="
            height:430px;
            display:flex;
            flex-direction:column;
            justify-content:center;
            margin-top:55px;
        ">
        """,
        unsafe_allow_html=True,
    )

    for kluster in chart["KLUSTER"]:

        st.markdown(
            f"""
            <div style="
                height:52px;
                display:flex;
                justify-content:center;
                align-items:center;

                color:white;
                font-size:15px;
                font-weight:600;
                white-space:nowrap;
            ">
                {kluster}
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)

def show_comparison_chart(df):

    chart = df.copy()
    chart = chart[chart["KLUSTER"] != "TOTAL"].reset_index(drop=True)

    chart["PERSENTASE"] = (
        chart["PERSENTASE"]
        .str.replace("%", "", regex=False)
        .astype(float)
    )

    chart["SELISIH"] = (
        chart["SELISIH"]
        .str.replace("(", "-", regex=False)
        .str.replace(")", "", regex=False)
        .str.replace(".", "", regex=False)
        .astype(int)
    )

    chart["DEVIASI"] = chart["SELISIH"].abs()

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=chart["PERSENTASE"],
            y=chart["KLUSTER"],
            orientation="h",
            marker_color="#60A5FA",
            text=chart["PERSENTASE"].astype(int).astype(str) + "%",
            textposition="inside",
        )
    )

    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor="#0f172a",
        paper_bgcolor="#0f172a",
        title="TEST GRAFIK",
        height=430,
    )

    st.plotly_chart(fig, use_container_width=True)