fila = [3,4,5,6]
parte = fila[1:]
parte[0]=115
print(fila,parte)

temperatura = [10, 20, 30, 50, 80]
temperatura.append([100])
temperatura.append(100)
print(temperatura)

temperatura.extend([100])
print(temperatura)

print(50 in temperatura)
print(temperatura.index(50)) # si no lo encuentra no devuelve -1, rompe el programa

for dato in temperatura:
    print(dato)

for elemento in range(len(temperatura)):
    print(temperatura[elemento],elemento)