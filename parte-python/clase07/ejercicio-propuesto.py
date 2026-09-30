"""
Crear una clase Motor.
-El constructor recibe identificador, velocidad y temperatura.
-Los tres datos deben almacenarse como atributos privados.
-"identificador" es un atributo de solo lectura (al ser privado, se tiene que habilitar un mecanismo para poder leerlo desde fuera de la clase ("getter")).
-velocidad será un atributo de lectura y escritura (es decir, tendrá un getter y un setter).
-El setter de velocidad debe impedir valores negativos.

Crear un programa con dos motores y modificar la velocidad de uno de ellos. Comprobar que son dos objetos totalmente independientes.
"""

class Motor:
    def __init__(self, identificador, velocidad, temperatura):
        self.__identificador = identificador
        self.__velocidad = velocidad
        self.__temperatura = temperatura
    #getter de identificador
    def get_identificador(self):
        return self.__identificador
    #getter de velocidad
    def get_velocidad(self):
        return self.__velocidad
    #setter de velocidad
    def set_velocidad(self, velocidad):
        if velocidad >= 0:
            self.__velocidad = velocidad
    #getter de temperatura
    def get_temperatura(self):
        return self.__temperatura

motor1 = Motor(1, 200, 90)
motor2 = Motor(2, 100, 80)
print(motor1.get_identificador(), motor1.get_velocidad(), motor1.get_temperatura())
print(motor2.get_identificador(), motor2.get_velocidad(), motor2.get_temperatura())
motor2.set_velocidad(50)
print(motor1.get_identificador(), motor1.get_velocidad(), motor1.get_temperatura())
print(motor2.get_identificador(), motor2.get_velocidad(), motor2.get_temperatura())
print(motor1 is motor2)

motor2.set_velocidad(-50)
print(motor2.get_velocidad())
