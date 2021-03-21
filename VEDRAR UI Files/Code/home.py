import sys
import sqlite3
import smtplib


from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtWidgets import QPushButton, QLineEdit
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap
from src import fileEncryption, AdminPanel
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        font = QtGui.QFont("Times", 12, QtGui.QFont.Bold)


        self.setFixedSize(600, 400)
        self.setWindowTitle("SECURE FILE MANAGER")

        oImage = QImage("bg1.jpg")
        sImage = oImage.scaled(QSize(600, 400))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)


        logButton = QPushButton('Login', self)
        logButton.setFont(font);
        logButton.clicked.connect(self.loginMethod);
        logButton.resize(120, 32)
        logButton.move(230, 280)
        logButton.setAutoFillBackground(True)
        logButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def loginMethod(self):
        self.dialog = LoginWindow()
        self.hide()
        self.dialog.show()




class LoginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        font = QtGui.QFont("Times", 12)
        self.setWindowIcon(icon)
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        self.flag = 1

        self.setFixedSize(600, 400)
        self.setWindowTitle("SECURE FILE MANAGER")

        oImage = QImage("bg3.jpg")
        sImage = oImage.scaled(QSize(600, 400))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.submit = QPushButton('Submit', self)
        self.submit.resize(100, 30)
        self.submit.move(70, 90)
        self.submit.clicked.connect(self.firstImage)
        self.submit.setFont(font)
        self.submit.setAutoFillBackground(True)
        self.submit.setStyleSheet("background-color:rgb(255,0,255);color:rgb(255,255,255);")
        self.submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        home = QPushButton('Go Home', self)
        home.resize(100, 30)
        home.move(10, 360)
        home.clicked.connect(self.goHome)
        home.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.usernameLabel = QLabel(self)
        self.usernameLabel.setText('Username')
        self.usernameLabel.move(20, 10)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setStyleSheet("color: rgb(255, 255, 255);")

        self.username_in = QLineEdit(self)
        self.username_in.move(20, 40)
        self.username_in.resize(200, 32)
        self.username_in.setFont(font)

        self.forgotpass = QtWidgets.QPushButton(self)
        self.forgotpass.setText('Forgot Password?')
        font2 = QtGui.QFont('Times',10)
        self.forgotpass.setFont(font2)
        self.forgotpass.resize(130,30)
        self.forgotpass.move(55,130)
        self.forgotpass.setStyleSheet("color:black;background-color:rgb(0,255,255);")
        self.forgotpass.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.forgotpass.clicked.connect(self.sendMail)
        self.forgotpass.show()

    def sendMail(self):
       if self.username_in.text()!="":
         try:

            for row in self.c.execute("select * from userdata where username = ?",[self.username_in.text()]):
                email = row[7]
                seg1 = row[1]
                seg2 = row[2]
                seg3 = row[3]
            fromaddr = "nithinkurian777@gmail.com"
            toaddr = email
            print(toaddr)
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "Secure File Manager Credentials"
            body = "Your credentials are\n segment no.1 : "+str(seg1)+"\n segment no.2 : "+str(seg2)+"\n segment no.3 : "+str(seg3)
            print(body)
            msg.attach(MIMEText(body, 'plain'))
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(fromaddr, "login@123")
            text = msg.as_string()

            s.sendmail(fromaddr, toaddr, text)

            s.quit()

            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Message',
                                          'Your credentials have sent to the registered mail id.')
         except Exception:
             QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error',
                                           'Username may not exist.')
       else:
           QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error',
                                         'Database Error.')

    def getPixels_1(self, event):
        self.next1.show()
        x = event.pos().x()
        y = event.pos().y()
        segment = self.segmentCalc(x, y)
        print(x, y)
        username = self.username_in.text()
        try:
            for row in self.c.execute("select * from userdata where username = ?", [username]):
                if row[1] != segment:
                    self.flag = 0



        except Exception:
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error',
                                          'Could not add data to the database.\n User may already exist')

    def getPixels_2(self, event):
        self.next2.show()
        x = event.pos().x()
        y = event.pos().y()
        print(x, y)
        segment = self.segmentCalc(x, y)
        username = self.username_in.text()
        try:
            for row in self.c.execute("select * from userdata where username = ?", [username]):
                if row[2] != segment:
                    self.flag = 0

        except Exception:
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error',
                                          'Could not add data to the database.\n User may already exist')

    def getPixels_3(self, event):
        self.next3.show()
        x = event.pos().x()
        y = event.pos().y()
        print(x, y)
        segment = self.segmentCalc(x, y)
        username = self.username_in.text()
        try:
            for row in self.c.execute("select * from userdata where username = ?", [username]):
                if row[3] != segment:
                    self.flag = 0


        except Exception:
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error',
                                          'Could not add data to the database.\n User may already exist')



    def firstImage(self):
        if self.username_in.text() != "":
            username = self.username_in.text()
            i = 0
            for item in self.c.execute("select * from userdata  where username = ?", [username]):
                i = i + 1
                self.img1 = item[4]
                self.img2 = item[5]
                self.img3 = item[6]
            if i == 0:
                QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error', 'User not exist')
                return 0

            self.submit.hide()
            self.username_in.setDisabled(True)
            image = self.img1
            self.pixmap1 = self.drawLines(image)
            self.image_label1 = QLabel(self)
            self.image_label1.setPixmap(self.pixmap1)
            self.image_label1.resize(280, 250)
            self.image_label1.move(300, 40)
            self.image_label1.mousePressEvent = self.getPixels_1
            self.image_label1.show()

            self.next1 = QPushButton('Next', self)
            self.next1.clicked.connect(self.secondImage)
            self.next1.resize(100, 30)
            self.next1.move(300, 300)
            self.next1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))



        else:
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error',
                                          'Username Field Cannot be empty.')

    def secondImage(self):
        self.image_label1.hide()
        self.next1.hide()
        image = self.img2

        self.pixmap1 = self.drawLines(image)
        self.image_label2 = QLabel(self)
        self.image_label2.setPixmap(self.pixmap1)
        self.image_label2.resize(280, 250)
        self.image_label2.move(300, 40)
        self.image_label2.mousePressEvent = self.getPixels_2
        self.image_label2.show()

        self.next2 = QPushButton('Next', self)
        self.next2.clicked.connect(self.thirdImage)
        self.next2.resize(100, 30)
        self.next2.move(300, 300)
        self.next2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


    def thirdImage(self):
        self.image_label2.hide()
        self.next2.hide()
        image = self.img3

        self.pixmap1 = self.drawLines(image)
        self.image_label3 = QLabel(self)
        self.image_label3.setPixmap(self.pixmap1)
        self.image_label3.resize(280, 250)
        self.image_label3.move(300, 40)
        self.image_label3.mousePressEvent = self.getPixels_3
        self.image_label3.show()

        self.next3 = QPushButton('Finish', self)
        self.next3.clicked.connect(self.Finish)
        self.next3.resize(100, 30)
        self.next3.move(300, 300)
        self.next3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


    def goHome(self):
        self.dialoag = MainWindow()
        self.hide()
        self.dialoag.show()

    def drawLines(self, image):
        pixmap = QPixmap(image)
        painter = QtGui.QPainter(pixmap)
        pen = QtGui.QPen(QtCore.Qt.white, 0, QtCore.Qt.SolidLine)
        painter.setPen(pen)

        width = 560
        height = 500
        numLines = 6
        numHorizontal = width // numLines
        numVertical = height // numLines
        painter.drawRect(0, 0, height, width)

        for x in range(numLines):
            newH = x * numHorizontal
            newV = x * numVertical
            painter.drawLine(0 + newH, 0, 0 + newH, width)
            painter.drawLine(0, 0 + newV, height, 0 + newV)
        return pixmap

    def Finish(self):
        if self.flag == 0:
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error',
                                          'Access Denied')

        elif self.flag == 1:
            self.dialoag = AdminPanel.MainWindow()
            self.hide()
            self.dialoag.show()

    def segmentCalc(self, x, y):
        if x >= 1 and x <= 94:
            if y >= 1 and y <= 84:
                segment = 1
            elif y >= 95 and y <= 168:
                segment = 4
            elif y >= 169 and y <= 250:
                segment = 7

        elif x >= 95 and x <= 186:
            if y >= 1 and y <= 84:
                segment = 2
            elif y >= 95 and y <= 168:
                segment = 5
            elif y >= 169 and y <= 250:
                segment = 8
        elif x >= 187 and x <= 280:
            if y >= 1 and y <= 84:
                segment = 3
            elif y >= 95 and y <= 168:
                segment = 6
            elif y >= 169 and y <= 250:
                segment = 9

        return segment



class EncryptWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setFixedSize(600, 400)
        self.setWindowTitle("SECURE FILE MANAGER")

        oImage = QImage("bg.png")
        sImage = oImage.scaled(QSize(600, 400))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.enc_file_in = QLineEdit()
        self.enc_file_in.resize(100,20)
        self.enc_file_in.move(50, 50)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
