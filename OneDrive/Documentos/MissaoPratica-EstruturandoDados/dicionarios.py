meu_dicionario = {'codigo 1': 'linguagem = Python', 'codigo 2': 'linguagem = Java', 'codigo 3': 'linguagem = PHP'}
print(meu_dicionario)
print(type(meu_dicionario))
print(meu_dicionario.get('linguagem'))
tamanho_dicionario = len(meu_dicionario)
print(tamanho_dicionario)

dicionario_frutas = {
    1: {"nome": "limão", "tipo": "ácida"},
    2: {"nome": "laranja", "tipo": "ácida"},
    3: {"nome": "manga", "tipo": "semiácida"},
    4: {"nome": "maça", "tipo": "semiácida"},
    5: {"nome": "banana", "tipo": "doce"},
    6: {"nome": "mamão", "tipo": "doce"}
}
print(dicionario_frutas[1])
print(dicionario_frutas[2])

for chave, valor in dicionario_frutas.items():
    print(chave,valor)
