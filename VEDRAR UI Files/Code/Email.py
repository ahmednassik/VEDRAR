from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtWidgets import QPushButton, QLineEdit
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
import sys
import pyAesCrypt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from src import fileEncryption, AdminPanel
bufferSize = 64 * 1024


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        homeicon = QtGui.QIcon()
        homeicon.addPixmap(QtGui.QPixmap("home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sendicon = QtGui.QIcon()
        sendicon.addPixmap(QtGui.QPixmap("send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        font = QtGui.QFont("Times", 12, QtGui.QFont.Bold)

        self.setFixedSize(600, 400)
        self.setWindowTitle("SECURE FILE MANAGER")

        oImage = QImage("emailbg.png")
        sImage = oImage.scaled(QSize(600, 400))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        self.toLabel = QtWidgets.QLabel(self)
        self.toLabel.resize(50, 30)
        self.toLabel.move(20, 22)
        self.toLabel.setText("To")
        self.toLabel.setStyleSheet("color:black;font-size:18px")

        self.subLabel = QtWidgets.QLabel(self)
        self.subLabel.resize(100, 30)
        self.subLabel.move(20, 62)
        self.subLabel.setText("Subject")
        self.subLabel.setStyleSheet("color:black;font-size:18px")

        self.bodyLabel = QtWidgets.QLabel(self)
        self.bodyLabel.resize(100, 30)
        self.bodyLabel.move(20, 100)
        self.bodyLabel.setText("Body")
        self.bodyLabel.setStyleSheet("color:black;font-size:18px")

        self.attachLabel = QtWidgets.QLabel(self)
        self.attachLabel.resize(100, 30)
        self.attachLabel.move(20, 285)
        self.attachLabel.setText("Attachment")
        self.attachLabel.setStyleSheet("color:black;font-size:18px")

        self.encKeyLabel = QtWidgets.QLabel(self)
        self.encKeyLabel.resize(150, 30)
        self.encKeyLabel.move(20, 245)
        self.encKeyLabel.setText("Encryption Key")
        self.encKeyLabel.setStyleSheet("color:black;font-size:18px")


        self.toEdit = QLineEdit(self)
        self.toEdit.resize(400, 25)
        self.toEdit.move(170, 25)
        self.toEdit.setStyleSheet("font-size:16px")

        self.subEdit = QLineEdit(self)
        self.subEdit.resize(400, 25)
        self.subEdit.move(170, 65)
        self.subEdit.setStyleSheet("font-size:16px")

        self.bodyEdit = QtWidgets.QPlainTextEdit(self)
        self.bodyEdit.resize(400, 125)
        self.bodyEdit.move(170, 105)
        self.bodyEdit.setStyleSheet("font-size:16px")

        self.attachKeyEdit = QLineEdit(self)
        self.attachKeyEdit.resize(300, 25)
        self.attachKeyEdit.move(170, 285)
        self.attachKeyEdit.setStyleSheet("font-size:16px")

        self.chooseButton = QPushButton('Choose', self)
        self.chooseButton.clicked.connect(self.OpenFileNamesDialog1)
        self.chooseButton.setFont(font)
        self.chooseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chooseButton.resize(80,30)
        self.chooseButton.move(490,282)

        self.encKeyEdit = QLineEdit(self)
        self.encKeyEdit.resize(400, 25)
        self.encKeyEdit.move(170, 245)
        self.encKeyEdit.setStyleSheet("font-size:16px")
        self.encKeyEdit.setEchoMode(QLineEdit.Password)

        home = QPushButton('Go Home', self)
        home.resize(100, 30)
        home.move(10, 360)
        home.setIcon(homeicon)
        home.clicked.connect(self.goHome)
        home.setStyleSheet("font-size:15px")
        home.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        send = QPushButton('Send', self)
        send.resize(100, 30)
        send.move(280, 330)
        send.setIcon(sendicon)
        send.clicked.connect(self.sendMail)
        send.setStyleSheet("font-size:15px")
        send.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def goHome(self):
        self.dialoag = AdminPanel.MainWindow()
        self.hide()
        self.dialoag.show()
    def sendMail(self):
      try:
        fromaddr = "nithinkurian777@gmail.com"
        print(fromaddr)
        toaddr = self.toEdit.text()
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = self.subEdit.text()
        body = self.bodyEdit.toPlainText()
        msg.attach(MIMEText(body, 'plain'))
        filename = self.attachKeyEdit.text()
        attachment = open(self.file, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % self.file)
        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "login@123")
        text = msg.as_string()

        s.sendmail(fromaddr, toaddr, text)

        s.quit()
        QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Success',
                                      'Mail sent Successfully!')
      except:
        QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error',
                                    'Mail sending Failed!')
    def OpenFileNamesDialog1(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Select File", "","All Files (*)", options=options)
        if fileName:
            self.attachKeyEdit.setText(fileName)
            self.fileEnc()

    def fileEnc(self):
        file_url = self.attachKeyEdit.text()
        file_url_words = file_url.split('/')
        file_url_size = len(file_url_words)
        self.file = file_url_words[file_url_size - 1]
        self.file += ".aes"
        try:
            pyAesCrypt.encryptFile(self.attachKeyEdit.text(), self.file, self.encKeyEdit.text(), bufferSize)
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Success',
                                          'File Encryption Successful!')

        except Exception:
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error',
                                          'File Encryption Failed!')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())