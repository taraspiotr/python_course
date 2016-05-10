
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


def zadanie1(old):
    newList = [old[0]]
    for e in old:
        if e != newList[-1]:
            newList.append(e)
    return newList

test(zadanie1, [1, 2, 3, 3, 5, 68, 68, 24], [1,2,3,5,68,24])


def zadanie2(list1, list2):
    smallSize = min(len(list1), len(list2))
    if len(list1) > len(list2):
        big = list1
    else:
        big = list2

    newList = list()
    for l,r in zip(list1[:smallSize], list2[:smallSize]):
        newList.append(l)
        newList.append(r)

    for e in big:
        newList.append(e)

    return newList

test(zadanie2, [1, 2, 19, 'dd', ':P', ":("], [12,'c','5'], [1, 12, 2, 'c', 19, '5', 1, 2, 19, 'dd', ':P', ':('])


def zadanie3(tupleList):
    #bubble sort
    for n in range(len(tupleList)-1, 0, -1):
        for i in range(n):
            if tupleList[i][-1] > tupleList[i+1][-1]:
                tmp = tupleList[i]
                tupleList[i] = tupleList[i+1]
                tupleList[i+1] = tmp

    return tupleList

test(zadanie3, [(1, 3), (3, 3, 2), (2, 1)], [(2, 1), (3, 3, 2), (1, 3)])




def zadanie4(text):
    return " ".join([ s.replace("ok","") for s in text.split("$") if s.startswith("ok") ])

test(zadanie4, "okmy$aiaetiaigaafbaf??a$okwatch$oafbusd$okhas$asbrsi31480$okended$aq340af", [109, 121, 32, 119, 97, 116, 99, 104, 32, 104, 97, 115, 32, 101, 110, 100, 101, 100])


#Zadanie 5
from random import randint

while True:
    r = randint(1,9)
    try:
        guess = input("Podaj liczbe od 1-9\n")
        num = int(guess)
        if not 0 < num < 10:
            print "Chose number in 1-9 range"
            continue

        if num == r:
            print "Hurra, you're right, it was "+str(r)
            break
        else:
            print "Sorry, try again"

    except Exception:
        print "You should provide integer number in range 1-9"