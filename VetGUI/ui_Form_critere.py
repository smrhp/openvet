# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Form_critere.ui'
#
# Created: Sun Mar  9 10:06:10 2014
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DialogCritere(object):
    def setupUi(self, DialogCritere):
        DialogCritere.setObjectName("DialogCritere")
        DialogCritere.resize(675, 392)
        self.layoutWidget = QtGui.QWidget(DialogCritere)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 250, 311, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.comboBox_Grade = QtGui.QComboBox(self.layoutWidget)
        self.comboBox_Grade.setMinimumSize(QtCore.QSize(71, 27))
        self.comboBox_Grade.setMaximumSize(QtCore.QSize(71, 27))
        self.comboBox_Grade.setObjectName("comboBox_Grade")
        self.horizontalLayout_3.addWidget(self.comboBox_Grade)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tableWidget_Seuil = MyTableWidget(self.layoutWidget)
        self.tableWidget_Seuil.setMinimumSize(QtCore.QSize(302, 50))
        self.tableWidget_Seuil.setMaximumSize(QtCore.QSize(302, 50))
        self.tableWidget_Seuil.setRowCount(1)
        self.tableWidget_Seuil.setColumnCount(3)
        self.tableWidget_Seuil.setObjectName("tableWidget_Seuil")
        self.tableWidget_Seuil.setColumnCount(3)
        self.tableWidget_Seuil.setRowCount(1)
        self.tableWidget_Seuil.verticalHeader().setVisible(False)
        self.tableWidget_Seuil.verticalHeader().setHighlightSections(True)
        self.verticalLayout_2.addWidget(self.tableWidget_Seuil)
        self.layoutWidget1 = QtGui.QWidget(DialogCritere)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 10, 631, 231))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Pathologie = QtGui.QLabel(self.layoutWidget1)
        self.label_Pathologie.setMinimumSize(QtCore.QSize(0, 30))
        self.label_Pathologie.setMaximumSize(QtCore.QSize(16777215, 36))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_Pathologie.setFont(font)
        self.label_Pathologie.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_Pathologie.setObjectName("label_Pathologie")
        self.verticalLayout.addWidget(self.label_Pathologie)
        self.label_Examen = QtGui.QLabel(self.layoutWidget1)
        self.label_Examen.setMinimumSize(QtCore.QSize(0, 30))
        self.label_Examen.setMaximumSize(QtCore.QSize(16777215, 36))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_Examen.setFont(font)
        self.label_Examen.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_Examen.setObjectName("label_Examen")
        self.verticalLayout.addWidget(self.label_Examen)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox_Critere = MyComboBox(self.layoutWidget1)
        self.comboBox_Critere.setMinimumSize(QtCore.QSize(261, 27))
        self.comboBox_Critere.setMaximumSize(QtCore.QSize(280, 27))
        self.comboBox_Critere.setEditable(True)
        self.comboBox_Critere.setObjectName("comboBox_Critere")
        self.horizontalLayout.addWidget(self.comboBox_Critere)
        self.toolButton_NewCritere = QtGui.QToolButton(self.layoutWidget1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/images/add1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_NewCritere.setIcon(icon)
        self.toolButton_NewCritere.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_NewCritere.setObjectName("toolButton_NewCritere")
        self.horizontalLayout.addWidget(self.toolButton_NewCritere)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        self.label_3.setMinimumSize(QtCore.QSize(51, 0))
        self.label_3.setMaximumSize(QtCore.QSize(51, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox_Unite = MyComboBox(self.layoutWidget1)
        self.comboBox_Unite.setMinimumSize(QtCore.QSize(141, 27))
        self.comboBox_Unite.setMaximumSize(QtCore.QSize(141, 27))
        self.comboBox_Unite.setEditable(True)
        self.comboBox_Unite.setObjectName("comboBox_Unite")
        self.horizontalLayout_2.addWidget(self.comboBox_Unite)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_5 = QtGui.QLabel(self.layoutWidget1)
        self.label_5.setMinimumSize(QtCore.QSize(141, 0))
        self.label_5.setMaximumSize(QtCore.QSize(141, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.lineEdit_NbGrades = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit_NbGrades.setMinimumSize(QtCore.QSize(41, 27))
        self.lineEdit_NbGrades.setMaximumSize(QtCore.QSize(41, 27))
        self.lineEdit_NbGrades.setObjectName("lineEdit_NbGrades")
        self.horizontalLayout_2.addWidget(self.lineEdit_NbGrades)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_remarque = QtGui.QLabel(self.layoutWidget1)
        self.label_remarque.setObjectName("label_remarque")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_remarque)
        self.plainTextEdit_Remarque = QtGui.QPlainTextEdit(self.layoutWidget1)
        self.plainTextEdit_Remarque.setMinimumSize(QtCore.QSize(0, 67))
        self.plainTextEdit_Remarque.setMaximumSize(QtCore.QSize(16777215, 77))
        self.plainTextEdit_Remarque.setObjectName("plainTextEdit_Remarque")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.plainTextEdit_Remarque)
        self.verticalLayout.addLayout(self.formLayout)
        self.layoutWidget2 = QtGui.QWidget(DialogCritere)
        self.layoutWidget2.setGeometry(QtCore.QRect(450, 288, 184, 41))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_Cancel = QtGui.QPushButton(self.layoutWidget2)
        self.pushButton_Cancel.setMinimumSize(QtCore.QSize(85, 27))
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.horizontalLayout_4.addWidget(self.pushButton_Cancel)
        self.pushButton_Save = QtGui.QPushButton(self.layoutWidget2)
        self.pushButton_Save.setMinimumSize(QtCore.QSize(85, 27))
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.horizontalLayout_4.addWidget(self.pushButton_Save)
        self.label_6.setBuddy(self.comboBox_Grade)
        self.label_2.setBuddy(self.comboBox_Critere)
        self.label_3.setBuddy(self.comboBox_Unite)
        self.label_5.setBuddy(self.lineEdit_NbGrades)
        self.label_remarque.setBuddy(self.plainTextEdit_Remarque)

        self.retranslateUi(DialogCritere)
        QtCore.QMetaObject.connectSlotsByName(DialogCritere)

    def retranslateUi(self, DialogCritere):
        DialogCritere.setWindowTitle(QtGui.QApplication.translate("DialogCritere", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("DialogCritere", "Grade :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Pathologie.setText(QtGui.QApplication.translate("DialogCritere", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Examen.setText(QtGui.QApplication.translate("DialogCritere", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogCritere", "Critère :", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_NewCritere.setText(QtGui.QApplication.translate("DialogCritere", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DialogCritere", "Unité :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DialogCritere", "Nombre de grades :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_remarque.setText(QtGui.QApplication.translate("DialogCritere", "Remarque :", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Cancel.setText(QtGui.QApplication.translate("DialogCritere", "Annuler", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Save.setText(QtGui.QApplication.translate("DialogCritere", "Enregi&strer", None, QtGui.QApplication.UnicodeUTF8))

from Mywidgets import MyTableWidget, MyComboBox
import resources_rc