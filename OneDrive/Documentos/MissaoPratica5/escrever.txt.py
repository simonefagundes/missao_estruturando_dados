with open('texto.txt', 'w') as arquivo:
    texto = list()
    texto.append("I miss you")
    texto.append("I miss you smile")
    texto.append("And I cry sometimes")
    for linha in texto:
        arquivo.write(linha + '\n')