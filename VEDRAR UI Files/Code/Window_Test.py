
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton, QLineEdit
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class HomeWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(1000,600)
        self.setWindowTitle("VEDRAR")

        regButton = QPushButton('Add New User', self)
        regButton.move(200, 10)
        regButton.resize(170, 32)
        regButton.setAutoFillBackground(True)
        regButton.clicked.connect(self.regMethod)
        regButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        sendEmailButton = QPushButton('Send Email', self)
        sendEmailButton.resize(170, 32)
        sendEmailButton.move(700, 50)
        sendEmailButton.setAutoFillBackground(True)
        sendEmailButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def regMethod(self):
        self.hide()
        self.dialog = SecondWindow()
        self.dialog.show()

class SecondWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(1000,600)
        self.setWindowTitle("VEDRAR PAGE 2")

        regButton = QPushButton('Add New User', self)
        regButton.move(400, 10)
        regButton.resize(170, 32)
        regButton.setAutoFillBackground(True)
        regButton.clicked.connect(self.regMethod)
        regButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def regMethod(self):
        self.hide()
        self.dialog = HomeWindow()
        self.dialog.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HomeWindow()
    mainWin.show()
    sys.exit(app.exec_())
