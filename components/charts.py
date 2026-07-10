import streamlit as st
import plotly.express as px


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
        textposition="outside",
    )

    fig.update_layout(
        title="📊 Capaian Realisasi (%)",
        template="plotly_dark",
        plot_bgcolor="#0f172a",
        paper_bgcolor="#0f172a",
        height=430,
        xaxis=dict(visible=False),
        yaxis=dict(title=""),
        margin=dict(
            l=10,
            r=20,
            t=50,
            b=10,
        ),
    )

    fig.update_yaxes(
    categoryorder="array",
    categoryarray=chart["KLUSTER"].tolist()
)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

def show_deviasi_chart(df):

    chart = df.copy()

    # Hapus baris TOTAL
    chart = chart[chart["KLUSTER"] != "TOTAL"]

    # Ubah format "(34.983.154)" menjadi -34983154
    chart["SELISIH"] = (
        chart["SELISIH"]
        .str.replace("(", "-", regex=False)
        .str.replace(")", "", regex=False)
        .str.replace(".", "", regex=False)
        .astype(int)
    )

    fig = px.bar(
        chart,
        x="SELISIH",
        y="KLUSTER",
        orientation="h",
        text="SELISIH",
    )

    fig.update_traces(
        marker_color="#ef4444",
        textposition="outside",
    )

    fig.update_layout(
        title="📉 Kekurangan Realisasi",
        template="plotly_dark",
        plot_bgcolor="#0f172a",
        paper_bgcolor="#0f172a",
        height=430,
        xaxis=dict(
            visible=False
        ),
        yaxis=dict(
            title=""
        ),
        margin=dict(
            l=10,
            r=20,
            t=50,
            b=10,
        ),
    )

    fig.update_yaxes(
    categoryorder="array",
    categoryarray=chart["KLUSTER"].tolist()
)

    st.plotly_chart(
        fig,
        use_container_width=True
    )