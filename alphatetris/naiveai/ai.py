import numpy as np 
import copy

class AI:
    def __init__(self,deep=3):
        self.block = None
        self.area = None
        self.deep = deep

    def __values(self):
        # Calculate the values of modes：{0,1,2,3,4}
        values = list()
        print('Thinking...')
        for mode in range(5):
            values.append(self.__search(self.block,mode,self.deep))
        return values

    def __search(self,block,mode,deep):
        newblock = copy.deepcopy(block)
        newblock.action(mode,self.area)
        value = self.__evaluate(newblock,self.area)

        if deep > 0:
            values = list()
            for i in range(5):
                values.append(self.__search(newblock,mode,deep-1))
            value += np.max(values)
        
        return value    

    def __evaluate(self,block,area):
        # Expert table
        (Nx,Ny) = area.shape
        body = block.getbody()
        value = 0

        # Set area
        miny,maxy = Ny,0
        minx,maxx = Nx,0
        for pos in body:
            area[pos] = block.getshape()
            x,y = pos
            if y > maxy: maxy = y
            if y < miny: miny = y
            if x > maxx: maxx = x
            if x < minx: minx = x

            value += y
        
        # value table
        #for j in range(miny,maxy+1):
        #    if np.sum(area[:,j]) == Nx:
        #        value += 300000
        #
        #    if np.sum(area[:,j]) == Nx-1:
        #        value += 10000
        #
        #    if np.sum(area[:,j]) == Nx-2:
        #        value += 500

        for i in range(minx,maxx+1):
            for j in range(miny,Ny):
                if area[i,j] == 0:
                    if np.sum(area[:,j]) == Nx-1:
                        value += 300000

                    if np.sum(area[:,j]) == Nx-1:
                        value += 10000

                    if np.sum(area[:,j]) == Nx-2:
                        value += 500
                
        # Recover area
        for pos in body:
            area[pos] = 0

        return value


    def play(self,block,area):
        self.area = area.copy()
        self.block = block

        # Choose mode：{0,1,2,3,4}
        values = self.__values()
        mode = np.argmax(values)
        return mode
