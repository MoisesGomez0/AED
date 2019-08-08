from menu_ui import *
from PyQt5.QtGui import QIcon

class MainWindow(QtWidgets.QMainWindow,Ui_Menu):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add)
        self.pushButton.setIcon(QIcon("icono.ico"))
        self.listWidget.itemDoubleClicked.connect(self.labelshow)
    def labelshow(self):
        self.label.setText(self.listWidget.currentItem().text())
    def add(self):
        item = QtWidgets.QListWidgetItem(QIcon("world.ico"),self.lineEdit.displayText())
        self.listWidget.addItem(item)
        self.lineEdit.setText("")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

