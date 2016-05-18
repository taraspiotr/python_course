import numpy as np

from zadanie1 import animate_contour_plot
from resources.lab3.kdiagonal import d_id

# Setup
N = 20
dx = 1./(N-1)
NTimeSteps = 100
a = 1.
dt = 0.01


# Definicja numerow wezlow brzegowych w pelnym wektorze rozwiazan T o wymiarze N*N
# skopiuj kod z poprzedniego zadania

# Zbierz wszystkie wezly w jeden wektor ( wykorzystaj funkcje reshape)
# skopiuj kod z poprzedniego zadania

#Zdefiniuj wartosci rozwiazania dla kazdego z 4 brzegow
# skopiuj kod z poprzedniego zadania

#Zbuduj uklad rownan uzupelniajac elementy macierzy K
K = np.matrix(np.zeros((N**2, N**2)))
# skopiuj kod z poprzedniego zadania


#Build mass matrix
M = np.matrix(np.zeros_like(K))
# Uzupelnij macierz masowa

# Utworz uklad rownan
# EqMatrix = ....


# Zmodyfikuj rownania w macierzy tak, aby jawnie wprowadzic rozwiazania dla wezlow brzegowych (odwolaj sie do
# indeksow za pomoca tablicy bcnodesAll)
# ... twoj kod ...


# Utworz wektor prawych stron rownania
Rhs = np.zeros(N**2)

# Zadaj warunki brzegowe i poczatkowe w wektorze prawych stron (skorzystaj z tablic bvals i bcnodes)
# Twoj kod ....


#Tworzymy zbior rozwiazan
Results = list()

#Dodajemy pierwsze rozwiazanie
Results.append(np.array(Rhs.reshape((N, N))))

# Petla czasowa
for iter in range(NTimeSteps):
    print 'time iteration:',iter

    #T = ... rozwiaz rownanie

    # Zaktualizuj wektor prawych stron
    #Rhs = ....

    #Zapisz rozwiazania w liscie, na skonwertuj wyniki z wektora na tablice 2D 
    # T = ... twoj kod ..
    Results.append(T)



# Wyswietl wyniki:
animate_contour_plot(Results, skip=5, repeat=True)