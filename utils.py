from dataset import df
import pandas as pd

def format_number(value, prefix=''):
    for unit in ['','mil']:
        if value < 1000:
            return f"{prefix}{value:.2f} {unit}"
        value /= 1000
    return f"{prefix}{value:.2f} milhões"

# 1 - dataframe para receita por estado
df_receita_estado = df.groupby('Local da compra').agg({
    'Preço': 'sum',
    'lat': 'first',
    'lon': 'first'
}).reset_index()
df_receita_estado = df_receita_estado.sort_values(by='Preço', ascending=False)


# 2 - dataframe receita mensal
df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], dayfirst=True)
df_receita_mensal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='ME'))['Preço'].sum().reset_index()
df_receita_mensal['Ano'] = df_receita_mensal['Data da Compra'].dt.year
df_receita_mensal['Mês'] = df_receita_mensal['Data da Compra'].dt.month_name()
print(df_receita_mensal)

# 3 - Receita por Categoria
df_receita_categoria = df.groupby('Categoria do Produto').agg({
    'Preço': 'sum'
}).reset_index()
df_receita_categoria = df_receita_categoria.sort_values(by='Preço', ascending=False)

# 4 - Receita por Vendedor
df_receita_vendedor = df.groupby('Vendedor').agg({
    'Preço': 'sum',
}).reset_index()
df_receita_vendedor = df_receita_vendedor.sort_values(by='Preço', ascending=False)  
df_receita_vendedor['Quantidade'] = df.groupby('Vendedor').size().values