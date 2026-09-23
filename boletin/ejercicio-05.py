maquinas = [
{'id': 'A35', 'trabajos': 5, 'libre': True},
{'id': 'B71', 'trabajos': 3, 'libre': True},
{'id': 'A28', 'trabajos': 2, 'libre': False},
{'id': 'B43', 'trabajos': 6, 'libre': False},
{'id': 'A82', 'trabajos': 3, 'libre': False},
{'id': 'A14', 'trabajos': 4, 'libre': True},
{'id': 'B62', 'trabajos': 1, 'libre': False},
{'id': 'B36', 'trabajos': 6, 'libre': False},
{'id': 'B18', 'trabajos': 4, 'libre': True},
{'id': 'A73', 'trabajos': 8, 'libre': True}
]

diccionario_maquina = {} ## dict()
for maquina in maquinas:
    tipo = maquina['id'][0]
    diccionario_maquina[tipo] = diccionario_maquina.get(tipo, 0) + 1 # más rápido. más intuitivo?
    #if tipo in diccionario_maquina:
    #    diccionario_maquina[tipo] = diccionario_maquina[tipo] + 1
    #else:
    #    diccionario_maquina[tipo] = 1
print(diccionario_maquina)