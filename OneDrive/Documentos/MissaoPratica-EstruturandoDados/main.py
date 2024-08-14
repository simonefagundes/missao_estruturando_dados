from operacoes import media_alunos, resultado_alunos, alunos_reprovados
alunos = {
    '26': {'nome': 'Maria','1 Bimestre': 8.0, '2 Bimestre': 7.0, '3 Bimestre': 5.0, '4 Bimestre': 9.0},
    '101': {'nome': 'Ana','1 Bimestre': 9.0, '2 Bimestre': 9.0, '3 Bimestre': 8.0, '4 Bimestre': 9.0},
    '13': {'nome': 'João','1 Bimestre': 6.0, '2 Bimestre': 5.0, '3 Bimestre': 5.0, '4 Bimestre': 5.0},
    '37': {'nome': 'Ágatha','1 Bimestre': 8.0, '2 Bimestre': 6.0, '3 Bimestre': 7.5, '4 Bimestre': 9.0},
    '72': {'nome': 'Joaquim','1 Bimestre': 6.0, '2 Bimestre': 5.5, '3 Bimestre': 5.0, '4 Bimestre': 7.0},
    '5': {'nome': 'Félix','1 Bimestre': 10, '2 Bimestre': 8.0, '3 Bimestre': 8.0, '4 Bimestre': 8.0},
}
media_alunos_chamada = media_alunos(alunos)
resultado_alunos_chamada = resultado_alunos(alunos)
alunos_reprovados_chamada = alunos_reprovados(alunos)