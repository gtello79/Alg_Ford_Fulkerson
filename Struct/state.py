import numpy as np
from .action import action

class state:
    def __init__(self, idState):
        self.id = idState
        self.travels = dict()


    def getActions(self):
        moviments = []
        for a in self.travels.keys():
            d = self.travels[a]
            a = action(a,d) 
            moviments.append(a)
            
        return np.array(moviments)


    def addTrack(self, destiny, value):
        if(self.travels.get(destiny) is None or self.travels[destiny] < value ):
            self.travels[destiny] = value
    
    