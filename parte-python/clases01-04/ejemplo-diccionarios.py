mantenimiento = {"motor":100,"bomba":150}
print(mantenimiento)

numeros = { (1,2): "uno", 2:"dos", "asdad":[12123,21332]}
print(numeros)

#mantenimiento.append({"compresor":200}) # error, nunca append en diccionarios
#añadir
mantenimiento["compresor"] = 200
print(mantenimiento,mantenimiento["motor"])

mantenimiento["motor"] = 123123 # actualiza la clave, porque existe. Si no, la crea
print(mantenimiento)

print("Hay motor?","motor" in mantenimiento)
#print(mantenimiento["válvula"]) # da error, no exite la clave

for clave in mantenimiento:
    print(clave, mantenimiento[clave])

c = mantenimiento.get("amoladora", 0)
print(c)

mantenimiento["amoladora"] = mantenimiento.get("amoladora", 0)
print(mantenimiento)

d1 = {
    "id":1,
    "datos": {"rpm": 1500}
}
print(d1["datos"]["rpm"])
d1["código"] = {}
d1["código"]["hexadecimal"] = "0x07AC" # debemos haberlo inicializado antes
print(d1)