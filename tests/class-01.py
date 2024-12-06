import pymongo
import pandas as pd

# Conecte ao MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["meu_banco"]
collection = db["clientes"]

# Leia os dados do MongoDB
cursor = collection.find()
data = list(cursor)
df = pd.DataFrame(data)

# Filtre clientes com idade maior que 25 anos
filtered_df = df[df['idade'] > 25]

# Exiba os 5 primeiros clientes filtrados
print(filtered_df.head())
