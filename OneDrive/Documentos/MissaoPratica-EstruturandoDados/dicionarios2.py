dicionario =  {1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}}
dicionario.update({2:{'nome':'Simone', 'idade':25,'nacionalidade':'brasileira' }})
print(dicionario)
dicionario.pop(2)
print(dicionario)
dicionario.popitem()
print(dicionario)
novoDicionario = ["Simone","Bernardo", "Catia", "Miriam"]
new_dict = dict.fromkeys(novoDicionario)
print(new_dict.items())
print(new_dict.keys())
print(new_dict.values())