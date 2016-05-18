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
    #wezly na scianie gornej
# twoj kod ...

# Zbierz wszystkie wezly w jeden wektor ( wykorzystaj funkcje reshape)
#bcnodesAll = ... twoj kod ...


#Zdefiniuj wartosci rozwiazania dla kazdego z 4 brzegow
# bvals = ....


#Zbuduj uklad rownan uzupelniajac elementy macierzy K
K = np.matrix(np.zeros((N**2, N**2)))

 # Diagonala odnoszaca sie do wezlow T[i,j-1]
# twoj kod ....
 # Diagonala odnoszaca sie do wezlow T[i-1,j]
# twoj kod ....
 # Glowna diagonala, wezlu T[i,j]
# twoj kod ....
 # Diagonala odnoszaca sie do wezlow T[i+1,j]
# twoj kod ....
 # Diagonala odnoszaca sie do wezlow T[i,j+1]
# twoj kod ....


# Zmodyfikuj rownania w macierzy tak, aby jawnie wprowadzic rozwiazania dla wezlow brzegowych (odwolaj sie do
# indeksow za pomoca tablicy bcnodesAll)
# ... twoj kod ...


# Utworz wektor prawych stron rownania
Rhs = np.zeros(N**2)

# Zadaj warunki brzegowe w wektorze prawych stron (skorzystaj z tablic bvals i bcnodes)
# Twoj kod ....


# Rozwiaz rownanie
T = np.array( solve(K, Rhs) )

# Rebuild T to 2D array
# your code ....

# Plot result
animate_contour_plot([T])