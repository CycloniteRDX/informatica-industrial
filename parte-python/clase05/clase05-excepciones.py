"""
try:
    fuerza = input("Dame la fuerza: ")
    fuerza = float(fuerza)
    seccion = float(input("Dame la seccion: "))

    resistencia = fuerza / seccion
except ZeroDivisionError as ze:
    print("La sección no puede ser 0: ",str(ze))
except ValueError as ve:
    rint("Debe ser un número",str(ve))
except Exception as e: # excepción general
    print("El error es: ",str(e))

print("Continuo")
"""

def calc_resis(fuerza,seccion):
    if seccion <= 0:
        #print("No puedo calcular seccion menor que cero") # mal, no es nuestra responsabilidad. Será de quién use esta función en el programa principal
        #return 0
        raise ValueError("Sección no puede ser menor que 0")
    return fuerza / seccion

print(calc_resis(100,-2))