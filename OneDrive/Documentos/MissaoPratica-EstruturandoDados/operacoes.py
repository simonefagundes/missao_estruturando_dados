import numpy as np

dados_alunos = {
    '26': {'nome': 'Maria','1 Bimestre': 8.0, '2 Bimestre': 7.0, '3 Bimestre': 5.0, '4 Bimestre': 9.0},
    '101': {'nome': 'Ana','1 Bimestre': 9.0, '2 Bimestre': 9.0, '3 Bimestre': 8.0, '4 Bimestre': 9.0},
    '13': {'nome': 'João','1 Bimestre': 6.0, '2 Bimestre': 5.0, '3 Bimestre': 5.0, '4 Bimestre': 5.0},
    '37': {'nome': 'Ágatha','1 Bimestre': 8.0, '2 Bimestre': 6.0, '3 Bimestre': 7.5, '4 Bimestre': 9.0},
    '72': {'nome': 'Joaquim','1 Bimestre': 6.0, '2 Bimestre': 5.5, '3 Bimestre': 5.0, '4 Bimestre': 7.0},
    '5': {'nome': 'Félix','1 Bimestre': 10, '2 Bimestre': 8.0, '3 Bimestre': 8.0, '4 Bimestre': 8.0},
}

def media_alunos(dados_alunos):
    for matricula, notas in dados_alunos.items():
        lista_notas = [
            notas.get('1 Bimestre'),
            notas.get('2 Bimestre'),
            notas.get('3 Bimestre'),
            notas.get('4 Bimestre')
        ]
        media_notas = np.mean(lista_notas)
        dados_alunos[matricula]['media'] = media_notas
        print(f'Notas do aluno {matricula}: {lista_notas}')
        print(f'Média do aluno {matricula}: {media_notas}')
    
    return dados_alunos

dados_alunos_atualizados = media_alunos(dados_alunos)


def resultado_alunos(dados_alunos):
    for matricula, aluno in dados_alunos.items():
        media = aluno.get('media')
        if media < 6:
            print(f"Aluno reprovado – Matrícula: {matricula} – Média Final: {media}")
        else:
            print(f"Aluno aprovado – Matrícula: {matricula} – Média Final: {media}")
resultado_alunos(dados_alunos_atualizados)

def alunos_reprovados(dados_alunos):
    for matricula, aluno in dados_alunos.items():
        media = aluno.get('media')
        nome = aluno.get('nome')
        
        if media < 6:
            print(f"Aluno reprovado:{nome} – Matrícula: {matricula} – Média Final: {media}")
alunos_reprovados(dados_alunos)

