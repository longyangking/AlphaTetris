import numpy as np 
import sys
from PyQt5.QtWidgets import QWidget, QApplication,QDesktopWidget
from PyQt5.QtCore import * 
from PyQt5.QtGui import *

# Color Table
WHITE = 0
RED = 1
BLUE = 2
ORANGE = 3
YELLOW = 4
MAGENTA = 5
CYAN = 6
GREEN = 7

class nativeUI(QWidget):
    playsignal = pyqtSignal(int) 

    def __init__(self,pressaction,area,sizeunit):
        super(nativeUI,self).__init__(None)
        self.area = area
        self.sizeunit = sizeunit

        self.ax = sizeunit
        self.ay = sizeunit

        self.pressaction = pressaction
        self.playsignal.connect(self.pressaction) 

        self.isgameend = False
        self.score = 0
        self.initUI()

    def initUI(self):
        (Nx,Ny) = self.area.shape
        screen = QDesktopWidget().screenGeometry()
        size =  self.geometry()

        self.setGeometry((screen.width()-size.width())/2, 
                        (screen.height()-size.height())/2,
                        Nx*self.sizeunit, Ny*self.sizeunit)
        self.setWindowTitle("Retro Snake")

        # set Background color
        palette =  QPalette()
        palette.setColor(self.backgroundRole(), QColor(255,255,255))
        self.setPalette(palette)

        #self.setMouseTracking(True)
        self.show()

    def setarea(self,area):
        self.area = area
        self.update()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)

        self.drawArea(qp)
    
        if self.isgameend:
            self.drawresult(qp)
        qp.end()

    def resizeEvent(self,e):
        (Nx,Ny) = self.area.shape
        size =  self.geometry()
        width = size.width()
        height = size.height()
        self.ax = 1.0*width/Nx
        self.ay = 1.0*height/Ny

    def gameend(self,score):
        self.score = score
        self.isgameend = True
        self.update()

    def drawresult(self,qp):
        # White rectangle
        size =  self.geometry()
        qp.setPen(0)
        qp.setBrush(QColor(200, 200, 200, 180))
        width = size.width()/5*4
        height = size.height()/3
        qp.drawRect(size.width()/2-width/2, size.height()/2-height/2, width, height)

        # Write score
        qp.setPen(QColor(0,0,0))
        font = qp.font()
        font.setPixelSize(width/10)
        qp.setFont(font)
        qp.drawText(QRect(size.width()/2-width/2, size.height()/2-height/2, width, height),	0x0004|0x0080,str("Game End! Score:{score}".format(score=self.score)))

    def drawArea(self,qp):
        (Nx,Ny) = self.area.shape
        qp.setPen(0)
        for i in range(Nx):
            for j in range(Ny):
                if self.area[i,j] == WHITE:
                    qp.setBrush(QColor(255, 255, 255))
                elif self.area[i,j] == RED:
                    qp.setBrush(QColor(255, 0, 0))
                elif self.area[i,j] == GREEN:
                    qp.setBrush(QColor(0,255,0))
                elif self.area[i,j] == BLUE:
                    qp.setBrush(QColor(0,0,255))
                elif self.area[i,j] == ORANGE:
                    qp.setBrush(QColor(255,165,0))
                elif self.area[i,j] == YELLOW:
                    qp.setBrush(QColor(255,255,0))
                elif self.area[i,j] == MAGENTA:
                    qp.setBrush(QColor(255,0,255))
                elif self.area[i,j] == CYAN:
                    qp.setBrush(QColor(0,255,255))
                if self.area[i,j] != 0:
                    qp.drawRect(i*self.ax, j*self.ay ,self.ax,self.ay)

    def closeEvent(self,e):
        pass

    def keyPressEvent(self, e):
        mode = -1

        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_Left:
            mode = 1
        elif e.key() == Qt.Key_Right:
            mode = 2
        elif e.key() == Qt.Key_Space:
            mode = 3
        elif e.key() == Qt.Key_Down:
            mode = 4

        if mode != -1:
            self.playsignal.emit(mode)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    area = np.random.randint(8,size=(10,10))
    sizeunit = 30
    ex = nativeUI(pressaction=lambda x:x,area=area,sizeunit=sizeunit)
    
    sys.exit(app.exec_())

    

