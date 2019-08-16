from form_ui import *
from PyQt5.QtGui import QIcon

class MainWindow(QtWidgets.QMainWindow,Ui_Form):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.ImportData.clicked.connect(self.importData)
        self.ImportData.setIcon(QIcon("icono.ico"))

    def importData(self):
        f = open("Archivo.tsv","r")
        content = f.read()
        content = content.split("\n")
        for i in content:
            item = QtWidgets.QListWidgetItem(QIcon("icono.ico"),i)
            self.list.addItem(item)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()