import pandas as pd

dados = {
    'produto': ['Notebook', 'Mouse', 'Teclado', 'Notebook', 'Mouse', 'Monitor'],
    'categoria': ['Eletrônico', 'Acessório', 'Acessório', 'Eletrônico', 'Acessório', 'Eletrônico'],
    'quantidade': [2, 10, 5, 1, 7, 3],
    'preco': [3000, 50, 150, 3200, 50, 1200]
}

df = pd.DataFrame(dados)

df['faturamento'] = df['quantidade'] * df['preco']

print("\n Dados:")
print(df)

print("\n Faturamento total:")
print(df['faturamento'].sum())

print("\n Produto mais vendido:")
print(df.groupby('produto')['quantidade'].sum().idxmax())

print("\n Vendas por categoria:")
print(df.groupby('categoria')['faturamento'].sum())