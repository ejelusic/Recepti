from PyQt5 import QtCore, QtGui, QtWidgets
from recepti import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(803, 651)
        MainWindow.setWindowIcon(QtGui.QIcon('slike\logo.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 90, 761, 481))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 20, 113, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.jelo = QtWidgets.QComboBox(self.centralwidget)
        self.jelo.setGeometry(QtCore.QRect(60, 20, 81, 25))
        self.jelo.setObjectName("comboBox")
        self.meso = QtWidgets.QLabel(self.centralwidget)
        self.meso.setGeometry(QtCore.QRect(190, 22, 111, 20))
        self.meso.setObjectName("label")
        self.naziv = QtWidgets.QLabel(self.centralwidget)
        self.naziv.setGeometry(QtCore.QRect(20, 22, 69, 20))
        self.naziv.setObjectName("naziv")
        self.grama = QtWidgets.QLabel(self.centralwidget)
        self.grama.setGeometry(QtCore.QRect(390, 22, 69, 20))
        self.grama.setObjectName("label_2")
        self.Recept = QtWidgets.QLabel(self.centralwidget)
        self.Recept.setGeometry(QtCore.QRect(20, 60, 69, 20))
        self.Recept.setObjectName("label_3")
        self.pushButton_izracunaj = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_izracunaj.setGeometry(QtCore.QRect(470, 20, 89, 28))
        self.pushButton_izracunaj.setObjectName("pushButton")
        self.pushButton_izlaz = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_izlaz.setGeometry(QtCore.QRect(20, 580, 89, 28))
        self.pushButton_izlaz.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.kolicina_mesa = ui.lineEdit.text()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Preračun količina sastojaka u odnosu na količinu mesa"))
        self.meso.setText(_translate("MainWindow", "Količina mesa:"))
        self.grama.setText(_translate("MainWindow", "grama"))
        self.Recept.setText(_translate("MainWindow", "Recept:"))
        self.naziv.setText(_translate("MainWindow", "Jelo:"))
        self.pushButton_izracunaj.setText(_translate("MainWindow", "Izracunaj"))
        self.pushButton_izlaz.setText(_translate("MainWindow", "Zatvori"))
        self.jelo.addItem("Tatarski")
        self.jelo.addItem("Bolognese")
        self.jelo.addItem("Hamburger")

def izlaz(self):
    sys.exit()


# noinspection PyCallByClass
def ispisi_recept(self):
    if ui.lineEdit.text():
        kolicina_mesa = int(ui.lineEdit.text())
        if ui.jelo.currentText() == "Tatarski":
            ui.textBrowser.setText(izracun_tatarski(kolicina_mesa))
        if ui.jelo.currentText() == "Bolognese":
            ui.textBrowser.setText(izracun_bolognese(kolicina_mesa))
        if ui.jelo.currentText() == "Hamburger":
            ui.textBrowser.setText(izracun_hamburger(kolicina_mesa))
    else:
        ui.textBrowser.setText("MOLIM UNESITE KOLIČINU MESA!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.pushButton_izracunaj.clicked.connect(ispisi_recept)

    ui.pushButton_izlaz.clicked.connect(izlaz)
    MainWindow.show()
    sys.exit(app.exec_())
