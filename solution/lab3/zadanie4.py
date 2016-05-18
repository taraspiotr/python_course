import numpy as np

from zadanie1 import animate_contour_plot
from resources.lab3.kdiagonal import d_id

# Setup
N = 20
dx = 1./(N-1)
NTimeSteps = 100
a = 1.
dt = 0.01


#Define boundary nodes
bcnodes = []
bcnodes.append(range(N)) #bottom nodes
bcnodes.append([i*N for i in range(N)]) #left nodes
bcnodes.append([(i+1)*N-1 for i in range(N)]) #right nodes
bcnodes.append([(N-1)*N + i for i in range(N)]) #top nodes
bcnodesAll = np.array(bcnodes)
bcnodesAll.reshape(bcnodesAll.size)

#Define dirichlet bounadry conditions values on each boundary
bvals = [1., 0., 0., 0.]


#Build stiffness matrix:
K = np.matrix(np.zeros((N**2, N**2)))

 # left far diagonal
K[d_id(K, -N)] = 1
 # left closer diagonal
K[d_id(K, -1)] = 1
 # main diagonal
K[d_id(K, 0)] = -4
 # right closer diagonal
K[d_id(K, 1)] = 1
 # right far diagonal
K[d_id(K, N)] = 1

#Build mass matrix
M = np.matrix(np.zeros_like(K))
np.fill_diagonal(M, 1)

EqMatrix = M - a*dt/(dx **2)*K


#Apply boundary conditions to matrix:
EqMatrix[bcnodesAll,:] = 0
EqMatrix[bcnodesAll, bcnodesAll] = 1


# Fill rhs vector
 #Fill with initial conditions
Rhs = np.matrix(np.zeros((N**2, 1)))

 #apply values from boundary conditions
for bcn, val in zip(bcnodes, bvals):
    Rhs[bcn] = val


# Time loop
Results = list()
Results.append(np.array(Rhs.reshape((N, N))))
for iter in range(NTimeSteps):
    print 'time iteration:',iter
    T = np.array(np.linalg.solve(EqMatrix, Rhs))
    # do not need to applay boundary conditions to Rhs, because
    # solution in T for boundary nodes is the same throughout the time.
    Rhs = T
    T = T.reshape((N, N))
    Results.append(T)

# Animate results:
animate_contour_plot(Results, skip=5, repeat=True)