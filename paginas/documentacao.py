import streamlit as st

def run():
    st.title("📘 Documentação do Dashboard")

    st.markdown("""
    ## Objetivo do Dashboard

    Este dashboard tem como objetivo **visualizar, explorar e entender os padrões de incêndios florestais no Brasil** ao longo dos anos. Através dele, é possível analisar:

    - A evolução temporal dos incêndios
    - A distribuição geográfica por estado
    - Variações mensais
    - Comparações entre estados e anos

    É uma ferramenta útil tanto para **análises exploratórias** quanto para **comunicação de dados ambientais**.

    ---

    ## Como Navegar entre as Seções

    A navegação principal do dashboard é feita pela **barra lateral**, onde você encontra as seguintes páginas:

    - **Home:** Apresenta uma introdução ao dashboard.
    - **Gráficos:** Exibe os principais gráficos de visualização dos dados.
    - **Dados:** Permite a visualização direta da tabela filtrada.
    - **Documentação:** Você está aqui! Esta seção explica o funcionamento do app.

    Use o menu lateral para alternar entre elas facilmente.

    ---

    ## Como os Filtros Funcionam

    A barra lateral também contém **filtros interativos**, que impactam diretamente os dados exibidos nas páginas de gráficos e dados:

    - **Ano(s):** Exibe apenas os registros dos anos selecionados.
    - **Estado(s):** Filtra os dados pelos estados brasileiros onde ocorreram incêndios.
    - **Mês(es):** Permite restringir a análise a meses específicos do ano.

    Sempre que você altera um filtro, os gráficos e tabelas são atualizados automaticamente com os dados correspondentes.

    Esses filtros tornam a análise mais flexível, permitindo focar em períodos ou regiões específicas de interesse.

    ---

    ## Contato

    Para dúvidas, sugestões ou contribuições, entre em contato com o desenvolvedor do projeto.
    """)
