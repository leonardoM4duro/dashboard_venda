import streamlit as st
from dataset import df
import pandas as pd

st.title("DataFrame de Vendas")

with st.expander('Colunas'):
    colunas = st.multiselect(
        'Selecione as colunas para exibir',
        options=df.columns.tolist(),
        default=df.columns.tolist()
    )

st.sidebar.title('Filtros')
with st.sidebar.expander('Categoria do Produto'):
    categoria_produto = st.multiselect(
        'Selecione as categorias do produto para filtrar',
        options=df['Categoria do Produto'].unique(),
        default=df['Categoria do Produto'].unique()
    )
    
with st.sidebar.expander('Preço do Produto'):
    preco = st.slider(
        'Selecione o intervalo de preço',
        min_value=float(df['Preço'].min()),
        max_value=float(df['Preço'].max()),
        value=(float(df['Preço'].min()), float(df['Preço'].max()))
    )
    
with st.sidebar.expander('Data da compra'):
    df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], dayfirst=True)
    data_compra = st.date_input(
        'Selecione a data da compra',
        (pd.to_datetime(df['Data da Compra'], dayfirst=True).min().date(), 
         pd.to_datetime(df['Data da Compra'], dayfirst=True).max().date())
    )

query = """
    `Categoria do Produto` in @categoria_produto and \
    `Preço` >= @preco[0] and `Preço` <= @preco[1] and \
    `Data da Compra` >= @data_compra[0] and `Data da Compra` <= @data_compra[1]
"""
filtro = df.query(query)
filtro = filtro[colunas] if colunas else filtro

st.dataframe(filtro)
