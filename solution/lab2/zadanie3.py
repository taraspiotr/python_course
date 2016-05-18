
def reduce(matIn, n_size):
    '''
    Function which reduces the size of matrix. Elements values are
    being calculated as average of neighbours
    :param matIn: bigger input matrix
    :param n_size: new size, has to be smaller
    :return:
    '''

    # Sprawdzamy typ n_size. Jesli jest to tuple lub lista to znaczy
    # ze uzytkownik przekazal 2 wymiary. W przeciwnym wypadku zakladamy
    # ze uzytkownik chce jako wynik uzyskac macierz kwadratowa
    if isinstance(n_size,tuple) or isinstance(n_size, list):
        nx, ny = n_size
    elif isinstance(n_size,int):
        nx = n_size
        ny = nx
    else:
        raise Exception("New size should be tuple/list for nonsqure matrix or integer for squre matrix")

    # Wyznaczamy wymiary macierzy wejsciowej. len(matIn) oznacz liczbe wierszy, a liczba kolumn
    # jest pobrana jako dlugosc pierwszego wiersza
    sx = len(matIn)
    sy = len(matIn[0])

    # Upewniamy sie czy przekazany rozmiar jest na pewno mniejszy od macierzy wejsciowej
    if sx < nx or sy < ny:
        raise Exception("New size should be smaller then origin")

    # Obliczamy wspolczynniki skalowania - ile razy musi sie zmniejszyc rozmiar w 2 kierunkach
    nxs = sx / nx
    nys = sy / nx

    # inicjalizujemy wynikowa macierz zerami
    mat = [[0. for i in range(nx)] for j in range(ny)]


    # rozpoczynamy 2 zaganiezdzone petle po kolejnych indeksach wynikowej macierzy
    for i in range(nx):
        for j in range(ny):
            # wyznaczamy "centralne" indeksy macierzy wyjsciowej ktory maja odpowiadac indeksom i,j po przeskalowaniu
            x = int(i*nxs)
            y = int(j*nys)

            # obliczamy sume ze wszystkich sasiadow wokol elementu x,y macierzy wyjsciowej. Sume obejmuja
            # element centralny i po 2 sasiadow w kazdym z kierunkow
            ids = 1
            s = matIn[x][y]
            for xi in range(-1, 2, 2):
                for yj in range(-1, 2, 2):
                    ii = x+xi
                    jj = y + yj
                    # Jesli element lezy na brzegu to suma musi byc ograniczona
                    if 0 <= ii < sx and 0 <= jj < sy:
                        s += matIn[x+xi][y+yj]
                        ids += 1

            # przypisujemy srednia z sumowanych elementow
            mat[i][j] = s/ids

    #Zwracamy wynik
    return mat


# Test
# m = [[float(i*j) for i in range(5)] for j in range(5)]
#
# print np.array(m)
#
# print np.array(reduce(m, (3, 3)))
