from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton, QLineEdit
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap, QColor
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        font = QtGui.QFont("Times", 12, QtGui.QFont.Bold)


        self.setFixedSize(600, 400)
        self.setWindowTitle("VEDRAR : Vehicle Event Data Recording & Review System")

        self.usernameLabel = QLabel(self)
        self.usernameLabel.setText(' V     E     D     R     A     R  ')
        self.usernameLabel.setFont(font)
        self.usernameLabel.resize(300,100)
        self.usernameLabel.move(200, 50)

        oImage = QImage("smk.jpg")
        sImage = oImage.scaled(QSize(600, 400))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        subButton = QPushButton('submit', self)
        subButton.move(300, 225)
        subButton.resize(175, 32)
        subButton.clicked.connect(self.regMethod)
        subButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


        cancelButton = QPushButton('cancel', self)
        cancelButton.move(100, 225)
        cancelButton.resize(175, 32)
        cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


        self.usernameLabel = QLabel(self)
        self.usernameLabel.setText('Enter ID')
        self.usernameLabel.setFont(font)
        self.usernameLabel.resize(200, 32)
        self.usernameLabel.move(150,175)

        self.username_in = QLineEdit(self)
        self.username_in.move(300,175)
        self.username_in.resize(175, 32)
#        self.username_in = QLineEdit.text()
        
    def regMethod(self):
        self.hide()
        self.dialog = RegisterWindow()
        self.dialog.show()

class RegisterWindow(QMainWindow):
      def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(600, 400)
        self.setWindowTitle("VEDRAR")
        
        if(result==1):
            self.usernameLabel = QLabel(self)
            self.usernameLabel.setText("CONGRATULATION  :    YOU HAVE PASSED THE TEST")
            self.usernameLabel.resize(300,100)
            self.usernameLabel.move(150, 275)
        else:
            self.usernameLabel = QLabel(self)
            self.usernameLabel.setText("Sorry  :    YOU HAVE FAILED THE TEST")
            self.usernameLabel.resize(300,100)
            self.usernameLabel.move(150, 275)
       
        oImage = QImage("smk.jpg")
        sImage = oImage.scaled(QSize(600, 400))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)


        self.usernameLabel = QLabel(self)
        self.usernameLabel.setText('USER ID:')
        self.usernameLabel.resize(70, 22)
        self.usernameLabel.move(80, 20)


#        self.usernameLabel = QLabel(self)
#        self.usernameLabel.setText('ABOUT DRIVE:')
#        self.usernameLabel.resize(300, 64)
#        self.usernameLabel.move(100, 80)
#
#        self.usernameLabel = QLabel(self)
#        self.usernameLabel.setText('SPEED')
#        self.usernameLabel.resize(300, 64)
#        self.usernameLabel.move(300, 120)
#
#        self.usernameLabel = QLabel(self)
#        self.usernameLabel.setText('PROXIMITY')
#        self.usernameLabel.resize(300, 64)
#        self.usernameLabel.move(300, 160)
#
#        self.usernameLabel = QLabel(self)
#        self.usernameLabel.setText('TILT')
#        self.usernameLabel.resize(300, 64)
#        self.usernameLabel.move(300, 200)



        cancelButton = QPushButton('LOGIN ANOTHER ID', self)
        cancelButton.move(395,15)
        cancelButton.resize(170, 32)
        cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

#        cancelButton = QPushButton('PASS', self)
#        cancelButton.move(380,145)
#        cancelButton.resize(80,20)
#        cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#
#        cancelButton = QPushButton('FAIL', self)
#        cancelButton.move(480, 145)
#        cancelButton.resize(80, 20)
#        cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#
#        cancelButton = QPushButton('PASS', self)
#        cancelButton.move(380,185)
#        cancelButton.resize(80,20)
#        cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#
#        cancelButton = QPushButton('FAIL', self)
#        cancelButton.move(480, 185)
#        cancelButton.resize(80, 20)
#        cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#
#
#        cancelButton = QPushButton('PASS', self)
#        cancelButton.move(380,225)
#        cancelButton.resize(80,20)
#        cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#
#        cancelButton = QPushButton('FAIL', self)
#        cancelButton.move(480, 225)
#        cancelButton.resize(80, 20)
#        cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    
#    id=mainWin.line_value()
    
sys.exit(app.exec_())

