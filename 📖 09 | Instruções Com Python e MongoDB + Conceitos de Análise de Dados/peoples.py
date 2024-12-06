import pandas as pd

# Criando um DataFrame
data = {
    "Nome": ["Ana", "Bruno", "Carlos"],
    "Idade": [22, 35, 28],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Curitiba"]
}
df = pd.DataFrame(data)

# Exibindo os dados
print(df)

# Filtrando por idade maior que 25
filtered_df = df[df["Idade"] > 25]
print("\nPessoas com mais de 25 anos:")
print(filtered_df)
