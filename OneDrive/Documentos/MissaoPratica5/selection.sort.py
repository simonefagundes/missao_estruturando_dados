arrayNumerico = [4,8,10,12,14,18,20,24,28,2,16,18,22,26,28]
for i in range(len(arrayNumerico)):
    valor = i
for j in range(i+1, len(arrayNumerico)):
    if valor> j:
        valor = j
        i = valor
        valor = i
print(arrayNumerico)