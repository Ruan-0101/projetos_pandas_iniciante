import pandas as pd

dados = {
    'aluno': ['Ana', 'Bruno', 'Carlos', 'Daniela'],
    'nota1': [7, 5, 8, 6],
    'nota2': [6, 4, 9, 7]
}

df = pd.DataFrame(dados)

df['media'] = (df['nota1'] + df['nota2']) / 2

df['status'] = df['media'].apply(lambda x: 'Aprovado' if x >= 6 else 'Reprovado')

print("\n Resultado:")
print(df)

print("\n Média geral da turma:")
print(df['media'].mean())

print("\n Melhor aluno:")
print(df.loc[df['media'].idxmax()])