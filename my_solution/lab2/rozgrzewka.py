
a = "xdxd"
b = 5

def typ(a):
    print a, type(a)

a = [1, 2, "sdf"]

print type(a)



a = [i**2 for i in range(10)]

print a
print a[-1::-1]
print ""

a = [1, 3, 3, 4, 2, 1, 10, 11, 0, 0, 0]

def remove_duplication(listObject):
    tmp = []
    for i in listObject:
        if i not in tmp:
            tmp.append(i)
    print listObject
    listObject = tmp
    print listObject

remove_duplication(a)

def remove_adjacent_duplication(listObject):
    tmp = []
    tmp.append(listObject[0])
    for i in listObject:
        if i != tmp[-1]:
            tmp.append(i)
    print tmp

remove_adjacent_duplication(a)

print ""

from random import *

def losowanie():
    wczytana, losowa = 0,1
    while not wczytana == losowa:
        wczytana = input("podaj liczbe: ")
        losowa = randint(1, 9)
        print losowa
    print "Braaaaaawo!!!!!!!!!!!!!!"

losowanie()