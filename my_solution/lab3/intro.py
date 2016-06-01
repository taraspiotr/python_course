def mojgenerator(start, koniec):
        aktualna = start-1

        while aktualna < koniec -1:
                aktualna += 1
                yield aktualna


for liczba in mojgenerator(0,5):
        print liczba



