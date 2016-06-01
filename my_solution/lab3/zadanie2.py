import numpy as np
from zadanie1 import animate_contour_plot

N = 50 #liczba wezlow w kierunku x i y
delta = 1./(N-1) #wielkosc oczka siatki
a = 1. #dyfuzyjnosc
dt = 0.1*(delta**2)/a # krok czasowy
endTime = 1.

# Tablica do przechowywania rozwiazan (2D, kazdy wezel to element)
T = np.ones((N,N),dtype=float)

# Ustaw wartosci rozwiazan dla wezlow na dolenej krawedzi na 1 - warunek brzegowy
#twoj kod ...

T[:,0] = 0


# Lista do przechowyania wynikow z kolejnych krokow czasowych
Results = []

# Utworz tablice zawierajca czasy kolejnych krokow czasowych
time = np.linspace(0, endTime, int(endTime/dt + 1))

T0 = np.copy(T)
#time loop
c = (a*dt/delta**2)
for t in time:

    print "calculating time :",t


    # (T - T0)/dt -a*laplacian(T0)=0
    # T = T0 + a*dt*laplacian(T0)
    # T = T0 + (a*dt/dx**2)*(T0(i,j+1) + T0(i+1,j) - 4*T0(i,j) + T0(i-1,j) + T0(i,j-1) )
    # Pamietaj, ze na brzegach jest zadany waruenek typu Dirichleta, zatem w tych wezlach
    # wartosci nie powinny sie zmieniac

    # Twoj kod ....

    # for j in range(1,N-1):
    #     for i in range(1,N-1):
    #         T[i][j] = T0[i][j] + (a*dt/delta**2)*(T0[i][j+1] + T0[i+1][j] - 4*T0[i][j] + T0[i-1][j] + T0[i][j-1])

    backward = range(0,N-2)
    forward = range(2,N)

    T[1:-1,1:-1] = T0[1:-1,1:-1] + c*(T0[backward,1:-1] + T0[1:-1,backward] - 4*T0[1:-1,1:-1] + T0[1:-1,forward] + T0[forward,1:-1])

    T0 = np.copy(T)
    Results.append(T0)


# Animate results:
# Wywolaj funkcje z zadania 1, tak aby wyswietlic animacje rozkladu temperatury


animate_contour_plot(Results, skip=20, nLevels= 20)