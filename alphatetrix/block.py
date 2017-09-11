import numpy as np 

# Seven basic shape
I,J,L,O,S,T,Z = 1,2,3,4,5,6,7

class Block:
    def __init__(self,pos,shape=None):
        self.pos = pos
        if shape is None:
            self.shape = np.random.randint(1,8)
        else:
            self.shape = shape

    def move(self,direction):
    