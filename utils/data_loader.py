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

@st.cache_data(ttl=60)
def load_kpi():

    ws = get_sheet()

    values = ws.get("C2:C6")

    return {
        "pagu": values[0][0],
        "rpd": values[1][0],
        "realisasi": values[2][0],
        "persentase": values[3][0],
        "selisih": values[4][0],
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