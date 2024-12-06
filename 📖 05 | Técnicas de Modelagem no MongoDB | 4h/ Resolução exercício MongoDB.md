Comandos MongoDB para realizar as tarefas:

// Tarefa 1
use livraria
db.createCollection("livros")
db.createCollection("autores")
db.createCollection("pedidos")

// Tarefa 2
db.livros.insertMany([
{titulo: "O Senhor dos Anéis", autor: "J.R.R. Tolkien", preco: 50, quantidade: 10},
{titulo: "Harry Potter", autor: "J.K. Rowling", preco: 40, quantidade: 15}
])
db.autores.insertMany([
{nome: "J.R.R. Tolkien", dataNascimento: "1892-01-03"},
{nome: "J.K. Rowling", dataNascimento: "1965-07-31"}
])
db.pedidos.insertMany([
{dataPedido: "2022-01-01", total: 100, livros: [
{titulo: "O Senhor dos Anéis", quantidade: 2},
{titulo: "Harry Potter", quantidade: 1}
]}
])

// Tarefa 3
db.livros.updateOne({titulo: "O Senhor dos Anéis"}, {$set: {preco: 55}})
db.autores.insertOne({nome: "George R.R. Martin", dataNascimento: "1948-09-20"})
db.pedidos.updateOne({}, {$push: {livros: {titulo: "A Song of Ice and Fire", quantidade: 1}}})

// Tarefa 4
db.livros.deleteOne({titulo: "Harry Potter"})
