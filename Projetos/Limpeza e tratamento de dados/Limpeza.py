import pandas as pd

dados = {
    'nome': ['Ana', 'João', 'Maria', 'Ana', None],
    'idade': [23, None, 29, 23, 35],
    'cidade': ['SP', 'RJ', None, 'SP', 'MG']
}

df = pd.DataFrame(dados)

print("\n Dados originais:")
print(df)

df = df.drop_duplicates()

df['idade'] = df['idade'].fillna(df['idade'].mean())
df['cidade'] = df['cidade'].fillna('Não informado')

df = df.dropna(subset=['nome'])

print("\n Dados tratados:")
print(df)