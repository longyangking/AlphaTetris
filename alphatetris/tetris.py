import gameengine
import ui
import player


class Tetris:
    def __init__(self,Nx,Ny):
        self.Nx = Nx
        self.Ny = Ny
        self.gameengine = None
        self.player = player.Human()
        self.ui = None

    def start(self):
        self.gameengine = gameengine.GameEngine(Nx=self.Nx,Ny=self.Ny,player=self.player,timeperiod=0.5)
        self.gameengine.start()

        sizeunit = 15
        area = self.gameengine.getarea()
        self.ui = ui.UI(pressaction=self.player.setdirection,area=area,sizeunit=sizeunit)
        self.ui.start()
        
        while self.gameengine.update():
            self.ui.setarea(area=self.gameengine.getarea())

        self.ui.gameend(self.gameengine.getscore())

if __name__=="__main__":
    Nx,Ny = 15,40
    tetris = Tetris(Nx,Ny)
    tetris.start()