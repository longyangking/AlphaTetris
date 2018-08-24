import gameengine
import ui
import naiveai

class Human:
    def __init__(self):
        self.mode = 0

    def setdirection(self,mode):
        self.mode = mode

    def play(self,block,area):
        mode = self.mode
        self.mode = 0
        return mode

class NaiveAI:
    def __init__(self,verbose=False):
        self.ai = naiveai.AI(verbose=verbose)

    def setdirection(self,mode):
        pass

    def play(self,block,area):
        return self.ai.play(block,area)

class Tetris:
    def __init__(self, state_shape, player, verbose):
        self.state_shape = state_shape
        self.Nx, self.Ny, self.channel = state_shape
        self.gameengine = None
        self.player = player
        self.ui = None

        self.verbose = verbose

    def start(self,sizeunit = 15):
        self.gameengine = gameengine.GameEngine(Nx=self.Nx,Ny=self.Ny,player=self.player,timeperiod=0.5)
        self.gameengine.start()

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