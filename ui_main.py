
import sys

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
                               QWidget)
from PySide6 import QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(388, 385)
        Form.setStyleSheet(u"background-color: #2BA245;color:white;\n"
                           "font: 700 9pt \"Microsoft YaHei UI\";")
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(110, 90, 81, 41))
        self.pushButton_3.setStyleSheet(u"background-color:#AAAAAA")
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 90, 81, 41))
        self.pushButton_4.setStyleSheet(u"background-color:#AAAAAA")
        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(290, 90, 81, 41))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet(u"background-color: #FFBE00;color:#444")
        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(200, 90, 81, 41))
        self.pushButton_6.setStyleSheet(u"background-color:#AAAAAA")
        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(200, 190, 81, 41))
        self.pushButton_7.setStyleSheet(u"background-color:white;color:#333")
        self.pushButton_8 = QPushButton(Form)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(200, 140, 81, 41))
        self.pushButton_8.setStyleSheet(u"background-color:white;color:#333")
        self.pushButton_9 = QPushButton(Form)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(110, 240, 81, 41))
        self.pushButton_9.setStyleSheet(u"background-color:white;color:#333")
        self.pushButton_10 = QPushButton(Form)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(110, 190, 81, 41))
        self.pushButton_10.setStyleSheet(u"background-color:white;color:#333")
        self.pushButton_11 = QPushButton(Form)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(110, 140, 81, 41))
        self.pushButton_11.setStyleSheet(u"background-color:white;color:#333")
        self.pushButton_12 = QPushButton(Form)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(20, 240, 81, 41))
        self.pushButton_12.setStyleSheet(u"background-color:white;color:#333")
        self.pushButton_13 = QPushButton(Form)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(20, 190, 81, 41))
        self.pushButton_13.setStyleSheet(u"background-color:white;color:#333")
        self.pushButton_14 = QPushButton(Form)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(20, 140, 81, 41))
        self.pushButton_14.setStyleSheet(u"background-color:white;color:#333")
        self.pushButton_15 = QPushButton(Form)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(200, 240, 81, 41))
        self.pushButton_15.setStyleSheet(u"background-color:white;color:#333")
        self.pushButton_16 = QPushButton(Form)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(290, 240, 81, 41))
        self.pushButton_16.setStyleSheet(u"background-color: #FFBE00;color:#444")
        self.pushButton_17 = QPushButton(Form)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(290, 190, 81, 41))
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet(u"background-color: #FFBE00;color:#444")
        self.pushButton_18 = QPushButton(Form)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(290, 140, 81, 41))
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet(u"background-color: #FFBE00;color:#444")
        self.pushButton_19 = QPushButton(Form)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(200, 290, 171, 41))
        self.pushButton_19.setAutoFillBackground(False)
        self.pushButton_19.setStyleSheet(u"background-color: #FFBE00;color:#444")
        self.pushButton_20 = QPushButton(Form)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(110, 290, 81, 41))
        self.pushButton_20.setStyleSheet(u"background-color:white;color:#333")
        self.pushButton_21 = QPushButton(Form)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(20, 290, 81, 41))
        self.pushButton_21.setStyleSheet(u"background-color:white;color:#333")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 30, 351, 41))
        self.lineEdit.setStyleSheet(u"background-color:white;color:#333")
        self.lineEdit.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"+/-", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"AC", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u00f7", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"%", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_13.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_14.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_15.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_16.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_17.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_18.setText(QCoreApplication.translate("Form", u"x", None))
        self.pushButton_19.setText(QCoreApplication.translate("Form", u"=", None))
        self.pushButton_20.setText(QCoreApplication.translate("Form", u".", None))
        self.pushButton_21.setText(QCoreApplication.translate("Form", u"0", None))
        self.lineEdit.setText("0")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
    # retranslateUi
