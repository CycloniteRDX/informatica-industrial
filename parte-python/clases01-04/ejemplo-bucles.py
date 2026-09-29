# buscar el resultado  que supere el límite. Cuando encontremos el primero podemos parar.

resis = [250, -20, 200, 444, 330]
limite = 400

"""
## while
i = 0
encontrado = False
while i < len(resis):
    if resis[i] < 0:
        print("bloqueado") # ojo, temos que sumar a i
        i = i + 1
        continue 
    if resis[i] >= limite:
        encontrado = True
        break # en esta asignatura si seguimos buscando tendríamos un cero
    i = i + 1
        
if encontrado:
    print("encontrado")
else:
    print("nao encontrado")
"""

## while
i = 0
while i < len(resis):
    if resis[i] < 0:
        i = i + 1
        continue
    if resis[i] >= limite:
        print("encontrado")
        break  # en esta asignatura si seguimos buscando tendríamos un cero
    i = i + 1
else:
    print("no encontrado")

## for

for dato in resis:
    if dato < 0:
        continue
    if dato >= limite:
        print("encontrado")
        break
else:
    print("no encontrado")

## for con variable i
for i in range (0,len(resis),1): # range(len(resis)) equivalente
    dato = resis[i]
    if dato < 0:
        continue
    if dato >= limite:
        print("encontrado")
        break
else:
    print("no encontrado")
