import sys

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton
from Informaticaindustrial.Qt import leeInterfaz

aplicacion = QApplication(sys.argv) # estas 6 lineas hay que ponerlas siempre
#archivoUI = QFile("interfaz.ui")
#archivoUI.open(QFile.ReadOnly)
#cargador = QUiLoader()
#ventana = cargador.load(archivoUI)
#archivoUI.close()
ventana = leeInterfaz("interfaz.ui")

def boton_pulsado():
    numero = float(leDato.text())
    resultado = numero * 2
    lblResultado.setText(str(resultado))

# aquí ponemos los elementos de la interfaz
leDato = ventana.findChild(QLineEdit,"editorDato")
btnCalcular = ventana.findChild(QPushButton,"botonDuplica")
lblResultado = ventana.findChild(QLabel,"etiquetaResultado")

# conexión de elementos
btnCalcular.clicked.connect(boton_pulsado)

ventana.show() # estas 2 lineas también hay que ponerlas siempre
sys.exit(aplicacion.exec())