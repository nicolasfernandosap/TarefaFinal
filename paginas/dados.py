import streamlit as st

def run(df_filtrado):
    st.subheader("🔍 Dados filtrados")
    st.dataframe(df_filtrado)
