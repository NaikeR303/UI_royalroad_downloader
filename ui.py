# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_design3QypFXE.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QProgressBar, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet(u"QDialog{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: rgba(40, 40, 40, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"	 padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    border-radius: 12px;\n"
"}\n"
"QPushButton[selected=\"true\"] {\n"
"    border: solid;\n"
"    border-width: 2px;\n"
"    border-color: #f25f2c;\n"
"}\n"
"QPushButton[selected=\"\"] {\n"
"    border:  none;\n"
"}")
        self.background = QLabel(Dialog)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(8, 8, 484, 284))
        self.background.setStyleSheet(u"background-color: rgb(23, 23, 23);\n"
"border-radius: 12px;")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(92, 15, 335, 25))
        font = QFont()
        font.setFamilies([u"Ubuntu Sans"])
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(194, 194, 194);\n"
"background-color: rgb(23, 23, 23);")
        self.urlLine = QLineEdit(Dialog)
        self.urlLine.setObjectName(u"urlLine")
        self.urlLine.setGeometry(QRect(20, 45, 460, 25))
        self.urlLine.setStyleSheet(u"background-color: rgb(94, 92, 92);")
        self.background_2 = QLabel(Dialog)
        self.background_2.setObjectName(u"background_2")
        self.background_2.setGeometry(QRect(16, 80, 230, 204))
        self.background_2.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"border-radius: 12px;")
        self.background_3 = QLabel(Dialog)
        self.background_3.setObjectName(u"background_3")
        self.background_3.setGeometry(QRect(254, 80, 230, 204))
        self.background_3.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"border-radius: 12px;")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 84, 171, 31))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(194, 194, 194);\n"
"background-color: rgb(40, 40, 40);")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(316, 84, 131, 31))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(194, 194, 194);\n"
"background-color: rgb(40, 40, 40);")
        self.verticalFrame = QFrame(Dialog)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setGeometry(QRect(16, 113, 230, 171))
        self.verticalFrame.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, -1)
        self.rr_light_button = QPushButton(self.verticalFrame)
        self.rr_light_button.setObjectName(u"rr_light_button")
        self.rr_light_button.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: black;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #CACACA;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #3D3730;\n"
"}")
        self.rr_light_button.setAutoDefault(True)
        self.rr_light_button.setFlat(False)

        self.verticalLayout_2.addWidget(self.rr_light_button)

        self.rr_dark_button = QPushButton(self.verticalFrame)
        self.rr_dark_button.setObjectName(u"rr_dark_button")
        self.rr_dark_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #131313;\n"
"    color: #CFCFCF;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2D2D2D;\n"
"}\n"
"QPushButton:disable {\n"
"    background-color: #3D3730;\n"
"}")
        self.rr_dark_button.setFlat(False)

        self.verticalLayout_2.addWidget(self.rr_dark_button)

        self.midnight_button = QPushButton(self.verticalFrame)
        self.midnight_button.setObjectName(u"midnight_button")
        self.midnight_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #1A1A1A;\n"
"    color: #808080;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #3D3730;\n"
"}")
        self.midnight_button.setFlat(False)

        self.verticalLayout_2.addWidget(self.midnight_button)

        self.antique_button = QPushButton(self.verticalFrame)
        self.antique_button.setObjectName(u"antique_button")
        self.antique_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #af926d;\n"
"    color: #52331e;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #8E7657;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #3D3730;\n"
"}")
        self.antique_button.setFlat(False)

        self.verticalLayout_2.addWidget(self.antique_button)

        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(264, 255, 210, 20))
        self.progressBar.setValue(24)
        self.verticalFrame1 = QFrame(Dialog)
        self.verticalFrame1.setObjectName(u"verticalFrame1")
        self.verticalFrame1.setGeometry(QRect(254, 110, 230, 141))
        self.verticalFrame1.setStyleSheet(u"QPushButton {\n"
"    background-color: #8D8D8D;\n"
"    color: black;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #6C6C6C;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #3D3730;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.verticalFrame1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, 10, -1)
        self.txt_button = QPushButton(self.verticalFrame1)
        self.txt_button.setObjectName(u"txt_button")
        self.txt_button.setStyleSheet(u"")
        self.txt_button.setAutoDefault(True)
        self.txt_button.setFlat(False)

        self.verticalLayout.addWidget(self.txt_button)

        self.html_button = QPushButton(self.verticalFrame1)
        self.html_button.setObjectName(u"html_button")
        self.html_button.setStyleSheet(u"")
        self.html_button.setAutoDefault(True)
        self.html_button.setFlat(False)

        self.verticalLayout.addWidget(self.html_button)

        self.pdf_button = QPushButton(self.verticalFrame1)
        self.pdf_button.setObjectName(u"pdf_button")
        self.pdf_button.setStyleSheet(u"")
        self.pdf_button.setAutoDefault(True)
        self.pdf_button.setFlat(False)

        self.verticalLayout.addWidget(self.pdf_button)


        self.retranslateUi(Dialog)

        self.rr_light_button.setDefault(False)
        self.txt_button.setDefault(False)
        self.html_button.setDefault(False)
        self.pdf_button.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"RoyalRoad downloader", None))
        self.background.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Put RoyalRoad fiction link here", None))
        self.urlLine.setText(QCoreApplication.translate("Dialog", u"https://www.royalroad.com/fiction/51893/the-heart-grows", None))
        self.background_2.setText("")
        self.background_3.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Choose a style", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Download!", None))
        self.rr_light_button.setText(QCoreApplication.translate("Dialog", u"RR Light", None))
        self.rr_dark_button.setText(QCoreApplication.translate("Dialog", u"RR Dark", None))
        self.midnight_button.setText(QCoreApplication.translate("Dialog", u"Midnight", None))
        self.antique_button.setText(QCoreApplication.translate("Dialog", u"Antique", None))
        self.txt_button.setText(QCoreApplication.translate("Dialog", u"TXT File", None))
        self.html_button.setText(QCoreApplication.translate("Dialog", u"HTML File - BEST!", None))
        self.pdf_button.setText(QCoreApplication.translate("Dialog", u"PDF File", None))
    # retranslateUi

