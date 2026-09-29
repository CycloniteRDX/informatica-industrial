def calc_resis(fuerza, seccion):
    if seccion <= 0:
        raise ValueError("La sección tiene que ser mayor que cero")
    return fuerza / seccion