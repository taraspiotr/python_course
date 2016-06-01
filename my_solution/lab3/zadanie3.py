import numpy as np
from zadanie1 import animate_contour_plot
from resources.lab3.kdiagonal import d_id
from numpy.linalg import solve



N = 50

# Definicja numerow wezlow brzegowych w pelnym wektorze rozwiazan T o wymiarze N*N
bcnodes = []
    #dolne wezly
bcnodes.append(range(N))
    #wezly na lewo
bcnodes.append([i*N for i in range(N)])
    #wezly na prawo
# twoj kod ...
bcnodes.append([(i*N + N - 1) for i in range(N)])
    #wezly na scianie gornej
# twoj kod ...
bcnodes.append(range(N*(N-1), N*N))

# Zbierz wszystkie wezly w jeden wektor ( wykorzystaj funkcje reshape)
#bcnodesAll = ... twoj kod ...
bcnodesAll = np.reshape(bcnodes, 4*N)


#Zdefiniuj wartosci rozwiazania dla kazdego z 4 brzegow
# bvals = ....
bvals = np.zeros(4*N)
for i in range(N):
        bvals[i] = 1


#Zbuduj uklad rownan uzupelniajac elementy macierzy K
K = np.zeros((N**2, N**2))

 # Diagonala odnoszaca sie do wezlow T[i,j-1]
# twoj kod ....
for i in range(N, N**2):
        K[i][i-N] = 1
 # Diagonala odnoszaca sie do wezlow T[i-1,j]
# twoj kod ....
for i in range(1, N**2):
        K[i-1][i] = 1
 # Glowna diagonala, wezlu T[i,j]
# twoj kod ....
for i in range(N**2):
        K[i][i] = -4
 # Diagonala odnoszaca sie do wezlow T[i+1,j]
# twoj kod ....
for i in range(N**2-1):
        K[i+1][i] = 1
 # Diagonala odnoszaca sie do wezlow T[i,j+1]
# twoj kod ....
for i in range(N**2-N):
        K[i][i+N] = 1

# Zmodyfikuj rownania w macierzy tak, aby jawnie wprowadzic rozwiazania dla wezlow brzegowych (odwolaj sie do
# indeksow za pomoca tablicy bcnodesAll)
# ... twoj kod ...
for i in bcnodesAll:
        K[i] = 0
        K[i][i] = 1

# Utworz wektor prawych stron rownania
Rhs = np.zeros(N**2)

# Zadaj warunki brzegowe w wektorze prawych stron (skorzystaj z tablic bvals i bcnodes)
# Twoj kod ....
for i in range(4*N):
        Rhs[bcnodesAll[i]] = bvals[i]


# Rozwiaz rownanie
T = np.array( solve(K, Rhs) )

# Rebuild T to 2D array
# your code ....
T = np.reshape(T, (N, N))

# Plot result
animate_contour_plot([T])