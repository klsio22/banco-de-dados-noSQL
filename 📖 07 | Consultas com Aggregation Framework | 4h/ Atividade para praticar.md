### Suponha que você tenha uma coleção chamada "alunos" com os seguintes documentos:

db.alunos.insertMany([
  {
    "nome": "João",
    "turma": "1º ano",
    "notas": [
      {
        "disciplina": "Matemática",
        "nota": 8
      },
      {
        "disciplina": "Português",
        "nota": 9
      },
      {
        "disciplina": "História",
        "nota": 7
      }
    ]
  },
  {
    "nome": "Maria",
    "turma": "2º ano",
    "notas": [
      {
        "disciplina": "Geografia",
        "nota": 8
      },
      {
        "disciplina": "Ciências",
        "nota": 9
      },
      {
        "disciplina": "Literatura",
        "nota": 8
      }
    ]
  },
  {
    "nome": "Pedro",
    "turma": "1º ano",
    "notas": [
      {
        "disciplina": "Matemática",
        "nota": 9
      },
      {
        "disciplina": "Português",
        "nota": 8
      },
      {
        "disciplina": "História",
        "nota": 9
      }
    ]
  },
  {
    "nome": "Ana",
    "turma": "2º ano",
    "notas": [
      {
        "disciplina": "Geografia",
        "nota": 7
      },
      {
        "disciplina": "Ciências",
        "nota": 8
      },
      {
        "disciplina": "Literatura",
        "nota": 9
      }
    ]
  },
  {
    "nome": "Luiz",
    "turma": "1º ano",
    "notas": [
      {
        "disciplina": "Matemática",
        "nota": 8
      },
      {
        "disciplina": "Português",
        "nota": 9
      },
      {
        "disciplina": "História",
        "nota": 8
      }
    ]
  }
])

Tarefa:

Encontre todos os alunos do 1º ano.
2. Expanda o campo "notas" em documentos separados.
3. Calcule a média das notas de cada aluno.
4. Ordene os resultados por média em ordem decrescente.
5. Retorne apenas os campos "_id", "nome", "turma" e "media_notas".
Dicas:

estágio 1 : match com 1º ano
estágio 2: unwind de notas
estágio 3: group com id, turma e notas
para calcular a média use: media_notas: {
 $avg: "$notas.nota"
 }
Se ocorrer um erro de "must be an acumulator", use o operador first para agrupar os dados apenas do primeiro documento. Exemplo: 
nome: {$first: '$nome'},
turma: {$first: '$turma'},
estágio 4: sort de média_notas
estágio 5: project id, turma e media_notas