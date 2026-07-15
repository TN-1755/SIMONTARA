import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from utils.config import SPREADSHEET_ID

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets.readonly"
]


@st.cache_resource
def connect_google_sheet():
    credentials = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=SCOPES
    )

    client = gspread.authorize(credentials)

    return client.open_by_key(SPREADSHEET_ID)


def get_sheet():
    spreadsheet = connect_google_sheet()
    return spreadsheet.worksheet("Data")


def parse_number(value):
    """
    Mengubah format Google Sheets menjadi angka.

    Contoh:
    "22.677.936.000" -> 22677936000
    "(1.661.026.274)" -> -1661026274
    """

    value = value.strip()

    negative = value.startswith("(") and value.endswith(")")

    value = (
        value.replace("(", "")
             .replace(")", "")
             .replace(".", "")
             .replace(",", ".")
             .replace("Rp", "")
             .strip()
    )

    number = float(value)

    if negative:
        number *= -1

    return number

def load_kpi():

    ws = get_sheet()

    values = ws.get("C2:C6")

    return {
    "pagu": parse_number(values[0][0]),
    "rpd": parse_number(values[1][0]),
    "realisasi": parse_number(values[2][0]),
    "persentase": values[3][0],
    "selisih": parse_number(values[4][0]),
}

@st.cache_data(ttl=60)
def load_tabel_akun():

    ws = get_sheet()

    values = ws.get("B8:E12")

    header = values[0]
    data = values[1:]

    return pd.DataFrame(data, columns=header)

@st.cache_data(ttl=60)
def load_tabel_kluster():

    ws = get_sheet()

    values = ws.get("B15:F24")

    header = values[0]
    data = values[1:]

    return pd.DataFrame(data, columns=header)

@st.cache_data(ttl=60)
def load_detail_kluster():

    ws = get_sheet()

    values = ws.get("B26:G35")

    header = values[0]
    data = values[1:]

    return pd.DataFrame(data, columns=header)

@st.cache_data(ttl=60)
def load_chart_realisasi():

    ws = get_sheet()

    values = ws.get("B15:D22")

    header = values[0]
    data = values[1:]

    return pd.DataFrame(data, columns=header)

@st.cache_data(ttl=60)
def load_chart_kluster():

    ws = get_sheet()

    values = ws.get("B15:G24")

    header = values[0]
    data = values[1:]

    df = pd.DataFrame(data, columns=header)

    # Bersihkan spasi pada nama kolom
    df.columns = df.columns.str.strip()

    # Hapus baris TOTAL
    df = df[df["KLUSTER"] != "TOTAL"]

    return df.reset_index(drop=True)

@st.cache_data(ttl=60)
def load_komposisi_realisasi():

    ws = get_sheet()

    values = ws.get("B8:D12")

    header = values[0]
    data = values[1:]

    df = pd.DataFrame(data, columns=header)

    df.columns = df.columns.str.strip()

    # Hapus TOTAL
    df = df[df["Akun"] != "TOTAL"].reset_index(drop=True)

    # REALISASI menjadi angka
    df["REALISASI"] = (
        df["REALISASI"]
        .str.replace(".", "", regex=False)
        .astype(int)
    )

    return df