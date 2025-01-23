from space_object import Obj
from functions import *
import matplotlib.pyplot as plt
from math import sqrt

earthx = 37250000.0
earthy = 37250000.0

earthdis = 149000000000

earthdisx = sqrt(2)**-1 * earthdis
earthdisy = sqrt(2)**-1 * earthdis


earthm = 5.9721* 10**24
sunm = 1.989* 10**30

earth = Obj(earthm, float(earthdisx), float(earthdisy))
sun = Obj(sunm, float(0), float(0))
dt = 1000.0

objs = [earth, sun]

maxdim = 149000000000
newdim = 50000000
dim = maxdim
plt.xlim(-dim, dim)
plt.ylim(-dim, dim)


angv = 29780
earth.v(float(0), float(angv))
#earth.v = np.array([7446.2, -7446.2])

earthcoords = []
suncoords = []

for i in range(30557):
    dis1 = earth._coords - sun._coords
    dis2 = sun._coords - earth._coords
    F1 = gFrc(earth._m, sun._m, dis1)
    F2 = gFrc(earth._m, sun._m, dis2)
    earth.aF(F2), sun.aF(F1)
    earth.newpos(dt)
    sun.newpos(dt)
    print("Velocity: ", earth._v)
    print("Force: ", F2)
    print("Coords: ", earth._coords)
    print("Acceleration", F2/earthm)
    print()
    earthcoords.append(earth._coords.tolist())
    suncoords.append(sun._coords)

for i in range(0, len(earthcoords), 100):
    plt.scatter(earthcoords[i][0], earthcoords[i][1])
    plt.scatter(suncoords[i][0], suncoords[i][1])
    plt.plot()
plt.show()
