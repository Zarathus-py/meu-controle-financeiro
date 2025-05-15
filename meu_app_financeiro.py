import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Funções auxiliares
# -------------------------------

@st.cache_data
def carregar_dados(caminho: str) -> pd.DataFrame:
    df = pd.read_excel(caminho)
    df["Data"] = pd.to_datetime(df["Data"], dayfirst=True, errors="coerce")
    df["Mês"] = df["Data"].dt.strftime("%B/%Y")
    return df

def formatar_moeda(valor):
    return f"R$ {valor:,.2f}"

def calcular_total_por_categoria(df: pd.DataFrame) -> pd.DataFrame:
    resumo = df.groupby("Categoria")["Valor"].sum().reset_index()
    resumo["Valor"] = resumo["Valor"].map(formatar_moeda)
    return resumo

def calcular_total_por_mes(df: pd.DataFrame) -> pd.DataFrame:
    resumo = df.groupby("Mês")["Valor"].sum().reset_index()
    resumo["Valor"] = resumo["Valor"].map(formatar_moeda)
    return resumo

def grafico_categoria(df_filtrado: pd.DataFrame, categoria: str):
    agrupado = df_filtrado.groupby("Data")["Valor"].sum().reset_index()
    fig, ax = plt.subplots()
    ax.bar(agrupado["Data"], agrupado["Valor"], color="#4b8bbe")
    ax.set_title(f"Gastos diários - {categoria}", fontsize=14)
    ax.set_ylabel("Valor (R$)")
    ax.set_xlabel("Data")
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

# -------------------------------
# Aplicativo Streamlit
# -------------------------------

st.title("Dashboard de Gastos Pessoais")

df = carregar_dados("Gastos_Pessoais.xlsx")

st.subheader("Visualização da Planilha")
st.dataframe(df)

with st.expander("Colunas disponíveis"):
    st.write(df.columns.tolist())

st.subheader("Total de Gastos por Categoria")
resumo_categoria = calcular_total_por_categoria(df)
st.dataframe(resumo_categoria)

st.subheader("Total de Gastos por Mês")
resumo_mensal = calcular_total_por_mes(df)
st.dataframe(resumo_mensal)

st.subheader("Filtro por Categoria")

categorias = sorted(df["Categoria"].dropna().unique())
categoria_escolhida = st.selectbox("Escolha uma categoria:", categorias)

df_filtrado = df[df["Categoria"] == categoria_escolhida]

st.markdown(f"**Gastos da categoria _{categoria_escolhida}_**")
st.dataframe(df_filtrado)

st.subheader("Evolução dos gastos por data")
grafico_categoria(df_filtrado, categoria_escolhida)
