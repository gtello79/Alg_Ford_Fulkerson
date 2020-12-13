from .state import state
import numpy as np 

class fordFulkerson:
    def __init__(self, universalMap = None):
       
        self.graphSize = 0
        self.nodesMap = None
        self.capabilityMap = None
        self.totalNodes = None
        self.top = 500
        path = None
        countLines = 0
        
        if(universalMap is None):
            path = 'Dataset/instance1.txt' 
        else:
            path = universalMap
        
        #Se almacenan los nodos con sus destinos
        instanceFile = open(path,'r')
        for line in instanceFile.readlines():
            if(countLines == 0):
                info = line.strip().split()
                size = info[1].split("x")
                self.totalNodes = int(size[0])
                self.nodesMap = np.zeros((self.totalNodes, self.totalNodes), dtype=int)
            else:
                info =  [int(x) for x in line.strip().split()]  
                origin , final, value = info  
                self.nodesMap[origin-1][final-1] = value 
                self.nodesMap[origin-1][final-1] = self.top
            countLines+=1

    '''
        Teniendo los estados ya definidos, se desea buscar el camino mejor utilizado para llegar a nodo. CapabilityMap es 
        la que permite construir implicitamente el grafo residual
    '''        

    def bestFirst(self, init, final):
        actual = state(init, nodesMap)
        queue_s = []
        queue_s.append(actual)
        while(len(queue_s)> 0):
            s = queue_s.pop(0)
            if(visited(s)): 
                continue
            s.visited = True
            actions = s.getActions()
            for a in actions:
                newStep = a.getState(s)
                
        #Actualizar CapabilityMap al encontrar un camino
