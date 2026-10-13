# código de la clase de la interfaz exportado por QtDesigner

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfazixwAre.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1041, 600)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_maquina = QLabel(self.centralwidget)
        self.lbl_maquina.setObjectName(u"lbl_maquina")
        self.le_maquina = QLineEdit(self.centralwidget)
        self.le_maquina.setObjectName(u"le_maquina")
        self.le_maquina.setGeometry(QRect(120, 150, 211, 26))
        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setGeometry(QRect(350, 150, 81, 26))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.btn_add.setFont(font1)
        self.btn_marcha = QPushButton(self.centralwidget)
        self.btn_marcha.setObjectName(u"btn_marcha")
        self.btn_marcha.setGeometry(QRect(440, 150, 81, 26))
        self.btn_marcha.setFont(font1)
        self.btn_paro = QPushButton(self.centralwidget)
        self.btn_paro.setObjectName(u"btn_paro")
        self.btn_paro.setGeometry(QRect(530, 150, 81, 26))
        self.btn_paro.setFont(font1)
        self.lbl_resultado = QLabel(self.centralwidget)
        self.lbl_resultado.setObjectName(u"lbl_resultado")
        self.lbl_resultado.setGeometry(QRect(50, 200, 331, 16))
        palette = QPalette()
        brush = QBrush(QColor(170, 0, 3, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(0, 170, 0, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.lbl_resultado.setPalette(palette)
        self.lbl_resultado.setAutoFillBackground(True)
        self.lbl_resultado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.img_lampara = QLabel(self.centralwidget)
        self.img_lampara.setObjectName(u"img_lampara")
        self.img_lampara.setGeometry(QRect(450, 200, 131, 131))
        self.img_lampara.setPixmap(QPixmap(u"../../../../../Desktop/iconosHMI/lampara/LamparaGris.png"))
        self.img_lampara.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1041, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Interfaz 1", None))
        self.lbl_maquina.setText(QCoreApplication.translate("MainWindow", u"M\u00e1quina:", None))
        self.le_maquina.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Inserte c\u00f3digo m\u00e1quina", None))
#if QT_CONFIG(tooltip)
        self.btn_add.setToolTip(QCoreApplication.translate("MainWindow", u"A\u00f1adir m\u00e1quina al diccionario", None))
#endif // QT_CONFIG(tooltip)
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir", None))
        self.btn_marcha.setText(QCoreApplication.translate("MainWindow", u"Marcha", None))
        self.btn_paro.setText(QCoreApplication.translate("MainWindow", u"Paro", None))
        self.lbl_resultado.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.img_lampara.setText("")
    # retranslateUi

