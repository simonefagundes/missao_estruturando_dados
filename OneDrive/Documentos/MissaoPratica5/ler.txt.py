lerArquivo = open('loremipsum.txt')
conteudo = lerArquivo.read()
print(conteudo)
print(conteudo.splitlines()[0])
print(conteudo[:3])

with open('loremipsum.txt') as lerArquivo:
    conteudo = lerArquivo.read()
    print(conteudo)