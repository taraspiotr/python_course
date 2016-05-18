import os
import shutil

katalog = os.path.join("/home", 'piotr', "PycharmProjects", "python_course", "resources", "lab2", "files")

for entry in os.listdir(katalog):
    sciezka = os.path.join(katalog, entry)
    if os.path.isfile(sciezka):
        plik = open(sciezka, "r")
        lokalizacja = os.path.join(katalog, plik.readline().split()[1])
        if not os.path.exists(lokalizacja):
            os.mkdir(lokalizacja)
        plik.close()
        sciezkaNowa = os.path.join(lokalizacja, entry)
        shutil.copy(sciezka, sciezkaNowa)