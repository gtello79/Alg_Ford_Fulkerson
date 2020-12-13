import numpy as np
from .action import action

class state:
    def __init__(self, onRoad, nodesMap):
        self.nodesMap = nodesMap
        self.node = onRoad
        self.eval = 0
        
    def getActions(self):
        actionList = []
        lastPlace = self.node[-1]
        for i in nodesMap.shape[0]:
            if self.nodesMap[lastPlace][i] != 0:
                destiny = i
                value = self.nodesMap[lastPlace][i]
                nextAction = action(destiny, value)
                actionList.append(nextAction)
            
        return actionList

    def isFinalState(self,final):
        return self.node[-1] == final