import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView, QAbstractItemView

from ui_tabla import Ui_MainWindow as UI_InterfazTabla
from model_datos import Modelo

class VentanaPrincipal(QMainWindow, UI_InterfazTabla):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Modelo y datos iniciales
        self.modelo = Modelo()
        self.modelo.cargar_datos([1, 2, 3, 4])
        self.modelo.cargar_datos([55, 20.1234, 30, 40])
        self.modelo.cargar_datos([11, 22, 33, 44])
        self.modelo.cargar_datos([110, 220, 330, 440])

        # Configuración de la tabla
        self.tabla.setModel(self.modelo)
        cabeceraVertical = self.tabla.verticalHeader()
        cabeceraVertical.setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        cabeceraVertical.setDefaultSectionSize(30)
        self.tabla.horizontalHeader().setStretchLastSection(True)
        self.tabla.setColumnWidth(0, 80)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        for cabecera in self.modelo.get_cabeceras():    #inicilización de valores del combobox
            self.comboOrdenar.addItem(cabecera)

        ## conexión de eventos
        self.botonInserta.clicked.connect(self.insertar_filas)
        self.botonBorra.clicked.connect(self.borrar_filas)
        self.botonIncrementa.clicked.connect(self.incrementar_dato)
        self.botonNoSeleccionar.clicked.connect(self.vaciar_seleccion)
        self.botonOrdenar.clicked.connect(self.ordenar_datos)
    #métodos de la vista que llaman a los métodos del módelo. Estos últimos son los que modifican la vista.
    def insertar_filas(self):
        pass

    def borrar_filas(self):
        pass

    def incrementar_dato(self):
        filas = self.tabla.selectionModel().selectedRows()
        for fila in filas:
            n_fila = fila.row()
            self.modelo.incremento_dato_A(n_fila)

    def vaciar_seleccion(self):
        #self.tabla.selectionModel().selectedRows()
        self.tabla.clearSelection()

    def ordenar_datos(self):
        columna = self.comboOrdenar.currentText()
        inverso = self.checkInverso.isChecked()
        self.modelo.ordena(columna, inverso)

##programa principal
aplicacion = QApplication(sys.argv)
ventana = VentanaPrincipal()
ventana.show()
sys.exit(aplicacion.exec())
