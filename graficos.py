import plotly.express as px
from utils import df_receita_estado, df_receita_mensal, df_receita_categoria, df_receita_vendedor

grafico_map_estado = px.scatter_geo(
    df_receita_estado,
    lat='lat',
    lon='lon',
    size='Preço',
    scope='south america',
    template='seaborn',
    title='Receita por Estado',
    hover_name='Local da compra',
    hover_data={'lat': False, 'lon': False}
)

grafico_receita_mensal = px.line(
    df_receita_mensal,
    x='Mês',
    y='Preço',
    markers=True,
    range_y=[0, df_receita_mensal.max()],
    color='Ano',
    line_dash='Ano',
    title='Receita Mensal'
)

grafico_receita_mensal.update_layout(yaxis_title='Receita (R$)')

grafico_receita_estado = px.bar(
    df_receita_estado.head(10),
    x='Local da compra',
    y='Preço',
    title='Receita por Estado',
    text_auto=True,
    labels={'Local da compra': 'Estado', 'Preço': 'Receita (R$)'},
    template='seaborn'
)

grafico_receita_categoria = px.bar(
    df_receita_categoria.head(10),
    x='Categoria do Produto',
    y='Preço',
    title='Receita por Categoria',
    text_auto=True,
    labels={'Categoria do Produto': 'Categoria', 'Preço': 'Receita (R$)'},
    template='seaborn'
)

grafico_receita_vendedor = px.bar(
    df_receita_vendedor.head(10),
    x='Vendedor',
    y=['Preço', 'Quantidade'],
    title='Receita por Vendedor',
    text_auto=True,
    labels={'Vendedor': 'Vendedor', 'Preço': 'Receita (R$)'},
    template='seaborn'
)