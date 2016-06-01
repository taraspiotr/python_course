import numpy as np

from zadanie1 import animate_contour_plot
from resources.lab3.kdiagonal import d_id
import time
start_time = time.time()

# Setup
N = 20
dx = 1./(N-1)
NTimeSteps = 1000
a = 1.
dt = 0.05


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


#Build mass matrix
M = np.zeros_like(K)
print M.shape
for i in range(N**2):
    M[i][i] = 1

# Utworz uklad rownan
# EqMatrix = ....
EqMatrix = M - dt*a*K


# Zmodyfikuj rownania w macierzy tak, aby jawnie wprowadzic rozwiazania dla wezlow brzegowych (odwolaj sie do
# indeksow za pomoca tablicy bcnodesAll)
# ... twoj kod ...
for i in bcnodesAll:
        EqMatrix[i] = 0
        EqMatrix[i][i] = 1


# Utworz wektor prawych stron rownania
Rhs = np.zeros(N**2)

# Zadaj warunki brzegowe i poczatkowe w wektorze prawych stron (skorzystaj z tablic bvals i bcnodes)
# Twoj kod ....
for i in range(4*N):
        Rhs[bcnodesAll[i]] = bvals[i]


#Tworzymy zbior rozwiazan
Results = list()

#Dodajemy pierwsze rozwiazanie
Results.append(np.array(Rhs.reshape((N, N))))

# Petla czasowa
for iter in range(NTimeSteps):
    print 'time iteration:',iter+1

    #T = ... rozwiaz rownanie
    T = np.linalg.solve(EqMatrix, Rhs)

    # Zaktualizuj wektor prawych stron
    #Rhs = ....
    Rhs = T

    #Zapisz rozwiazania w liscie, na skonwertuj wyniki z wektora na tablice 2D 
    # T = ... twoj kod ..
    T = np.reshape(T, (N, N))
    Results.append(T)
print("\n--- %s seconds ---" % (time.time() - start_time))



# Wyswietl wyniki:
animate_contour_plot(Results, skip=5, repeat=True)
