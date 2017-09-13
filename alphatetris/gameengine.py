import numpy as np 
import block
import time

class GameEngine:
    def __init__(self,Nx,Ny,player,timeperiod=1.0):
        self.Nx = Nx
        self.Ny = Ny
        self.block = None
        self.score = 0
        self.player = player
        self.timeperiod = timeperiod

        self.area = np.zeros((Nx,Ny))
    
    def getarea(self):
        return self.area
    
    def getscore(self):
        return self.score

    def start(self):
        # Initiate the retro snake
        position = (int(self.Nx/2),0)
        self.block = block.Block(position=position,player=self.player)
        self.prearea = self.area.copy()
        
        return True

    def restart(self):
        return self.start()

    def updatearea(self):
        body = self.block.getbody()
        shape = self.block.getshape()

        if self.block.survive(area=self.prearea):
            self.area = self.prearea.copy()
            for pos in body:
                self.area[pos] = shape
        else:
            for pos in body:
                self.prearea[pos] = shape
            self.area = self.prearea.copy()

            position = (int(self.Nx/2),0)
            self.block = block.Block(position=position,player=self.player)

        # To cancel one line
        for j in range(self.Ny):
            if np.sum(self.prearea[:,j]!=0) == self.Nx:
                self.prearea[:,1:j+1] = self.prearea[:,0:j]

    def tocontinue(self):
        for i in range(self.Nx):
            if self.prearea[i,0] != 0:
                return False
        return True

    def update(self):

        starttime = time.time()
        self.block.update(self.prearea)
        endtime = time.time()
        if self.timeperiod-(endtime-starttime) > 0:
            time.sleep(self.timeperiod-(endtime-starttime))

        self.updatearea()   # Update Area

        return self.tocontinue()