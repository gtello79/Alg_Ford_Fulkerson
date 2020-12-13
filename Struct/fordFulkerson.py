from .state import state
import numpy as np 

class fordFulkerson:
    def __init__(self, universalMap = None):
        self.nodesMap = None
        self.capabilityMap = None
        self.totalNodes = None
        self.top = 100
        path = None
        countLines = 0

        #Se lee el dataset por defecto, seria bueno generar numeros aleatorios
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
                self.capabilityMap = np.zeros((self.totalNodes, self.totalNodes), dtype=int)
            else:
                info =  [int(x) for x in line.strip().split()]  
                origin, final, value = info  
                self.nodesMap[origin-1][final-1] = value 
                self.capabilityMap[origin-1][final-1] = self.top
            countLines+=1

    '''
        Inicializacion del algoritmo de búsqueda:
    '''
    def getRoutes(self, init, final):
        #Se almacenaran los caminos
        paths = []
        nextPath = True
        while(nextPath):
            s = self.solve(init, final)
            if(s is None):
                nextPath = False
            else:
                paths.append(s)
                self.updateCapabilityMap(s)
        return paths    

    '''
        Teniendo los estados ya definidos, se desea buscar el camino mejor utilizado para llegar a nodo. capabilityMap es 
        la que permite construir implicitamente el grafo residual
    '''        
    def solve(self, init, final):
        iterCounter = 0
        actual = state([init], self.nodesMap, self.capabilityMap, self.totalNodes) 
        queue_s = []
        queue_s.append(actual)
        while(len(queue_s)> 0):
            s = queue_s.pop(0)
            if(s.isFinalState(final)):
                return s
            
            actions = s.getActions()
            for a in actions:
                state_s = s.transition(a)
                if(state_s.isValidState()):
                    queue_s.append(state_s)

        print("No se encontraron estado solucion")
        return None
        #Actualizar CapabilityMap al encontrar un camino


    '''
        Actualizar Capability Map
    '''
    def updateCapabilityMap(self, lastState):
        path = lastState.node
        acum = 0
        for i in range(0,len(path)-1):
            for j in range(1,len(path)):
                acum += self.nodesMap[i][j]
                self.capabilityMap[i][j] -= acum
                
                if(self.capabilityMap[i][j] < 0):
                    self.capabilityMap[i][j] = 0
        