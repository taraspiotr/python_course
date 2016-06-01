def test(fun, *args):
    print "".join(['-' for i in range(40)])
    print fun.__name__[:-1].upper()+" "+fun.__name__[-1]
    res = fun(*args[:-1])
    if isinstance(args[0], str):
        decoded = "".join([chr(i) for i in args[-1]])
        if res == decoded:
            print "Yes, "+decoded.replace("my","your")
        else:
            print "No, "+decoded.replace("my","your").replace("has","has not")+" yet"
    else:
        print "Is correct? "+ str(res == args[-1])
    print "".join(['-' for i in range(40)])


def zadanie1(listObject):
    temp = []
    temp.append(listObject[0])
    for item in listObject:
        if not item == temp[-1]:
            temp.append(item)
    return temp

#test(zadanie1, [1, 2, 3, 3, 5, 68, 68, 24], [1,2,3,5,68,24])

def zadanie2(list1, list2):
    temp = []
    a, b = len(list1), len(list2)
    counter = 0
    while(counter < a or counter < b):
        if(counter < a):
            temp.append(list1[counter])
        if(counter < b):
            temp.append(list2[counter])
        counter += 1
    return temp



#test(zadanie2, [1, 2, 19, 'dd', ':P', ":("], [12,'c','5'], [1, 12, 2, 'c', 19, '5', 'dd', ':P', ':('])



def zadanie3(listTuples):
    return sorted(listTuples, key=lambda x: x[-1])

#test(zadanie3, [(1, 3), (3, 3, 2), (2, 1)], [(2, 1), (3, 3, 2), (1, 3)])





def zadanie4(text):
    nowy = ""
    indeks = 0
    koniec = False
    while indeks < len(text):
        indeks +=2
        while not text[indeks] == "$":
            nowy += text[indeks]
            indeks += 1
        indeks += 1
        while not text[indeks] == "$":
            indeks +=1
            if indeks >= len(text):
                koniec = True
                break
        indeks += 1
        if not koniec == True:
            nowy += " "
    return nowy





bla = "okmy$aiaetiaigaafbaf??a$okwatch$oafbusd$okhas$asbrsi31480$okended$aq340af"
zadanie4(bla)

#test(zadanie4, "okmy$aiaetiaigaafbaf??a$okwatch$oafbusd$okhas$asbrsi31480$okended$aq340af", [109, 121, 32, 119, 97, 116, 99, 104, 32, 104, 97, 115, 32, 101, 110, 100, 101, 100])







from random import *

def losowanie():
    wczytana, losowa = 0,1
    while not wczytana == losowa:
        losowa = randint(1, 9)
        wczytana = input("podaj liczbe: ")
        print "losowa:", losowa
        if wczytana == losowa:
            print wczytana, "=", losowa
        else:
            print wczytana, "!=", losowa
    print "Braaaaaawo!!!!!!!!!!!!!!"

losowanie()