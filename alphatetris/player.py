import numpy as np 
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

class Computer:
    def __init__(self):
        self.ai = naiveai.AI()

    def setdirection(self,mode):
        pass

    def play(self,block,area):
        return self.ai.play(block,area)