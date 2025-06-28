import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def run(df_filtrado):
    st.subheader("📈 Evolução por ano e número de incêndios")
    
    if {'year', 'number'}.issubset(df_filtrado.columns):
        df_agrupado = df_filtrado.groupby('year')['number'].sum().reset_index()
        st.area_chart(df_agrupado, x='year', y='number')
    else:
        st.warning("Não foi possível plotar o gráfico. Verifique as colunas.")

    # Aqui você coloca o resto dos seus gráficos, adaptados para receber df_filtrado
    # Por exemplo, Gráfico 1
    st.subheader("1. Total de Incêndios por Ano")
    anos_disponiveis = sorted(df_filtrado['year'].dropna().unique())
    ano_min, ano_max = int(min(anos_disponiveis)), int(max(anos_disponiveis))

    intervalo_anos = st.slider(
        "Selecione o intervalo de anos",
        min_value=ano_min,
        max_value=ano_max,
        value=(ano_min, ano_max),
        step=1
    )
    df_anos_filtrado = df_filtrado[(df_filtrado['year'] >= intervalo_anos[0]) & (df_filtrado['year'] <= intervalo_anos[1])]
    total_por_ano = df_anos_filtrado.groupby("year")["number"].sum()

    fig1, ax1 = plt.subplots(figsize=(6, 2))
    ax1.plot(total_por_ano.index, total_por_ano.values, marker='o')
    ax1.set_title(f"Total de Incêndios por Ano ({intervalo_anos[0]} - {intervalo_anos[1]})")
    ax1.set_xlabel("Ano")
    ax1.set_ylabel("Número de Incêndios")
    st.pyplot(fig1)

    # Gráfico 2 - Barras
    st.subheader("2. Top 10 Estados com Mais Incêndios")
    top_estados = df_filtrado.groupby("state")["number"].sum().sort_values(ascending=False).head(10)
    fig2, ax2 = plt.subplots(figsize=(6, 2) )
    top_estados.plot(kind='bar', color='firebrick', ax=ax2)
    ax2.set_title("Top 10 Estados com Mais Incêndios")
    ax2.set_xlabel("Estado")
    ax2.set_ylabel("Número Total")
    st.pyplot(fig2)

    # Gráfico 3 - Caixa
    st.subheader("3. Distribuição Mensal de Incêndios")
    fig3, ax3 = plt.subplots(figsize=(6, 2))
    df_filtrado.boxplot(column="number", by="month", ax=ax3)
    ax3.set_title("Distribuição Mensal dos Incêndios")
    ax3.set_xlabel("Mês")
    ax3.set_ylabel("Número de Incêndios")
    st.pyplot(fig3)

    # Gráfico 4 - Heatmap por Estado ou Todos
    st.subheader("4. Heatmap de Incêndios por Estado e Mês")

    # Lista de estados + opção "Todos"
    estados_disponiveis = sorted(df_filtrado['state'].unique())
    opcoes_estados = ["Todos"] + estados_disponiveis

    # Dropdown
    estado_escolhido = st.selectbox("Selecione o estado", options=opcoes_estados)

    # Lógica para heatmap
    if estado_escolhido == "Todos":
        heatmap_data = df_filtrado.pivot_table(
            values="number", index="state", columns="month", aggfunc="sum"
        )
    else:
        heatmap_data = df_filtrado[df_filtrado['state'] == estado_escolhido] \
            .pivot_table(values="number", index="state", columns="month", aggfunc="sum")

    # Exibe o heatmap se houver dados
    if not heatmap_data.empty:
        fig4, ax4 = plt.subplots(figsize=(8, 4 if estado_escolhido == "Todos" else 2.5))
        sns.heatmap(heatmap_data, cmap="YlOrRd", linewidths=0.5, ax=ax4)
        titulo = (
            "Heatmap de Incêndios por Estado e Mês"
            if estado_escolhido == "Todos"
            else f"Heatmap de Incêndios - {estado_escolhido}"
        )
        ax4.set_title(titulo, fontsize=10)
        st.pyplot(fig4)
    else:
        st.info(f"Sem dados disponíveis para a seleção atual.")

    # Gráfico 5 - Interativo com Plotly
    st.subheader("5. Incêndios por Estado ao Longo dos Anos (Interativo)")
    df_grouped = df_filtrado.groupby(["year", "state"])["number"].sum().reset_index()
    fig5 = px.line(df_grouped, x="year", y="number", color="state",
                labels={"number": "Número de Incêndios", "year": "Ano", "state": "Estado"},
                title="Incêndios por Estado ao Longo dos Anos")
    fig5.update_layout(template="plotly_white")
    st.plotly_chart(fig5, use_container_width=True)

