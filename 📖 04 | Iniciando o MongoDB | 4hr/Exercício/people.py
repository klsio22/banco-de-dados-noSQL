from pymongo import MongoClient

# Configurar a conexão com o MongoDB
conn = "mongodb://127.0.0.1:27017/"
client = MongoClient(conn)

# Escolher o banco de dados e a coleção
database = client["MyDataBase"]
people = database["people"]

# Recuperar os dados e exibir
for people in people.find():
    print(people)
