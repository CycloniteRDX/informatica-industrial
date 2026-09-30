import robot_mod as Robot1
import robot_mod as Robot2

Robot1.nombre = "Robotito"
Robot2.nombre = "Rb"

Robot1.mostrar()
Robot2.mostrar()

print(Robot1 is Robot2)
# no podemos crear robots como varibales importándolos

class Robot:
    __contador = 0 # atributo privado estático. Pueden usarlo todas las instancias de la clase, es decir, todos los objetos de esa clase.

    def __init__(self,nombre,x,y,bateria=100):
        self.nombre = nombre # sin __ sería un atributo público
        self.__x = x
        self.__y = y
        self.__bateria = bateria
        Robot.__contador += 1
    #metodos
    def mover(self,dx,dy):
        self.__x = self.__x + dx
        self.__y = self.__y + dy

    def get_x(self): # getter
        return self.__x

    def set_x(self,nueva_x):
        if nueva_x < 1000 and nueva_x > -1000:
            self.__x = nueva_x
    #clase 07
    # diff entre property e getter?
    @property # equivalente getter?
    def nivel_bateria(self):
        return self.__bateria

    @nivel_bateria.setter # equivalente setter?
    def nivel_bateria(self,nuevo_valor):
        if nuevo_valor > 100:
            self.__bateria = 100
        else:
            self.__bateria = nuevo_valor

    @staticmethod # no tienen porque trabajar solo con atributos estáticos
    def cuantos():
        return Robot.__contador

    def __eq__(self,other): #sobrecarga de operadores
        return self.nombre == other.nombre

    def trabajar(self):
        pass


rb1 = Robot("Rb1",5,5)
rb2 = Robot("Rb2",0,0)

rb2.mover(10,-10)
Robot.mover(rb2,1,1)

#print(rb1.x,rb2.x)
print(rb1 is rb2)
#print(rb2.x)

rb2.x = -12341 # el atributo no debe ser público, debemos poner __ en los atributos de la clase
print(rb2.x)

print(rb2.get_x())

rb2._Robot__x=666
print(rb2.get_x())

#clase 07
rb2.nivel_bateria=1234 ### rb2.set_bateria(1324) # usando propiedad | usando setter
print(rb2.nivel_bateria)

print("Tengo {tantos} robots".format(tantos=Robot.cuantos()))

rb3=Robot("Rb3",5,5)
rb4=Robot("Rb3",5,5)
print(rb3 == rb4) # en este caso python no sabe que comparar. Sería el equivalente a hacer rb3 is rb4

class RobotPintura(Robot):
    def __init__(self,nombre,x,y,color,bateria=100): # batería de última porque tiene un valor por defecto
        # más utilizada/recomendada
        super().__init__(nombre,x,y,bateria)
        #otra forma
        #Robot.__init__() # menos recomendada por si en un futuro cambiamos el nombre de la clase de la que hereda
        self.color = color # sin __ sería un atributo público

    def trabajar(self): # sobrecargamos el método trabajar
        print("Estoy pintando con el color: ",self.color)


class RobotSoldador(Robot):
    def __init__(self, nombre, x, y, potencia, bateria=100):
        super().__init__(nombre, x, y, bateria)
        self.potencia = potencia

    def trabajar(self):  # sobrecargamos el método trabajar
        print("Estoy soldando a {} potencia: ".format(self.potencia))

rb5 = RobotPintura("Rb5",5,5,"red")
rb6 = RobotSoldador("Rb6",5,5,1000)

#print(rb6.color) # rompe
print(rb6.potencia)

print(rb6.mover(100,100)) # devuelve none
