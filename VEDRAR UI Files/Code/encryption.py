from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton, QLineEdit, QFileDialog , QLabel, QGridLayout
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap, QColor
from PyQt5.QtCore import QSize
import sys



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setFixedSize(700, 500)
        self.setWindowTitle("GRAPHICAL PASSWORD SYSTEM")

        oImage = QImage("bg.png")
        sImage = oImage.scaled(QSize(700, 500))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        image = "img3.jpg"
        self.pixmap1 = QPixmap(image)
        self.pixmap1 = self.drawLines(image)
        self.image_label1 = QLabel(self)
        self.image_label1.setPixmap(self.pixmap1)
        self.image_label1.resize(300, 300)
        self.image_label1.move(300, 150)
        self.image_label1.show()
        self.image_label1.mousePressEvent = self.getPixels_1

        self.welcomelabel = QLabel('Welcome', self)
        self.welcomelabel.resize(200, 50)
        self.welcomelabel.move(200,100)
        self.welcomelabel.setText('WELCOME TO GRAPHICAL PASSWORD SYSTEM!')
        self.show()

        self.pushButton1 = QPushButton('Button1', self)
        self.pushButton2 = QPushButton('Button2', self)
        self.pushButton1.clicked.connect(self.Button1Method)
        self.pushButton2.clicked.connect(self.Button2Method)
        self.pushButton1.resize(100, 32)
        self.pushButton2.resize(100, 32)
        self.pushButton1.move(490, 10)
        self.pushButton2.move(490, 50)

        self.sample1_in = QLineEdit(self)
        self.sample1_in.move(20, 40)
        self.sample1_in.resize(400, 30)
        self.sample2_in = QLineEdit(self)
        self.sample2_in.move(20, 200)
        self.sample2_in.resize(400, 30)
        self.setPalette(palette)

        self.chooseButton = QPushButton('Choose file', self)
        self.encryptButton = QPushButton('Encrypt file', self)
        self.chooseButton.clicked.connect(self.OpenFileNamesDialog)
        # self.encryptButton.clicked(self.FileEncryption)
        self.chooseButton.resize(100, 32)
        self.encryptButton.resize(100, 32)
        self.chooseButton.move(450, 40)
        self.encryptButton.move(450, 100)
        self.chooseButton2 = QPushButton('Choose file', self)
        self.decryptButton = QPushButton('Decrypt file', self)
        self.chooseButton2.resize(100, 32)
        self.chooseButton2.move(450, 200)
        self.decryptButton.resize(100, 32)
        self.decryptButton.move(450, 250)

    def WelcomeMethod(self):
        self.dialog = WelcomeMethod()
        self.dialog.show()

    def Button1Method(self):
            self.dialog = Button1Window()
            self.hide()
            self.dialog.show()

    def Button2Method(self):
            self.dialog = Button2Window()
            self.hide()
            self.dialog.show()

    def drawLines(self, image):
            pixmap = QPixmap(image)
            painter = QtGui.QPainter(pixmap)
            pen = QtGui.QPen(QtCore.Qt.white, 0, QtCore.Qt.SolidLine)
            painter.setPen(pen)

            width = 550
            height = 550
            numLines = 11
            numHorizontal = width // numLines
            numVertical = height // numLines
            painter.drawRect(0, 0, height, width)

            for x in range(numLines):
                newH = x * numHorizontal
                newV = x * numVertical
                painter.drawLine(0 + newH, 0, 0 + newH, width)
                painter.drawLine(0, 0 + newV, height, 0 + newV)
            return pixmap

    def getPixels_1(self, event):
            x = event.pos().x()
            y = event.pos().y()

    def OpenFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "File Chooser", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
           self.sample1_in.setText(fileName)

class Button1Window(QMainWindow):
    def __init__(self):
            QMainWindow.__init__(self)
            self.setFixedSize(700, 500)
            self.setWindowTitle("GRAPHICAL PASSWORD SYSTEM")

class Button2Window(QMainWindow):
    def __init__(self):
            QMainWindow.__init__(self)
            self.setFixedSize(700, 500)
            self.setWindowTitle("GRAPHICAL PASSWORD SYSTEM")

    def getPixels_1(self, event):
        x = event.pos().x()
        y = event.pos().y()



class Button1Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(700, 500)
        self.setWindowTitle("GRAPHICAL PASSWORD SYSTEM")

class Button2Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(700, 500)
        self.setWindowTitle("GRAPHICAL PASSWORD SYSTEM")
    def ChoosefileMethod(self):
        self.dialog = Button1Window()
        self.hide()
        self.dialog.show()

    def OpenFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "File Chooser", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
           self.sample1_in.setText(fileName)




class ChooseWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(700, 500)
        self.setWindowTitle("GRAPHICAL PASSWORD SYSTEM")

class EncryptionWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(700, 500)
        self.setWindowTitle("GRAPHICAL PASSWORD SYSTEM")








if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
