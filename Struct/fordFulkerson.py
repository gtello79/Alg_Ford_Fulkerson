from .state import state
import numpy as np 

class fordFulkerson:
    def __init__(self, universalMap = None):
        self.nodes = np.array([])
        path = None
        self.node = 0
        
        if(universalMap is None):
            path = 'Dataset/instance1.txt' 
        else:
            path = universalMap
        
        instanceFile = open(path,'r')
        for line in instanceFile.readlines():
            info =  [int(x) for x in line.strip().split()]  
            origin, final, value = info  
            node = state(origin)
            
            if(self.getNode(origin) is None):
                self.nodes = np.append(self.nodes,[node],axis=0)
            else:
                for n in self.nodes:
                    if n.id == origin:
                        n.addTrack(final,value)
    

    def getNode(self, idNode):
        for n in self.nodes:
            if n.id == idNode:
                return n 
        return None


    def getRoute(self,init,final):
        x = 0
    