import streamlit as st
import pandas as pd

def run():
    st.title("🔥 Dashboard - Incêndios Florestais no Brasil")
    st.write("Visualização interativa dos incêndios florestais.")

    df = pd.read_csv('data/incendiosFlorestais.csv', encoding='cp1252')
    st.write("Colunas no dataset:", list(df.columns))

    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
