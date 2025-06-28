import streamlit as st
import pandas as pd
from paginas import home, graficos, dados, documentacao  # importe as páginas

# Configurações da página
st.set_page_config(page_title="Incêndios Florestais - Dashboard", layout="wide")

# Carregando dados
df = pd.read_csv('data/incendiosFlorestais.csv', encoding='cp1252')
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Sidebar - menu de navegação
st.sidebar.title("Navegação")
pagina = st.sidebar.radio("Selecione a página:", ["Home", "Gráficos", "Dados", "Documentação"])

# Sidebar - filtros comuns (para passar para páginas que usam)
st.sidebar.header("Filtros")
anos = sorted(df['year'].unique()) if 'year' in df.columns else []
ano_selecionado = st.sidebar.multiselect("Ano(s)", anos, default=anos)
estados = sorted(df['state'].unique()) if 'state' in df.columns else []
estado_selecionado = st.sidebar.multiselect("Estado(s)", estados, default=estados)
meses = sorted(df['month'].unique()) if 'month' in df.columns else []
mes_selecionado = st.sidebar.multiselect("Mês(es)", meses, default=meses)

# Aplicar filtros
df_filtrado = df[
    df['year'].isin(ano_selecionado) &
    df['state'].isin(estado_selecionado) &
    df['month'].isin(mes_selecionado)
]

# Controlador de páginas
if pagina == "Home":
    home.run()
elif pagina == "Gráficos":
    graficos.run(df_filtrado)
elif pagina == "Dados":
    dados.run(df_filtrado)
elif pagina == "Documentação":
    documentacao.run()