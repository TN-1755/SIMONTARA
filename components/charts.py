import streamlit as st
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def show_realisasi_chart(df):
    st.info("show_realisasi_chart")

def show_deviasi_chart(df):
    st.info("show_deviasi_chart")

def format_rupiah_short(value):

    if value >= 1_000_000_000:
        return f"Rp {value/1_000_000_000:.2f} M"

    elif value >= 1_000_000:
        return f"Rp {value/1_000_000:.1f} Jt"

    elif value >= 1_000:
        return f"Rp {value/1_000:.1f} Rb"

    else:
        return f"Rp {value:,.0f}".replace(",", ".")

def show_donut_chart(df):

    chart = df.copy()
    total = chart["REALISASI"].sum()

    fig = go.Figure(
        data=[
            go.Pie(
                labels=chart["Akun"],
                values=chart["REALISASI"],

                hole=0.78,

                textinfo="none",
                texttemplate="%{percent:.1%}",

                textfont=dict(
                color="white",
                size=16,
                family="Segoe UI",
            ),

                marker=dict(
                colors=[
                    "#3B82F6",
                    "#22C55E",
                    "#F59E0B",
                ],
                line=dict(
                    color="#0f172a",
                    width=3,
                ),
            ),

                hovertemplate=
                "<b style='font-size:16px'>Akun %{label}</b><br><br>"
                "💰 Realisasi<br>"
                "<b>Rp %{value:,.0f}</b><br><br>"
                "📊 Persentase : <b>%{percent}</b>"
                "<extra></extra>",
            )
        ]
    )

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",

        margin=dict(
        l=10,
        r=10,
        t=10,
        b=25,
    ),

        transition=dict(
            duration=700,
        ),

        height=380,

        showlegend=True,

        legend=dict(
        orientation="h",
        x=0.5,
        y=-0.08,
        xanchor="center",

        font=dict(
            size=13,
            color="white",
            family="Segoe UI",
        ),

        bgcolor="rgba(0,0,0,0)",
    )
)
    
    fig.add_annotation(
    x=0.5,
    y=0.5,

    text=(
        "<br>"
        f"<b style='font-size:22px;color:white;'>{format_rupiah_short(total)}</b>"
    ),

    showarrow=False,

    xanchor="center",
    yanchor="middle",

    align="center",
)


    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False},
    )

def show_kluster(df):
    st.info("show_kluster")

def show_comparison_chart(df):

    chart = df.copy()

    # Hilangkan baris TOTAL
    chart = chart[chart["KLUSTER"] != "TOTAL"].reset_index(drop=True)

    # Persentase
    chart["PERSENTASE"] = (
        chart["PERSENTASE"]
        .str.replace("%", "", regex=False)
        .astype(float)
    )

    # Selisih
    chart["SELISIH"] = (
        chart["SELISIH"]
        .str.replace("(", "-", regex=False)
        .str.replace(")", "", regex=False)
        .str.replace(".", "", regex=False)
        .astype(int)
    )

    # Label angka
    chart["LABEL"] = (
        chart["SELISIH"]
        .abs()
        .map(lambda x: f"{x:,.0f}".replace(",", "."))
    )

    # Bar selalu ke kiri
    chart["BAR"] = -chart["SELISIH"].abs()

    # Warna
    chart["COLOR"] = chart["SELISIH"].apply(
    lambda x: (
        "#EF4444" if x < 0
        else "#3B82F6" if x == 0
        else "#22C55E"
    )
)

    fig = make_subplots(
    rows=1,
    cols=3,
    shared_yaxes=True,
    horizontal_spacing=0.015,
    column_widths=[0.44, 0.12, 0.44],

    subplot_titles=(
    "📈 CAPAIAN REALISASI",
    "",
    "📉 KEKURANGAN REALISASI",
),
)

    fig.add_trace(
        go.Bar(
            x=chart["PERSENTASE"],
            y=chart["KLUSTER"],
            orientation="h",

            marker=dict(
                color="#60A5FA",
            ),

            text=chart["PERSENTASE"].round().astype(int).astype(str) + "%",
            textposition="inside",
            insidetextanchor="middle",

            textfont=dict(
                color="white",
                size=15,
            ),

            hovertemplate="<b>%{y}</b><br>%{x:.0f}%<extra></extra>",
            showlegend=False,
        ),
        row=1,
        col=1,
    )

    fig.add_trace(
        go.Scatter(
            x=[0] * len(chart),
            y=chart["KLUSTER"],

            mode="text",

            text=chart["KLUSTER"],
            textposition="middle center",

            textfont=dict(
            color="white",
            size=19,
            family="Segoe UI Semibold",
        ),

            hoverinfo="skip",
            showlegend=False,
        ),
        row=1,
        col=2,
    )

    fig.add_trace(
        go.Bar(
            x=chart["BAR"],
            y=chart["KLUSTER"],
            orientation="h",

            marker=dict(
                color=chart["COLOR"],
            ),

            text=chart["LABEL"],
            textposition="inside",
            insidetextanchor="middle",

            textfont=dict(
                color="white",
                size=15,
            ),

            hovertemplate="<b>%{y}</b><br>Rp %{text}<extra></extra>",
            showlegend=False,
        ),
        row=1,
        col=3,
    )

    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor="#0f172a",
        paper_bgcolor="#0f172a",

        height=430,

        margin=dict(
        l=0,
        r=0,
        t=30,
        b=10,
    ),

        bargap=0.20,

        showlegend=False,
    )

        # Kolom kiri
    fig.update_xaxes(
        visible=False,
        showgrid=False,
        zeroline=False,
        fixedrange=True,
        row=1,
        col=1,
    )

    # Kolom tengah
    fig.update_xaxes(
        visible=False,
        range=[-1, 1],
        fixedrange=True,
        row=1,
        col=2,
    )

    # Kolom kanan
    fig.update_xaxes(
        visible=False,
        showgrid=False,
        zeroline=False,
        fixedrange=True,
        row=1,
        col=3,
    )


    max_bar = chart["BAR"].abs().max()

    fig.update_xaxes(
        range=[-max_bar * 1.1, 0],
        row=1,
        col=3,
    )

    fig.update_yaxes(
        visible=False,
        fixedrange=True,
        autorange="reversed",
        categoryorder="array",
        categoryarray=chart["KLUSTER"].tolist(),
    )

    for annotation in fig.layout.annotations:

        annotation.font.size = 19
        annotation.font.family = "Segoe UI Black"

    if annotation.text == "📈 CAPAIAN REALISASI":
        annotation.font.color = "#93C5FD"

    elif annotation.text == "📉 KEKURANGAN REALISASI":
        annotation.font.color = "#FCA5A5"

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False},
    )