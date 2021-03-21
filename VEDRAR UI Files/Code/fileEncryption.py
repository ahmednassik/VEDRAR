from PyQt5.QtWidgets import QMainWindow, QPushButton, QFileDialog, QLineEdit
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
import sys
import pyAesCrypt
from src import AdminPanel
import os

bufferSize = 64 * 1024

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        font = QtGui.QFont("Times", 10)
        font2 = QtGui.QFont("Times", 20, QtGui.QFont.Bold)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.setFixedSize(600, 400)
        self.setWindowTitle("SECURE FILE MANAGER")

        oImage = QImage("bg4.jpg")
        sImage = oImage.scaled(QSize(600, 400))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("Encryption")
        self.label1.setFont(font2)
        self.label1.resize(200, 40)
        self.label1.move(220, 10)
        self.label1.setStyleSheet("color:rgb(0,255,255);")
        self.label1.show()

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("Decryption")
        self.label2.setFont(font2)
        self.label2.resize(200, 40)
        self.label2.move(220, 200)
        self.label2.setStyleSheet("color:rgb(0,255,255);")
        self.label2.show()

        self.sample1_in = QLineEdit(self)
        self.sample1_in.move(20, 70)
        self.sample1_in.resize(400, 30)
        self.sample2_in = QLineEdit(self)
        self.sample2_in.move(20, 250)
        self.sample2_in.resize(400, 30)
        self.setPalette(palette)
        self.sample1_in.setDisabled(True)
        self.sample2_in.setDisabled(True)

        self.hline = QtWidgets.QFrame(self)
        self.hline.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline.move(0, 180)
        self.hline.setFixedWidth(600)
        self.hline.setLineWidth(2)
        self.hline.show()

        self.chooseButton = QPushButton('Choose File', self)
        self.encryptButton = QPushButton('Encrypt File', self)
        self.chooseButton.clicked.connect(self.OpenFileNamesDialog1)
        self.encryptButton.clicked.connect(self.fileEnc)
        self.chooseButton.setFont(font)
        self.encryptButton.setFont(font)
        self.encryptButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # self.encryptButton.clicked(self.FileEncryption)
        self.chooseButton.resize(100, 32)
        self.encryptButton.resize(100, 32)
        self.chooseButton.move(450, 69)
        self.encryptButton.move(450, 125)
        self.chooseButton2 = QPushButton('Choose File', self)
        self.decryptButton = QPushButton('Decrypt File', self)
        self.chooseButton2.resize(100, 32)
        self.chooseButton2.move(450, 249)
        self.chooseButton2.clicked.connect(self.OpenFileNamesDialog2)
        self.decryptButton.resize(100, 32)
        self.decryptButton.move(450, 300)
        self.decryptButton.clicked.connect(self.fileDec)
        self.chooseButton2.setFont(font)
        self.decryptButton.setFont(font)
        self.decryptButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.encKeyLabel = QtWidgets.QLabel(self)
        self.encKeyLabel.resize(150,30)
        self.encKeyLabel.move(30,120)
        self.encKeyLabel.setText("Encryption Key")
        self.encKeyLabel.setStyleSheet("color:white;font-size:18px")

        self.decKeyLabel = QtWidgets.QLabel(self)
        self.decKeyLabel.resize(150, 30)
        self.decKeyLabel.move(30, 295)
        self.decKeyLabel.setText("Decryption Key")
        self.decKeyLabel.setStyleSheet("color:white;font-size:18px")

        self.encKeyEdit = QLineEdit(self)
        self.encKeyEdit.resize(150,25)
        self.encKeyEdit.move(200, 125)
        self.encKeyEdit.setEchoMode(QLineEdit.Password)

        self.decKeyEdit = QLineEdit(self)
        self.decKeyEdit.resize(150, 25)
        self.decKeyEdit.move(200, 300)
        self.decKeyEdit.setEchoMode(QLineEdit.Password)

        self.home = QPushButton('Go Home', self)
        self.home.resize(80, 30)
        self.home.move(10, 360)
        self.home.clicked.connect(self.goHome)
        self.home.show()
        self.home.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def OpenFileNamesDialog1(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Select File", "",
                                                  "All Files (*)", options=options)
        if fileName:
            self.sample1_in.setText(fileName)

    def OpenFileNamesDialog2(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Select File", "",
                                                  "Encrypted Files (*.aes)", options=options)
        if fileName:
            self.sample2_in.setText(fileName)

    def fileEnc(self):
        file_url = self.sample1_in.text()
        file_url_words = file_url.split('/')
        file_url_size = len(file_url_words)
        file = file_url_words[file_url_size - 1]
        file += ".aes"
        try:

            pyAesCrypt.encryptFile(self.sample1_in.text(), file, self.encKeyEdit.text(), bufferSize)
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Success',
                                          'File Encryption Successful!')
            self.encKeyEdit.clear()
            if os.path.exists(file_url):
                os.remove(file_url)
            else:
                print("The file does not exist")
        except Exception:
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error',
                                          'File Encryption Failed!')

    def fileDec(self):
        file_url = self.sample2_in.text()
        file_url_words = file_url.split('/')
        file_url_size = len(file_url_words)
        file = file_url_words[file_url_size - 1]
        file_size = len(file)
        print(file_size)
        file_out = file[:-4]
        print(file_out)
        try:
            pyAesCrypt.decryptFile(file, file_out, self.decKeyEdit.text(), bufferSize)
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Success',
                                          'File Decryption Successful!')
            self.decKeyEdit.clear()
            if os.path.exists(file_url):
                os.remove(file_url)
            else:
                print("The file does not exist")
        except Exception:
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error',
                                          'File Decryption Failed!')

    def goHome(self):
        self.hide()
        self.dialog = AdminPanel.MainWindow()
        self.dialog.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
