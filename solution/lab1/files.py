# Generate files
# import tempfile, os
#
# path = "../../resources/lab1/files"
# step = 10
# suff = 1
# for i in range(50):
#     name = tempfile.NamedTemporaryFile().name.split("/")[-1]
#     with open(path+os.sep+name, "a") as f:
#         f.write("location: dir"+str(suff))
#
#     if i+1 > suff*step:
#         suff += 1




# Ładujemy potrzebne biblioteki
#   os - do operacji systemowych, takich jak listowanie katalogów, tworzenie folderów
#   shutil - biblioteka do tworzenia kopii, archiwów oraz pełnych drzew katalogów
# Import można wykonać także w jednej linijce: import os, shutil
import os
import shutil

# Definiujemy zmienna do przechowywania scieżki do folderu zawierajacego pliki
source = "../../resources/lab1/files"

# Tworzymy petle po wszystkich katalogach. os.listdir zwraca tablice katalogow w danej lokalizacji
for f in os.listdir(source):
    # Otwieramy plik. os.sep jest to zmienna globalna przechowujaca znak okreslajacy rozdzielenie folderow w sciezkach
    # w zależnosci od systemu na jakim jest uruchomiony kod(linux: /, windows: \)
    with open(source+os.sep+f, "r") as rf:
        # Wyciagamy nazwe katalogu w ktorym powinny byc umieszczone pliki.
        #   metoda replace w klasie string zamienia znaki ze spacjji na pusty znak i zwraca nowy string
        #   metoda split w klasie string zwraca tablice stringow wynikajaca z podzialu stringa za pomoca :
        dirname = rf.read().replace(' ', '').split(':')[1]

    # sprawadzamy czy folder o podanej nazwie istnieje. Jeśli nie to go tworzymy.
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    # Kopiujemy plik z poczatkowego katalogu do wskazanego przez teks znajdujacy sie pliku
    shutil.copyfile(source+os.sep+f, dirname+os.sep+f)
