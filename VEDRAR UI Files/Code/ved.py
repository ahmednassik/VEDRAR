from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton, QLineEdit
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap, QColor
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


        self.setFixedSize(400, 400)
        self.setWindowTitle("VEDRAR")


        subButton = QPushButton('submit', self)
        subButton.move(100, 225)
        subButton.resize(170, 32)
        subButton.clicked.connect(self.regMethod)
        subButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        cancelButton = QPushButton('cancel', self)
        cancelButton.move(250, 225)
        cancelButton.resize(170, 32)
        cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.usernameLabel = QLabel(self)
        self.usernameLabel.setText('Enter ID')
        self.usernameLabel.resize(100, 32)
        self.usernameLabel.move(300, 90)

        self.username_in = QLineEdit(self)
        self.username_in.move(200, 120)
        self.username_in.resize(200, 32)

    def regMethod(self):
        self.hide()
        self.dialog = RegisterWindow()
        self.dialog.show()

class RegisterWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setFixedSize(600, 400)
        self.setWindowTitle("VEDRAR")

        self.usernameLabel = QLabel(self)
        self.usernameLabel.setText('USER ID:')
        self.usernameLabel.resize(800, 32)
        self.usernameLabel.move(80, 20)

        self.usernameLabel = QLabel(self)
        self.usernameLabel.setText('ABOUT DRIVE:')
        self.usernameLabel.resize(200, 64)
        self.usernameLabel.move(10, 80)

        self.usernameLabel = QLabel(self)
        self.usernameLabel.setText('SPEED')
        self.usernameLabel.resize(300, 64)
        self.usernameLabel.move(100, 120)

        sButton = QPushButton('submit', self)
        sButton.move(10, 225)
        sButton.resize(170, 32)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())

