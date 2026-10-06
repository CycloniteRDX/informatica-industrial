import xml.etree.ElementTree as ET # del paquete xml, modulo etree, método ElementTree

arbol = ET.parse("maquina_clase.xml")
print(arbol)

raiz = arbol.getroot()
print(raiz.tag) # etiqueta

print(len(raiz))

for elemento in raiz:
    print(elemento.tag)
    print(elemento.attrib["a"])

    for dato in elemento:
        print(dato.tag,"=",dato.text)