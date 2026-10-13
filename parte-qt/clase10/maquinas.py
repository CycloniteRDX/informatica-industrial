class Maquina:

    __contador = 0

    def __init__(self, nombre):
        self.__id = nombre
        self.__num_trabajos = 0
        self.__trabajando = False
        Maquina.__contador += 1 # a los atributos estáticos se accede desde la clase, en este caso, Maquina

    def getNombre(self): #método de la clase recibe siempre parámetro self
        return self.__id

    def getNumTrabajos(self):
        return self.__num_trabajos

    def getEstaLibre(self):
        return not self.__trabajando

    @staticmethod
    def getNumMaquinas(): # sin self porque es método estático. Trabaja contra toda la clase, no solo con la propia intancia o objeto
        return Maquina.__contador

    def marcha(self):
        if self.__trabajando:
            raise Exception("La máquina {} ya está trabajando".format(self.__id))

        self.__trabajando = True

    def parada(self):
        if not self.__trabajando:
            raise Exception("La máquina {} NO está trabajando".format(self.__id))

        self.__trabajando = False
        self.__num_trabajos += 1