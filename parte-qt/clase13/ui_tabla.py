# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tablanJvEFI.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(712, 425)
        MainWindow.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionCerrar = QAction(MainWindow)
        self.actionCerrar.setObjectName(u"actionCerrar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabla = QTableView(self.centralwidget)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setGeometry(QRect(10, 10, 691, 291))
        self.botonInserta = QPushButton(self.centralwidget)
        self.botonInserta.setObjectName(u"botonInserta")
        self.botonInserta.setGeometry(QRect(50, 310, 121, 24))
        self.botonBorra = QPushButton(self.centralwidget)
        self.botonBorra.setObjectName(u"botonBorra")
        self.botonBorra.setGeometry(QRect(180, 310, 121, 24))
        self.botonIncrementa = QPushButton(self.centralwidget)
        self.botonIncrementa.setObjectName(u"botonIncrementa")
        self.botonIncrementa.setGeometry(QRect(310, 310, 151, 24))
        self.botonNoSeleccionar = QPushButton(self.centralwidget)
        self.botonNoSeleccionar.setObjectName(u"botonNoSeleccionar")
        self.botonNoSeleccionar.setGeometry(QRect(490, 310, 181, 24))
        self.lblOrdenar = QLabel(self.centralwidget)
        self.lblOrdenar.setObjectName(u"lblOrdenar")
        self.lblOrdenar.setGeometry(QRect(50, 350, 91, 41))
        self.comboOrdenar = QComboBox(self.centralwidget)
        self.comboOrdenar.setObjectName(u"comboOrdenar")
        self.comboOrdenar.setGeometry(QRect(150, 360, 151, 22))
        self.checkInverso = QCheckBox(self.centralwidget)
        self.checkInverso.setObjectName(u"checkInverso")
        self.checkInverso.setGeometry(QRect(330, 360, 141, 20))
        self.botonOrdenar = QPushButton(self.centralwidget)
        self.botonOrdenar.setObjectName(u"botonOrdenar")
        self.botonOrdenar.setGeometry(QRect(500, 360, 171, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.actionCerrar.setText(QCoreApplication.translate("MainWindow", u"Cerrar", None))
        self.botonInserta.setText(QCoreApplication.translate("MainWindow", u"Insertar 2 filas", None))
        self.botonBorra.setText(QCoreApplication.translate("MainWindow", u"Borra filas", None))
        self.botonIncrementa.setText(QCoreApplication.translate("MainWindow", u"Incrementa dato A", None))
        self.botonNoSeleccionar.setText(QCoreApplication.translate("MainWindow", u"No seleccionar", None))
        self.lblOrdenar.setText(QCoreApplication.translate("MainWindow", u"Ordenar por", None))
        self.checkInverso.setText(QCoreApplication.translate("MainWindow", u"Orden Inverso", None))
        self.botonOrdenar.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None))
    # retranslateUi

