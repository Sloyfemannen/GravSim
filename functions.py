import numpy as np
from math import sin, cos, radians

G = 6.6743 * 10**(-11)

def gFrc(m1, m2, r):
    F = G * m1 * m2 / np.linalg.norm(r)**2
    return np.array([F*r[i]/np.linalg.norm(r) for i in range(len(r))])

def v(mag, ang, raddeg):
    if raddeg == 'r' or raddeg == 'rad':
        return np.array([mag*cos(ang), mag*sin(ang)])
    elif raddeg == 'd' or raddeg == 'deg':
        radians(ang)
        return np.array([mag*cos(ang), mag*sin(ang)])
    else:
        raise TypeError("Your degree type must be of type r (rad) or d (deg)")
