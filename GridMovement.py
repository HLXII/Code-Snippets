from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math

"""
Given an infinite grid of points, and a set number of moves, 
what is the probability of landing on any point given random movements
"""


def ncr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

def rec(mat,point,curLen,maxLen):
        if curLen == maxLen:
                mat[point] += 1
                return
        else:
                rec(mat,(point[0],point[1]+1),curLen+1,maxLen)
                rec(mat,(point[0],point[1]-1),curLen+1,maxLen)
                rec(mat,(point[0]+1,point[1]),curLen+1,maxLen)
                rec(mat,(point[0]-1,point[1]),curLen+1,maxLen)
                return

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

#xpos = [1,1.5,3,4,5,6,7,8,9,10]
#ypos = [1,1.5,3,4,5,6,7,8,9,10]
#num_elements = len(xpos)
#zpos = [0,0,0,0,0,0,0,0,0,0]
#dx = [2,2,2,2,2,2,2,2,2,2]
#dy = np.ones(10)
#dz = [1,2,3,4,5,6,7,8,9,1]

order = 7
num_elements = (2*order+1)**2
xpos = []
ypos = []
zpos = np.zeros(num_elements)
dx = 1
dy = 1
dz = []

mat = [[0 for x in range(2*order + 1)] for y in range(2*order + 1)]

for x in range(-order,order+1):
        for y in range(-order,order+1):
                if abs(x)+abs(y) == order:
                        mat[y][x] = ncr(order,abs(x))

for y in range(-order,order+1):
        for x in range(-order,order+1):
                if abs(x)+abs(y) < order and (((abs(x)+abs(y)+order) % 2) == 0):
                        mat[y][x] = mat[y-1][x-1] * mat[y-1][x+1] // mat[y-2][x]

for y in range(-order,order+1):
        for x in range(-order,order+1):
                print(" {:03} ".format(mat[y][x]),end="")
        print()


#for point,value in mat.items():
#        xpos.append(point[0])
#        ypos.append(point[1])
#        dz.append(value/4**order)
#print("Total = {}".format(sum(dz)))

#for y in range(-order,order+1):
#        for x in range(-order,order+1):
#                if (x,y) in mat:
#                        print(" {:03} ".format(mat[(x,y)]),end="")
#                else:
#                        print("  X  ",end="")
#        print()

for x in range(-order,order+1):
        for y in range(-order,order+1):
                xpos.append(x)
                ypos.append(y)
                dz.append(mat[y][x]/(4**order))


ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#00ceaa')
plt.show()

