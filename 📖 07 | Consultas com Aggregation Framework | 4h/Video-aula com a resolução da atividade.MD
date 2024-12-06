```javascript
db.getCollection('alunos').aggregate([
  { $match: { turma: '1º ano' } },
  { $unwind: { path: '$notas' } },
  {
    $group: {
      _id: '$_id',
      nome: { $first: '$nome' },
      turma: { $first: '$turma' },
      media_notas: { $avg: '$notas.nota' }
    }
  },
  { $sort: { media_notas: -1 } },
  {
    $project: {
      _id: 1,
      nome: 1,
      turma: 1,
      media_notas: 1
    }
  }
]);

DICA: ao invés de $group, vocês poderiam ir direto para o estágio $project, e adicionar o $avg dentro de $project mesmo. Testem!!

Clique aqui para assistir à videoaula com a resolução da atividade ```