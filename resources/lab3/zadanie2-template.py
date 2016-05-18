import numpy as np
from zadanie1 import animate_contour_plot

N = 50 #liczba wezlow w kierunku x i y
delta = 1./(N-1) #wielkosc oczka siatki
a = 1. #dyfuzyjnosc
dt = 0.1 # krok czasowy
endTime = 1.

# Tablica do przechowywania rozwiazan (2D, kazdy wezel to element)
T = np.zeros((N,N),dtype=float)

# Ustaw wartosci rozwiazan dla wezlow na dolenej krawedzi na 1 - warunek brzegowy
#twoj kod ...


# Lista do przechowyania wynikow z kolejnych krokow czasowych
Results = []

# Utworz tablice zawierajca czasy kolejnych krokow czasowych
#time = twoj kod ...

#time loop
for t in time:

    print "calculating time :",t

    T0 = np.copy(T)

    #Zaimplementuj funkcje obliczajaca jeden krok czasowy zgodnie z poniższym wzorem:
    # (T - T0)/dt -a*laplacian(T0)=0
    # T = T0 + a*dt*laplacian(T0)
    # T = T0 + (a*dt/dx**2)*(T0(i,j+1) + T0(i+1,j) - 4*T0(i,j) + T0(i-1,j) + T0(i,j-1) )
    # Pamietaj, ze na brzegach jest zadany waruenek typu Dirichleta, zatem w tych wezlach
    # wartosci nie powinny sie zmieniac

    # Twoj kod ....

    Results.append(np.copy(T))


# Animate results:
# Wywolaj funkcje z zadania 1, tak aby wyswietlic animacje rozkladu temperatury
