# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 530)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(900, 530))
        Form.setMaximumSize(QtCore.QSize(900, 530))
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Explorer1 = QtWidgets.QListWidget(Form)
        self.Explorer1.setGeometry(QtCore.QRect(100, 70, 256, 361))
        self.Explorer1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.Explorer1.setObjectName("Explorer1")
        self.Explorer2 = QtWidgets.QListWidget(Form)
        self.Explorer2.setGeometry(QtCore.QRect(550, 70, 260, 361))
        self.Explorer2.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.Explorer2.setObjectName("Explorer2")
        self.NDir1 = QtWidgets.QPushButton(Form)
        self.NDir1.setGeometry(QtCore.QRect(211, 440, 50, 50))
        self.NDir1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("newFolder.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NDir1.setIcon(icon)
        self.NDir1.setIconSize(QtCore.QSize(20, 20))
        self.NDir1.setObjectName("NDir1")
        self.NDir2 = QtWidgets.QPushButton(Form)
        self.NDir2.setGeometry(QtCore.QRect(651, 440, 50, 50))
        self.NDir2.setText("")
        self.NDir2.setIcon(icon)



        self.NDir2.setIconSize(QtCore.QSize(20, 20))
        self.NDir2.setObjectName("NDir2")
        self.NFile2 = QtWidgets.QPushButton(Form)
        self.NFile2.setGeometry(QtCore.QRect(570, 440, 50, 50))
        self.NFile2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("newFile.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NFile2.setIcon(icon1)
        self.NFile2.setIconSize(QtCore.QSize(20, 20))
        self.NFile2.setObjectName("NFile2")
        self.Delete2 = QtWidgets.QPushButton(Form)
        self.Delete2.setGeometry(QtCore.QRect(740, 440, 50, 50))
        self.Delete2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("trash.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Delete2.setIcon(icon2)
        self.Delete2.setIconSize(QtCore.QSize(20, 20))
        self.Delete2.setObjectName("Delete2")
        self.LeftToRigth = QtWidgets.QPushButton(Form)
        self.LeftToRigth.setGeometry(QtCore.QRect(400, 160, 91, 31))
        self.LeftToRigth.setObjectName("LeftToRigth")
        self.RigthToLeft = QtWidgets.QPushButton(Form)
        self.RigthToLeft.setGeometry(QtCore.QRect(400, 220, 91, 31))
        self.RigthToLeft.setObjectName("RigthToLeft")
        self.NFile1 = QtWidgets.QPushButton(Form)
        self.NFile1.setGeometry(QtCore.QRect(130, 440, 50, 50))
        self.NFile1.setText("")
        self.NFile1.setIcon(icon1)
        self.NFile1.setIconSize(QtCore.QSize(20, 20))
        self.NFile1.setObjectName("NFile1")
        self.Delete1 = QtWidgets.QPushButton(Form)
        self.Delete1.setGeometry(QtCore.QRect(300, 440, 50, 50))
        self.Delete1.setText("")
        self.Delete1.setIcon(icon2)
        self.Delete1.setIconSize(QtCore.QSize(20, 20))
        self.Delete1.setObjectName("Delete1")
        self.label1 = QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(180, 40, 81, 17))
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(Form)
        self.label2.setGeometry(QtCore.QRect(640, 40, 81, 17))
        self.label2.setObjectName("label2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Directorios"))
        self.NDir1.setToolTip(_translate("Form", "Nueva Carpeta"))
        self.NDir2.setToolTip(_translate("Form", "Nueva Carpeta"))
        self.NFile2.setToolTip(_translate("Form", "Nuevo Archivo"))
        self.Delete2.setToolTip(_translate("Form", "Eliminar"))
        self.LeftToRigth.setText(_translate("Form", "----->"))
        self.RigthToLeft.setText(_translate("Form", "<-----"))
        self.NFile1.setToolTip(_translate("Form", "Nuevo Archivo"))
        self.Delete1.setToolTip(_translate("Form", "Eliminar"))
        self.label1.setText(_translate("Form", "Directorio 1"))
        self.label2.setText(_translate("Form", "Directorio 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
