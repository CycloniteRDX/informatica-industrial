from copy import copy
from random import randint

from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtGui import QColor, QPixmap


class Modelo(QAbstractTableModel):
    ## defino atributos estáticos con colores para usar posteriormente
    __amarillo = QColor(255, 255, 0)
    __naranja = QColor(255, 200, 0)
    __rojo = QColor(200, 0, 0)
    __negro = QColor(0, 0, 0)

    def __init__(self):
        super().__init__()
        self.__datos = []
        self.__cabeceras = ["Dato A", "Dato B", "Dato C", "Dato D"] #poderían ser parámetros del constructor

    def cargar_datos(self, fila): #añadir un nuevo dato al modelo
        self.__datos.append(fila)

    def get_cabeceras(self):
        return copy(self.__cabeceras)

    def rowCount(self, posicion):
        return len(self.__datos)

    def columnCount(self, posicion):
        return len(self.__cabeceras)

    def headerData(self, n_columna, orientacion, peticion):
        if peticion == Qt.ItemDataRole.DisplayRole:
            if orientacion == Qt.Orientation.Horizontal:
                return self.__cabeceras[n_columna]
        return None

    def data(self, posicion, peticion):
        n_fila = posicion.row()
        n_columna = posicion.column()

        # DisplayRole/EditRole: mostrar o editar números y cadenas
        if peticion == Qt.ItemDataRole.DisplayRole or peticion == Qt.ItemDataRole.EditRole:
            dato = self.__datos[n_fila][n_columna]
            if isinstance(dato, float):
                return "{:.2f}".format(dato)
            else:
                return str(dato)

        # BackgroundRole: color de fondo
        elif peticion == Qt.ItemDataRole.BackgroundRole:
            if self.__datos[n_fila][0] <= 40:
                return Modelo.__amarillo #no self porque es atributo estático. Accedemos a través de la clase, no del objeto
            else:
                return Modelo.__naranja

        # TextAlignmentRole: alineación
        elif peticion == Qt.ItemDataRole.TextAlignmentRole:
            if (n_columna == 0):
                return Qt.AlignmentFlag.AlignLeft
            else:
                return Qt.AlignmentFlag.AlignHCenter

        # ForegroundRole: color del texto
        elif peticion == Qt.ItemDataRole.ForegroundRole:
            if n_fila == 1:
                return Modelo.__rojo
            else:
                return Modelo.__negro

        # DecorationRole: iconos
        elif peticion == Qt.ItemDataRole.DecorationRole:
            pass

        return None

    def flags(self, posicion):
        if posicion.column() == 0:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
            # Las celdas de la primera columna se pueden seleccionar, están habilitadas y son editables
        else:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled
            # Las celdas de las demás columnas son seleccionables, habilitadas pero no editables

    def setData(self, posicion, valor, role):
        n_fila = posicion.row()
        n_columna = posicion.column()

        if n_columna != 0:
            return False

        if role == Qt.EditRole:  # Si la operación consiste en una modificación ...
            try:
                dato = int(valor)
            except ValueError:
                return False
            self.__datos[n_fila][n_columna] = dato
            self.layoutChanged.emit() # para que se refresque la vista con el nuevo dato. ¡OBLIGATORIO!
            return True
        else:
            return False  # Devuelve False si la operación no es una modificació

    def incremento_dato_A(self, fila):
        self.__datos[fila][0] += 1
        self.layoutChanged.emit()

    def insertar_filas(self, fila, cuantas):
        for i in range(cuantas):
            lista = []
            for j in range(4):
                lista.append(randint(0, 100))
            self.__datos.insert(fila, lista)
        self.layoutChanged.emit()

    def eliminar_filas(self, fila, cuantas):
        for i in range(cuantas):
            self.__datos.pop(fila)
        self.layoutChanged.emit()

    def ordena(self, columna, inverso):
        n_columna = self.__cabeceras.index(columna)

        def criterio(fila):
            return fila[n_columna]

        self.__datos = sorted(self.__datos, reverse=inverso, key=criterio)
        self.layoutChanged.emit()
