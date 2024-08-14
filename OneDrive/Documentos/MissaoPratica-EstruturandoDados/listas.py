lista_mesclada = [ 1, 2, 3, "Olá, Python", True, 12.6]
#print(lista_mesclada)

lista_mesclada.append("Lista aninhada")
lista_mesclada.insert(4,5)

#print(lista_mesclada)
tamanho_lista = len(lista_mesclada)
#print(tamanho_lista)
lista_mesclada.remove(1)
print(lista_mesclada)

nova_lista_mesclada = lista_mesclada[:5]
print(nova_lista_mesclada)