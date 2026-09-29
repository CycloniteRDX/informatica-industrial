# ideales para eliminar duplicados de listas

fallos_1 = {"cavitacion","vibracion"}
fallos_2 = {"cavitacion","sobrecalentamiento"}

fallos_1.add("corrosion")
print(fallos_1)

fallos_total = fallos_1 | fallos_2 # unión
print(fallos_total)

fallos_interseccion =fallos_1 & fallos_2
print(fallos_interseccion)

diferencia = fallos_1 - fallos_2
print(diferencia)

L1 = [1, 2, 3]
L2 = [3, 2, 1]
# tienen los mismos valores?
print(L1 == L2)
print(set(L1) == set(L2))

L1 = [1, 2, 3, 1, 2, 3, 4, 5, 6, 7]
#filtrar duplicados
L1 = list(set(L1))
print(L1)
