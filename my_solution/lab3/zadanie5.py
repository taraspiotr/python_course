import numpy as np
from zadanie1 import animate_contour_plot
from scipy import sparse
from scipy.sparse.linalg.isolve.iterative import bicgstab
from scipy.sparse.linalg.isolve.iterative import cg
import time
start_time = time.time()

# Select linear solver by adding new name for function
solve = cg  # conjugate gradient solver
# solve = bicgstab #bi-conjugate gradient stabilized solver

# Setup
size = (1., 1.)
N = 50
a = 1
u = np.array([-0.1, 0.])
dx = size[0] / (N - 1)
dy = size[1] / (N - 1)

NTimeSteps = 2000


dt = 1e-1  # 0.5*(dx**2)/a #<-- stability requirement for time step

N = 20
dx = 1./(N-1)
NTimeSteps = 10000
a = 1.
dt = 0.05

# Definicja numerow wezlow brzegowych w pelnym wektorze rozwiazan T o wymiarze N*N
bcnodes = []
# dolne wezly
bcnodes.append(range(N))
# wezly na lewo
bcnodes.append([i * N for i in range(N)])
# wezly na prawo
# twoj kod ...
bcnodes.append([(i * N + N - 1) for i in range(N)])
# wezly na scianie gornej
# twoj kod ...
bcnodes.append(range(N * (N - 1), N * N))

# Zbierz wszystkie wezly w jeden wektor ( wykorzystaj funkcje reshape)
# bcnodesAll = ... twoj kod ...
bcnodesAll = np.reshape(bcnodes, 4 * N)

# Zdefiniuj wartosci rozwiazania dla kazdego z 4 brzegow
# bvals = ....
bvals = np.zeros(4 * N)
for i in range(N):
        bvals[i] = 1

# Skonstruuj macierz ukladu rownan wykorzystujac format macierzy rzadkich
rowCols = []  # holds indices for non-zero columns in ith row
rowStarts = [0]  # information where starts next row definition, eg. number of columns in i-th row would be rowStarts[i+1] - rowStarts[i]
data = []  # stores values for each non-zeoro coefficient in rows. Its size is the same as rowCols
# Twoj kod ....
val1 = 1 + a * dt * 4
val2 = -a * dt

for rowNumber in range(N ** 2):
        # if rowNumber < N:
        #     rowCols.append(rowNumber)
        #     rowCols.append(rowNumber+N)
        #     rowStarts.append(rowStarts[-1] + 2)
        #     data.append(1 + a * dt * 4)
        #     data.append(-a * dt)
        # elif N <= rowNumber < N**2-N:
        #     rowCols.append(rowNumber-N)
        #     rowCols.append(rowNumber)
        #     rowCols.append(rowNumber + N)
        #     rowStarts.append(rowStarts[-1] + 3)
        #     data.append(-a*dt)
        #     data.append(1 + a * dt * 4)
        #     data.append(-a * dt)
        # else:
        #     rowCols.append(rowNumber - N)
        #     rowCols.append(rowNumber)
        #     rowStarts.append(rowStarts[-1] + 2)
        #     data.append(-a*dt)
        #     data.append(1 + a * dt * 4)
        if rowNumber not in bcnodesAll:
                counter = 0
                if rowNumber - N > 0:
                        rowCols.append(rowNumber - N)
                        data.append(val2)
                        counter += 1
                if rowNumber - 1 > 0:
                        rowCols.append(rowNumber - 1)
                        data.append(val2)
                        counter += 1
                rowCols.append(rowNumber)
                data.append(val1)
                counter += 1
                if rowNumber + 1 < N ** 2:
                        rowCols.append(rowNumber + 1)
                        data.append(val2)
                        counter += 1
                if rowNumber + N < N ** 2:
                        rowCols.append(rowNumber + N)
                        data.append(val2)
                        counter += 1
                rowStarts.append(rowStarts[-1] + counter)
        else:
                rowCols.append(rowNumber)
                data.append(1)
                rowStarts.append(rowStarts[-1] + 1)

# print len(rowStarts)
# print len(rowCols)
# print len(data)
# print rowStarts

# Create sparse matrix - CSR - Compressed Sparse Row Matrix
EqMat = sparse.csr_matrix((data, rowCols, rowStarts), shape=(N ** 2, N ** 2), dtype=float)
# print EqMat.toarray()

# Create and fill Rhs vector - vector holding dirichelet bc values and initital conditions
Rhs = np.zeros(N * N)

# Zadaj warunki brzegowe i poczatkowe w wektorze prawych stron (skorzystaj z tablic bvals i bcnodes)
# Twoj kod ....
for i in range(4 * N):
        Rhs[bcnodesAll[i]] = bvals[i]

# Time loop
Results = list()
Results.append(np.array(Rhs.reshape((N, N))))

for iter in range(NTimeSteps):
        print 'time iteration:', iter + 1

        sol = solve(EqMat, Rhs)

        if sol[1] != 0:
                print "solution is not converged"

        T = np.array(sol[0])

        # Zaktualizuj wektor prawych stron
        Rhs = T

        # Zapisz rozwiazania w liscie, na skonwertuj wyniki z wektora na tablice 2D
        # T = ... twoj kod ..
        T = np.reshape(T, (N, N))
        Results.append(T)

print("\n--- %s seconds ---" % (time.time() - start_time))

# Animate results:
animate_contour_plot(Results, skip=20, repeat=True)
