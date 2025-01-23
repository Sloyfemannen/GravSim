import numpy as np

class Obj:
    def __init__(self, m, x, y):
        self._m = m
        self._coords = np.array([x, y])
        self._v = np.array([0.0, 0.0])
        self._a = np.array([0.0, 0.0])

    def v(self, x, y):
        self._v = np.array([x, y])

    def a(self, x, y):
        self._a = np.array([x, y])

    def ds(self):
        self.dv()
        self._coords += (self._v * self._dt)

    def dv(self):
        self._v += (self._a * self._dt)

    def aF(self, F):
        self._a = F / self._m

    def newpos(self, dt):
        self._dt = dt
        self.ds()