import robot_mod as Robot1
import robot_mod as Robot2

Robot1.nombre = "Robotito"
Robot2.nombre = "Rb"

Robot1.mostrar()
Robot2.mostrar()

print(Robot1 is Robot2)
# no podemos crear robots como varibales importándolos

class Robot:
    def __init__(self,nombre,x,y,bateria=100):
        self.__nombre = nombre
        self.__x = x
        self.__y = y
        self.__bateria = bateria
    #metodos
    def mover(self,dx,dy):
        self.__x = self.__x + dx
        self.__y = self.__y + dy

    def get_x(self): # getter
        return self.__x

    def set_x(self,nueva_x):
        if nueva_x < 1000 and nueva_x > -1000:
            self.__x = nueva_x


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
