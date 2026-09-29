# qué valor final tiene lecturas_por_hora y lecturas_base?

lecturas_por_hora = []
lecturas_base = [25, 30, 28]

i=0
for i in range(3):
    lecturas_por_hora.append(lecturas_base)
    lecturas_base[0] += 1

print(lecturas_por_hora)
print(lecturas_base)