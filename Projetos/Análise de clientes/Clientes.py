import pandas as pd

dados = {
    'nome': ['Carlos', 'Ana', 'Pedro', 'Julia', 'Marcos'],
    'idade': [17, 22, 35, 30, 15],
    'compras': [100, 250, 300, 150, 80]
}

df = pd.DataFrame(dados)

def classificar_idade(idade):
    if idade < 18:
        return 'Menor'
    elif idade < 30:
        return 'Jovem'
    else:
        return 'Adulto'

df['categoria'] = df['idade'].apply(classificar_idade)

maiores = df[df['idade'] >= 18]

print("\n Clientes maiores de idade:")
print(maiores)

print("\n Média de compras:")
print(df['compras'].mean())

print("\n Compras por categoria:")
print(df.groupby('categoria')['compras'].mean())