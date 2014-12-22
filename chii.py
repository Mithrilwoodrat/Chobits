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
from PyQt4.QtCore import QString


"""fun to read cpu info """
try:
    import psutil
    def currentCPU(time):
        return psutil.cpu_percent(time)
except ImportError:
    def currentCPU(time):
        print "no moudle named psutil"
        return 0
        
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Chii(QtGui.QWidget):
    """
    Chobits (ちょびっツ Chobittsu?) is a Japanese manga created by the Japanese manga collective Clamp
    Chi (ちぃ Chii?) is A "chobit"
    wikipedia : http://en.wikipedia.org/wiki/Chobits
    """
    
    def __init__(self, parent=None):
        super(Chii, self).__init__()
        self.picnames = ["./pictures/chii.png","./pictures/chii3.png"]
        self.pictures = []
        self.current_pic = None
        self.current_pic_num = 0
        self.word = ""
        self.talkflag = 0
        self.initui()

    def initui(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.load_img()
        self.createContextMenu()

    def load_img(self):
        """function to load pictures """
        #add pictures to picture list
        for picname in self.picnames:
            self.pictures.append(QPixmap(picname))
        self.current_pic = self.pictures[self.current_pic_num]
        self.width,self.height = self.current_pic.width(),self.current_pic.height()
        self.setMask(self.current_pic.mask())

    def paintEvent(self, QPaintEvent):
        self.setMask(self.current_pic.mask())
        self.resize(self.current_pic.width(),self.current_pic.height())
        self.painter = QPainter()
        self.painter.begin(self)
        
        self.drawImg()
        self.drawWord()
        self.painter.end()

    def drawImg(self):
        self.painter.save()
        self.img = QImage(self.current_pic.toImage())
        self.pic_rect = QRect(0, 0, self.current_pic.width(), self.current_pic.height())
        self.painter.drawImage(self.pic_rect, self.img)
        self.painter.restore()
        
    def drawWord(self):
        self.painter.save()
        self.painter.setPen(Qt.black)
        self.painter.setBrush(Qt.black)
        if self.talkflag ==1:
            word = QString(self.word)
        else:
            word = ""
        fm = QtGui.QFontMetricsF(self.font())
        w = fm.size(Qt.TextSingleLine,word).width()
        self.painter.drawText(self.width, 50, word)
        self.painter.restore()

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
        
        self.talk_menu = self.contextMenu.addAction(u'talk')
        self.status_menu = self.contextMenu.addAction(u'status')
        self.about_menu = self.contextMenu.addAction(u'about')
        self.close_menu = self.contextMenu.addAction(u'close')
        
        
        self.talk_menu.triggered.connect(self.talk_action)
        self.status_menu.triggered.connect(self.status_action)
        self.about_menu.triggered.connect(self.about_action)
        self.close_menu.triggered.connect(self.colse_action)
        
    def showContextMenu(self, pos):
        self.contextMenu.move(self.pos() + pos)
        self.contextMenu.show()

    def changpic(self):
        """ change the picture to a picture with textfield"""
        if self.current_pic_num < len(self.pictures)-1:
            self.current_pic_num += 1
        else:
            self.current_pic_num = 0
        self.current_pic = self.pictures[self.current_pic_num]
        self.update()

    def status_action(self):
        self.changpic()
        self.talkflag =1
        self.word = "CPU : "+str(currentCPU(0))+"%"
        
    def talk_action(self):
        self.changpic()
        self.talkflag = 1
        self.word = "Chii"
        
    def colse_action(self):
        self.close()

    def about_action(self):
        self.msg = QMessageBox(self)
        self.msg.about(self, "About", "Author:Mithrilwoodrat")

def main():
    app = QtGui.QApplication(sys.argv)
    myapp = Chii()
    myapp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
