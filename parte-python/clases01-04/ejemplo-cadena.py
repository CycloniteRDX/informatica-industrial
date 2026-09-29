cadena = "Robótica"

print(cadena[7],cadena[-1])
print(cadena)

cadena2 = cadena[0:3]
print(cadena2)

#cadena2[0] = "r" # no se puede, las cadena son inmutables
cadena2 = "r" + cadena[1:3] # o cadena[1:]
print(cadena2)

cadena = cadena.replace("R", "r")
print(cadena)



piezas_OK = 5
defectuosas = 10

print("Hubo {} piezas OK y hubo {} defectuosas".format(piezas_OK,defectuosas))
print("Hubo {1} piezas OK y hubo {0} defectuosas".format(piezas_OK,defectuosas)) # para alterar el orden
print("Hubo {OK} piezas OK y hubo {NOK} defectuosas".format(OK=piezas_OK,NOK=defectuosas))

n1 = 34.1235345
#n1 = round(n1) # altera el número original
print("{:.3f}".format(n1)) #no altera el número original y muestra solo 3 decimales
print(n1)