#!/usr/bin/python
#coding=utf-8
import sys
from PyQt4 import  QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QPixmap
from PyQt4.QtCore import QRect
from PyQt4.QtGui import QImage
from PyQt4.QtGui import QPainter



try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Chii(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Chii, self).__init__()
        self.picnames = ["chii.png","chii2.png"]
        self.pictures = []
        self.current_pic = None
        self.current_pic_num = 0
        self.initui()

    def initui(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.load_img()
        self.createContextMenu()

    def load_img(self):
        for picname in self.picnames:
            self.pictures.append(QPixmap(picname))
        self.current_pic = self.pictures[self.current_pic_num]
        self.setMask(self.current_pic.mask())

    def paintEvent(self, QPaintEvent):
        self.setMask(self.current_pic.mask())
        self.resize(self.current_pic.width(),self.current_pic.height())
        self.painter = QPainter()
        self.painter.begin(self)
        self.img = QImage(self.current_pic.toImage())
        self.pic_rect = QRect(0, 0, self.current_pic.width(), self.current_pic.height())
        self.painter.drawImage(self.pic_rect, self.img)
        self.painter.end()

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
        self.changpic_menu = self.contextMenu.addAction(u'changepicture')
        self.close_menu = self.contextMenu.addAction(u'close')

        self.say_menu.triggered.connect(self.say_action)
        self.changpic_menu.triggered.connect(self.changpic)
        self.close_menu.triggered.connect(self.colse_action)

    def showContextMenu(self, pos):
        self.contextMenu.move(self.pos() + pos)
        self.contextMenu.show()

    def changpic(self):
        if self.current_pic_num < len(self.pictures)-1:
            self.current_pic_num += 1
        else:
            self.current_pic_num = 0
        self.current_pic = self.pictures[self.current_pic_num]
        self.update()

    def colse_action(self):
        self.close()

    def say_action(self):
        self.msg = QMessageBox(self)
        self.msg.about(self, "Chii says", "Chii")




def main():
    app = QtGui.QApplication(sys.argv)
    myapp = Chii()
    myapp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
