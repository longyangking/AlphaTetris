import numpy as np 

# Seven basic shape
I,J,L,O,S,T,Z = 1,2,3,4,5,6,7

class Block:
    def __init__(self,position,player,shape=None):
        self.position = position
        self.player = player

        if shape is None:
            self.shape = np.random.randint(1,8)
        else:
            self.shape = shape

        self.body = None
        x,y = position

        if self.shape == I:
            self.body = list([
                (x,y),
                (x+1,y),
                (x+2,y),
                (x+3,y)
            ])
        elif self.shape == J:
            self.body = list([
                (x,y),
                (x+1,y),
                (x+2,y),
                (x+2,y+1)
            ])
        elif self.shape == L:
            self.body = list([
                (x,y),
                (x+1,y),
                (x+2,y),
                (x,y+1)
            ])
        elif self.shape == O:
            self.body = list([
                (x,y),
                (x+1,y),
                (x,y+1),
                (x+1,y+1)
            ])
        elif self.shape == S:
            self.body = list([
                (x+1,y),
                (x+2,y),
                (x,y+1),
                (x+1,y+1)
            ])
        elif self.shape == T:
            self.body = list([
                (x,y),
                (x+1,y),
                (x+2,y),
                (x+1,y+1)
            ])
        elif self.shape == Z:
            self.body = list([
                (x,y),
                (x+1,y),
                (x+1,y+1),
                (x+2,y+1)
            ])

        self.direction = (0,1)

    def __move(self,direction,area):
        (Nx,Ny) = area.shape
        dx,dy = direction

        # Check body
        flag = True
        for pos in self.body:
            x,y = pos
            if (0>x+dx) or (x+dx>=Nx) or (0>y+dy) or (y+dy>=Ny):
                flag = False
                break
            if area[x+dx,y+dy] != 0:
                flag = False
                break

        if flag:
            for i in range(len(self.body)):
                x,y = self.body[i]
                self.body[i] = (x+dx,y+dy)
            x,y = self.position
            self.position = (x+dx,y+dy)

    def __rotate(self,area):
        (Nx,Ny) = area.shape
        #x0,y0 = self.position
        x0,y0 = self.body[1]

        # TODO specification for every shape
        if True:
            # Check body
            flag = True
            for pos in self.body:
                x,y = pos
                x,y = x0 - (y-y0), y0 + (x-x0)
                if (0>x) or (x>=Nx) or (0>y) or (y>=Ny):
                    flag = False
                    break
                if area[x,y] != 0:
                    flag = False
                    break

            if flag:
                for i in range(len(self.body)):
                    x,y = self.body[i]
                    x,y = x0-(y-y0), y0+(x-x0)
                    self.body[i] = (x,y)
        

    def getbody(self):
        return self.body

    def getshape(self):
        return self.shape

    def survive(self,area):
        (Nx,Ny) = area.shape
        for pos in self.body:
            x,y = pos
            if (y+1 >= Ny):
                return False
            if area[x,y+1] != 0:
                return False
            
        return True

    def update(self,area):
        mode = self.player.play(
            position=self.position,
            shape=self.shape,
            area=area)

        if mode == 1:
            self.__move(direction=(-1,0),area=area)
        elif mode == 2:
            self.__move(direction=(1,0),area=area)
        elif mode == 3:
            self.__rotate(area=area) 

        self.__move(direction=(0,1),area=area)   
        if mode == 4:
            self.__move(direction=(0,1),area=area)