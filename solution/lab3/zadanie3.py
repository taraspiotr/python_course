import numpy as np
from zadanie1 import animate_contour_plot

from numpy.linalg import solve


from resources.lab3.kdiagonal import d_id

N = 50

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


#Apply boundary conditions to matrix:
K[bcnodesAll,:] = 0
K[bcnodesAll, bcnodesAll] = 1


# Fill rhs vector - apply value to lower boundary
Rhs = np.zeros(N**2)

 #apply values from boundary conditions
for bcn, val in zip(bcnodes, bvals):
    Rhs[bcn] = val


# Solve equation
T = np.array( solve(K, Rhs) )

# Rebuild T to 2D array
T = T.reshape((N, N))

# Plot result
animate_contour_plot([T])