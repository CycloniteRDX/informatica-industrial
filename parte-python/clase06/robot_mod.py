# robot_mod.py
# Módulo simple que mantiene el estado de un robot 2D

nombre = "R1"   # Identificador del robot
x = 0           # Posición en el eje X
y = 0           # Posición en el eje Y

def mover(desplazamiento_x, desplazamiento_y):
    """
    Desplaza el robot en el plano 2D.
    Se actualiza el estado global (x, y).
    """
    global x, y
    x += desplazamiento_x
    y += desplazamiento_y

def mostrar():
    """
    Imprime el estado actual del robot: nombre y posición.
    """
    print(nombre, "\t posición:", x, y)
