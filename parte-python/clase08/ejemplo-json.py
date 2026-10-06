import json

from boletin import maquinas

contenido = json.load(open("maquinas.json",encoding="utf-8")) # si lo abrimos dentro del load, luego ya se cierra solo
print(contenido)
print(type(contenido))

diccionario = { 'M1':True , 'M2':None }

fichero = open("log.json","w",encoding="utf-8")
json.dump(diccionario,fichero,ensure_ascii=False,indent=4) # mínimo 2 parámetros, el diccionario y donde lo guardamos.
# ensure es para que guarde tildes y no el caracter unicode de la tilde. indent para mejorar la readability
