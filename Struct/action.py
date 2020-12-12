import copy as cp

class action:
    def __init__(self, state, value):
        self.actual = state
        self.distance = value
        