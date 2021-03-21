from PyQt5 import QtWidgets, QtGui, QtCore
import sys
class imageSelector(QtWidgets.QWidget):

    def __init__(self):
        super(imageSelector,self).__init__()
        self.initIS()

    def initIS(self):
        self.pixmap = self.createPixmap()

        painter = QtGui.QPainter(self.pixmap)
        pen = QtGui.QPen(QtCore.Qt.white, 0, QtCore.Qt.SolidLine)
        painter.setPen(pen)

        # width = self.pixmap.width()
        # height = self.pixmap.height()

        width = 400
        height = 400
        numLines = 6
        numHorizontal = width//numLines
        numVertical = height//numLines
        painter.drawRect(0,0,height,width)

        for x in range(numLines):
            newH = x * numHorizontal
            newV = x * numVertical
            painter.drawLine(0+newH,0,0+newH,width)
            painter.drawLine(0,0+newV,height,0+newV)

        label = QtWidgets.QLabel()
        label.setPixmap(self.pixmap)
        label.resize(label.sizeHint())

        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(label)

        self.setLayout(hbox)
        self.show()

    def createPixmap(self):
        pixmap = QtGui.QPixmap("bg.png")#.scaledToHeight(500)
        return pixmap


def main():
    app = QtWidgets.QApplication(sys.argv)
    Im = imageSelector()
    Im.setFixedSize(400,400)
    sys.exit(app.exec_())

if __name__== '__main__':
    main()
