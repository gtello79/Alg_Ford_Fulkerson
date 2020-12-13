import numpy as np
import copy as cp
from .action import action

class state:
    def __init__(self, onRoad, nodesMap, capabilyMap):
        self.nodesMap = nodesMap
        self.node = onRoad
        self.capMap = capabilyMap
        self.eval = 0
        self.visited = False
    
    '''
        Obtiene las rutas posibles a llegar desde el estado actual
    '''
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

    '''
        Aplica una transicion, es decir, se mueve a otro punto adyacente del grafo
    '''

    def transition(self, action):
        s = cp.deepcopy(self)
        s.append(action.newPoint)
        s.eval += action.distance
        return s

    '''
        Verifica que el movimiento no supere a la capacidad permitida en el par de nodos (flujo maximo)
    '''
    def isValidState(self):
        xf = self.node[-1]
        xi = self.node[-2]
        maxFluj = self.capMap[xi][xf]
        return eval < maxFluj

    '''
        Evalua el estado según el record de puntos visitados por el estado (flujo acumulado)
    '''    
    def evaluateState(self):
        val = 0
        for i in range(0, len(self.node)-1):
            for j in range(1, len(self.node)):
                val += self.nodesMap[i][j]
        self.eval = val 
        return val
    
    '''
        Verificacion de si se llegó al punto final deseado
    '''
    def isFinalState(self,final):
        return self.node[-1] == final