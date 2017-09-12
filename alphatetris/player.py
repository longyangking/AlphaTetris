import numpy as np 

class Human:
    def __init__(self):
        self.mode = 0

    def setdirection(self,mode):
        self.mode = mode

    def play(self,position,shape,area):
        mode = self.mode
        self.mode = 0
        return mode

class Computer:
    def __init__(self):
        pass

    def play(self,head,body,area):
        pass