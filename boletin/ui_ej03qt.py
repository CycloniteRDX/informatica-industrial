# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ej03qtZoKtQw.ui'
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
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.img_termo = QLabel(self.centralwidget)
        self.img_termo.setObjectName(u"img_termo")
        self.img_termo.setGeometry(QRect(330, 60, 81, 271))
        self.img_termo.setPixmap(QPixmap(u"../iconosHMI/termometro/termometro.png"))
        self.img_termo.setScaledContents(True)
        self.wdg_barra = QWidget(self.centralwidget)
        self.wdg_barra.setObjectName(u"wdg_barra")
        self.wdg_barra.setGeometry(QRect(360, 70, 21, 191))
        self.wdg_barra.setAutoFillBackground(True)
        self.le_temp = QLineEdit(self.centralwidget)
        self.le_temp.setObjectName(u"le_temp")
        self.le_temp.setGeometry(QRect(470, 130, 113, 26))
        self.btn_calcular = QPushButton(self.centralwidget)
        self.btn_calcular.setObjectName(u"btn_calcular")
        self.btn_calcular.setGeometry(QRect(490, 170, 81, 26))
        self.lbl_temp = QLabel(self.centralwidget)
        self.lbl_temp.setObjectName(u"lbl_temp")
        self.lbl_temp.setGeometry(QRect(350, 340, 49, 16))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(400, 250, 49, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(400, 60, 49, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.img_termo.setText("")
        self.btn_calcular.setText(QCoreApplication.translate("MainWindow", u"Introduce", None))
        self.lbl_temp.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"0\u00baC", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"1000\u00baC", None))
    # retranslateUi

