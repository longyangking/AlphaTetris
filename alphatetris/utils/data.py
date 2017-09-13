import numpy as np 
import h5py
import time
import datetime

class Data:
    def __init__(self):
        self.areas = list()
        self.steps = 0
        self.score = 0
    
    def add(self,area):
        self.areas.append(area)
        self.steps += 1

    def setscore(self,score)：
        self.score = score

    def load(self,filename):
        with h5py.File(filename,'r') as inputfile:
            self.steps = inputfile['steps'][...]
            self.score = inputfile['score'][...]
            areas = inputfile['areas']
            for i in range(self.steps):
                self.areas = areas['{step}'.format(step=i)][...]

    def save(self,filename=None):
        if filename is None:
            filename = '{date}.h5'.format(date=datetime.datetime.now())
        with h5py.File(filename,'w') as outputfile:
            outputfile.create_dataset('steps',data=self.steps)
            outputfile.create_dataset('score',data=self.score)
            areas = outputfile.create_group('areas')
            for i in range(self.steps):
                areas.create_dataset('{step}'.format(step=i),data=self.areas[i])