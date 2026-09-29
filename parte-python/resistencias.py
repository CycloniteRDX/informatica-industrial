limite = 400
medidas = [250, 280, 330]
print("Cargando módulo resistencias")
print("__name__ =", __name__)

def calc_resis(fuerza, seccion):
    if seccion <= 0:
        raise ValueError("La sección tiene que ser mayor que cero")
    return fuerza / seccion

def supera_limite(resistencia, limite=400):
    return resistencia >= limite

if __name__ == "__main__":
    print("Prueba del módulo resistencias")
    resultado = calc_resis(100, 2)
    print("Resistencia: {} MPa".format(resultado))
    print("¿Supera el límite?", supera_limite(450))
