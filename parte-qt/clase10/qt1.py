# ejemplo basado en el ejercicio 1 del boletín de Qt

import sys
from PySide6.QtWidgets import (QMainWindow, QApplication)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QTimer
from maquinas import Maquina
from ui_interfaz import Ui_MainWindow as interfaz1

class VentanaPrincipal(QMainWindow, interfaz1):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        ## inicialización de variables
        self.__d_maquina = {}
        #self.lbl_resultado.setText("") #lo hacemos más abajo con el temporizador

        self.pixmapVerde = QPixmap("../../iconosHMI/lampara/LamparaVerde")
        self.pixmapGris = QPixmap("../../iconosHMI/lampara/LamparaGris.png")

        self.temporizador = QTimer()


        ## conexión de elementos y funciones
        self.btn_add.clicked.connect(self.add_maquina) # solo el nombre de la función. Nunca le vamos a pasar parámetros en esta asignatura
        self.btn_marcha.clicked.connect(self.marcha)

        self.temporizador.timeout.connect(self.limpia)

    def limpia(self):
        self.temporizador.stop()
        self.lbl_resultado.setText("")

    def marcha(self):
        # habría que validar que el texto no esté vacío y sea de una máquina que está registrada en el diccionario
        codigo = self.le_maquina.text().strip()
        try:
            self.__d_maquina[codigo].marcha()
            self.lbl_resultado.setText("Máquina en marcha")
            self.img_lampara.setPixmap(self.pixmapVerde)
        except Exception as e:
            self.lbl_resultado.setText(str(e))

    def add_maquina(self):
        self.temporizador.start(3000) # en milisegundos

        codigo = self.le_maquina.text().strip()
        if codigo in self.__d_maquina:
            self.lbl_resultado.setText("El código ya existe")
            return

        nueva_maquina = Maquina(codigo)
        self.__d_maquina[codigo] = nueva_maquina
        self.lbl_resultado.setText("Máquina registrada") # también deberíamos añadir el código de la máquina en el mensaje



aplicacion = QApplication(sys.argv)
ventana = VentanaPrincipal()

ventana.show()
sys.exit(aplicacion.exec())