import numpy as np 

class Human:
    def __init__(self):
        self.direction = (1,0)

    def setdirection(self,mode):
        if mode == 0:
            self.direction = (1,0)
        elif mode == 1:
            self.direction = (-1,0)
        elif mode == 2:
            self.direction = (0,1)
        elif mode == 3:
            self.direction = (0,-1)

    def play(self,head,body,area):
        return self.direction


class Computer:
    def __init__(self):
        pass

    def play(self,head,body,area):
        pass