def calc_potencia(intensidad,voltaje=220): # los valores por defecto siempre deben estar al final, si no da error
    potencia = voltaje * intensidad
    return (potencia, "W") #devuelve una tupla

#potencia = calc_potencia(220, 5)
potencia, unidad = calc_potencia(intensidad=5, voltaje=220)
print("La potencia ha sido {}{}".format(potencia, unidad))

### objetos inmutables
def incrementar(numero):
    numero = numero + 1
    return numero

n1 = 5
incrementar(n1)
print("original:",n1) # n1 sigue apuntando a 5, con numero se crea una referencia en 6 y se elimina de 5

### objetos mutables
def add_lista(lista, elemento):
    lista.append(elemento)
    return lista

l1 = []
#l1 = list() #equivalente
l1 = add_lista(l1,200)
print(l1)
# eliminando el return de la función devolvería [200] igualmente. También funcionaría usando solo add_lista(l1,200), sin l1 =

### variables globales
def incrementar2():
    global n2
    n2 = n2 + 1

n2 = 4
incrementar2()
print(n2)

