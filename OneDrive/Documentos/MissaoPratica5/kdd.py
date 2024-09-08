import time
lista = list()
with open('texto.txt', 'r') as arquivo:
    for linha in arquivo:
        palavras = linha.split()
        lista.extend(palavras)
    #for palavra in lista:
        #print(palavra)
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if j>j+1:
                valorJ = array[j]
                array[j] = array[j+1]
                array[j+1] = valorJ
inicio_bubble = time.time()
bubbleSort(lista)
print (lista)
fim_bubble = time.time()
tempo_execucao_bubble = fim_bubble - inicio_bubble
print(tempo_execucao_bubble)

for i in range(len(lista)):
    valor = i
for j in range(i+1, len(lista)):
    if valor> j:
        valor = j
        i = valor
        valor = i
inicio_select = time.time()
print(lista)
fim_select = time.time()
tempo_execucao_select = fim_select - inicio_select
print(tempo_execucao_select)

lista.sort()
inicio_sort = time.time()
print(lista)
fim_sort = time.time()
tempo_execucao_sort = fim_sort - inicio_sort
print(tempo_execucao_sort)