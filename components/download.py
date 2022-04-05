import streamlit as st
from base64 import b64encode

def encode_csv(df):
    csv = df.to_csv(index=False)
    b64 = b64encode(
            csv.encode()
            ).decode()  
    return f'<a href="data:file/csv;base64,{b64}">Descargar CSV</a>'

def download_csv(df):
    st.markdown(
            encode_csv(df),
            unsafe_allow_html=True
            )

