#!/usr/bin/python
#coding=utf-8
import sys
from PyQt4 import  QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QPixmap
from PyQt4.QtGui import QLabel

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ji(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Ji, self).__init__()
        self.picname = "ji.jpg"
        self.picture = QLabel(self)

        self.initUI()

    def initUI(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.load_img()
        self.createContextMenu()

    def load_img(self):
        self.picture.setGeometry(0,0,154,300)
        self.picture.setPixmap(QPixmap(self.picname))

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.buttons() == Qt.LeftButton:
            self.dragPosition = QMouseEvent.globalPos() - self.frameGeometry().topLeft()
            QMouseEvent.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() ==QtCore.Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.dragPosition)
            QMouseEvent.accept()

    def createContextMenu(self):
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)

        # create QMenu
        self.contextMenu = QtGui.QMenu(self)
        self.say_menu = self.contextMenu.addAction(u'Hai')
        self.close_menu = self.contextMenu.addAction(u'close')

        self.say_menu.triggered.connect(self.say_action)
        self.close_menu.triggered.connect(self.colse_action)

    def showContextMenu(self, pos):
        self.contextMenu.move(self.pos() + pos)
        self.contextMenu.show()

    def colse_action(self):
        self.close()

    def say_action(self):
        self.msg = QMessageBox(self)
        self.msg.about(self, "Ji says", "Hai")




def main():
    app = QtGui.QApplication(sys.argv)
    myapp = Ji()
    myapp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
