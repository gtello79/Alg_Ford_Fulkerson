import copy as cp

class action:
    def __init__(self, newPoint, value):
        self.actual = newPoint
        self.distance = value
        
    def getState(self, state):
        newState = cp.deepcopy(state)
        newState.node.append(self.actual)
        newState.eval += self.distance
        return newState

    