from .state import state
import numpy as np 

class fordFulkerson:
    def __init__(self, universalMap = None):
       
        self.graphSize = 0
        self.nodesMap = None
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
                
            countLines+=1
            
    def getRoute(self, init, final):
        actual = state(init, nodesMap)
        while(not (actual.isFinalState(final)) ):

