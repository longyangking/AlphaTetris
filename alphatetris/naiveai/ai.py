import numpy as np 

class AI:
    def __init__(self,deep=5):
        self.block = None
        self.area = None
        self.deep = deep

    def __values(self):
        # Calculate the values of modes：{0,1,2,3,4}
        

    def __search(self,mode,deep):
        

    def play(self,block,area):
        self.area = area.copy()
        self.block = block

        # Choose mode：{0,1,2,3,4}
        values = self.__values()
        mode = np.argmax(values)
        return mode
