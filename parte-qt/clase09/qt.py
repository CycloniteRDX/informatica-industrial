from PySide6.QtUiTools import QUiLoader
from PySide6.Qtcore import QFile

def leeInterfaz(fichero):
    archivoUI = QFile(fichero)
    archivoUI.open(QFile.ReadOnly)
    cargador = QUiLoader()
    ventana = cargador.load(archivoUI)
    archivoUI.close()
    return ventana