from PyQt5 import QtCore, QtGui, QtWidgets
from recepti import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(803, 651)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 90, 761, 481))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 20, 113, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 20, 81, 25))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 111, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 20, 69, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 69, 20))
        self.label_3.setObjectName("label_3")
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
        self.label.setText(_translate("MainWindow", "Količina mesa:"))
        self.label_2.setText(_translate("MainWindow", "grama"))
        self.label_3.setText(_translate("MainWindow", "Recept:"))
        self.pushButton_izracunaj.setText(_translate("MainWindow", "Izracunaj"))
        self.pushButton_izlaz.setText(_translate("MainWindow", "Zatvori"))

def izlaz(self):
    sys.exit()


# noinspection PyCallByClass
def ispisi_recept(self):
    ui.textBrowser.setText(tatarski_biftek)

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
