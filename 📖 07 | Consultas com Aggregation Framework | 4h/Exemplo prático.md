### Suponha que você tenha uma coleção chamada "pedidos" com os seguintes documentos:

db.pedidos.insertMany([
  {
    "cliente": "João",
    "data": ISODate("2022-01-01T00:00:00.000Z"),
    "itens": [
      {
        "produto": "Notebook",
        "quantidade": 2,
        "preco": 2000
      },
      {
        "produto": "Mouse",
        "quantidade": 1,
        "preco": 50
      }
    ]
  },
  {
    "cliente": "Maria",
    "data": ISODate("2022-01-15T00:00:00.000Z"),
    "itens": [
      {
        "produto": "Smartphone",
        "quantidade": 1,
        "preco": 1500
      },
      {
        "produto": "Carregador",
        "quantidade": 2,
        "preco": 20
      }
    ]
  },
  {
    "cliente": "Pedro",
    "data": ISODate("2022-01-20T00:00:00.000Z"),
    "itens": [
      {
        "produto": "Tablet",
        "quantidade": 1,
        "preco": 1000
      },
      {
        "produto": "Teclado",
        "quantidade": 1,
        "preco": 100
      }
    ]
  },
  {
    "cliente": "Ana",
    "data": ISODate("2022-01-25T00:00:00.000Z"),
    "itens": [
      {
        "produto": "Câmera",
        "quantidade": 1,
        "preco": 500
      },
      {
        "produto": "Tripé",
        "quantidade": 1,
        "preco": 50
      }
    ]
  },
  {
    "cliente": "Luiz",
    "data": ISODate("2022-02-01T00:00:00.000Z"),
    "itens": [
      {
        "produto": "Notebook",
        "quantidade": 1,
        "preco": 2000
      },
      {
        "produto": "Mouse",
        "quantidade": 2,
        "preco": 50
      }
    ]
  }

{
    "cliente": "Kelly",
    "data": ISODate("2022-02-01T00:00:00.000Z"),
    "itens": [
      {
        "produto": "Notebook",
        "quantidade": 3,
        "preco": 4000
      },
      {
        "produto": "Teclado",
        "quantidade": 1,
        "preco": 100
      }
    ]
    }
])

Atividade

Encontre todos os pedidos feitos em janeiro de 2022.
2. Expanda o campo "itens" em documentos separados.
3. Calcule o valor total de cada item.
4. Ordene os resultados por valor total em ordem decrescente.
5. Retorne apenas os campos "_id", "cliente", "produto" e "valor_total".
db.pedidos.aggregate([
 {
 $match: {
 data: {
 $gte: ISODate("2022-01-01T00:00:00.000Z"),
 $lt: ISODate("2022-02-01T00:00:00.000Z")
 }
 }
 },
 {
 $unwind: "$itens"
 },
 {
 $project: {
 _id: 1,
 cliente: 1,
 produto: "$itens.produto",
 quantidade: "$itens.quantidade",
 preco: "$itens.preco",
 valor_total: {
 $multiply: ["$itens.quantidade", "$itens.preco"]
 }
 }
 },
 {
 $sort: {
 valor_total: -1
 }
 },
 {
 $project: {
 _id: 1,
 cliente: 1,
 produto: 1,
 valor_total: 1
 }
 }
])

SAÍDA:

[
  {
    _id: ObjectId('67348ec656e7bbf91cfe6916'),
    cliente: 'João',
    produto: 'Notebook',
    valor_total: 4000
  },
  {
    _id: ObjectId('67348ec656e7bbf91cfe6917'),
    cliente: 'Maria',
    produto: 'Smartphone',
    valor_total: 1500
  },
  {
    _id: ObjectId('67348ec656e7bbf91cfe6918'),
    cliente: 'Pedro',
    produto: 'Tablet',
    valor_total: 1000
  },
  {
    _id: ObjectId('67348ec656e7bbf91cfe6919'),
    cliente: 'Ana',
    produto: 'Câmera',
    valor_total: 500
  },
  {
    _id: ObjectId('67348ec656e7bbf91cfe6918'),
    cliente: 'Pedro',
    produto: 'Teclado',
    valor_total: 100
  },
  {
    _id: ObjectId('67348ec656e7bbf91cfe6916'),
    cliente: 'João',
    produto: 'Mouse',
    valor_total: 50
  },
  {
    _id: ObjectId('67348ec656e7bbf91cfe6919'),
    cliente: 'Ana',
    produto: 'Tripé',
    valor_total: 50
  },
  {
    _id: ObjectId('67348ec656e7bbf91cfe6917'),
    cliente: 'Maria',
    produto: 'Carregador',
    valor_total: 40
  }
]