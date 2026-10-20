import sys

from PySide6.QtWidgets import (QMainWindow, QApplication)
from ui_ej03qt import Ui_MainWindow as interfaz


class VentanaPrincipal(QMainWindow, interfaz):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.temperatura = 25

        self.y1 = self.wdg_barra.y()
        self.y0 = self.wdg_barra.y() + self.wdg_barra.height()

        #conexión
        self.btn_calcular.clicked.connect(self.actualizar)

    def actualizar(self):
        try:
            self.temperatura = float(self.le_temp.text().strip())
            self.lbl_temp.setText(str(self.temperatura))
            if self.temperatura < 0:
                self.temperatura = 0
            elif self.temperatura > 1000:
                self.temperatura = 1000

            posicion = self.y0 + (self.temperatura - 0) * (self.y1 - self.y0) / (1000 - 0)

            self.wdg_barra.setGeometry(
                self.wdg_barra.x(),self.wdg_barra.y(),
                self.wdg_barra.width(),int(posicion - self.y1)
            )

        except:
            pass





aplicacion = QApplication(sys.argv)
ventana = VentanaPrincipal()

ventana.show()
sys.exit(aplicacion.exec())
