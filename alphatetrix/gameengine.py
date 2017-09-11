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

        self.resourcevalid = False
        self.resourcepos = None

        self.area = np.zeros((Nx,Ny))
        self.validplaces = list(range(self.Nx*self.Ny))
    
    def getarea(self):
        return self.area
    
    def getscore(self):
        return self.score
        
    def __pos2place(self,pos):
        place = self.Nx*pos[1] + pos[0]
        return place

    def __place2pos(self,place):
        pos = (place%self.Nx,int(place/self.Nx))
        return pos

    def initsnake(self,snakelength,velocity):
        # Initiate the retro snake
        x = np.random.randint(self.Nx)
        y = np.random.randint(self.Ny)
        head = (x,y) 

        choice = np.random.randint(4)
        direction = (1,0)
        if choice == 0:
            direction = (1,0)
        elif choice == 1:
            direction = (-1,0)
        elif choice == 2:
            direction = (0,1)
        else:
            direction = (0,-1)

        body = list()
        body.append(head)
        for i in range(snakelength-1):
            x = (x - direction[0])%self.Nx
            y = (y - direction[1])%self.Ny
            body.append((x,y))

        # Update Area Information
        for pos in body:
            self.area[pos] = 1
            self.validplaces.remove(self.__pos2place(pos))  #not valid place anymore

        self.snake = snake.snake(head=head,body=body,direction=direction,
                velocity=velocity,player=self.player)

    def start(self,snakelength=3,velocity=1):
        self.area = np.zeros((self.Nx,self.Ny))
        self.resourcevalid = False
        self.validplaces = list(range(self.Nx*self.Ny))
        self.initsnake(snakelength=snakelength,velocity=velocity)
        
        return True

    def restart(self,snakelength=3,velocity=1):
        return self.start(snakelength=snakelength,velocity=velocity)

    def setresource(self):
        choice = np.random.randint(len(self.validplaces))
        place = self.validplaces[choice]
        pos = self.__place2pos(place)

        self.resourcepos = pos
        self.area[pos] = -1
        self.validplaces.remove(place)

        self.resourcevalid = True

    def updatearea(self):
        body = self.snake.getbody()
        head = self.snake.gethead()

        if self.area[head] == -1:
            self.score += 1
            self.snake.growup()
            self.resourcevalid = False

        # update area and valid places
        self.validplaces = list(range(self.Nx*self.Ny))
        self.area = np.zeros((self.Nx,self.Ny))
        for pos in body:
            self.area[pos] = 1
            place = self.__pos2place(pos)
            if place in self.validplaces:
                self.validplaces.remove(place)

        if self.resourcevalid:
            self.area[self.resourcepos] = -1

    def update(self):
        if not self.resourcevalid:
            self.setresource()

        starttime = time.time()
        self.snake.update(self.area)
        endtime = time.time()
        time.sleep(self.timeperiod-(endtime-starttime))

        self.updatearea()   # Update Area

        return self.snake.survive()