##list:
# aList = ['a', 2, 3, 'b']
#
# aList.append(12)

#loops, generate data
# for a in aList:
#     print a

# geneartion of data
# aList = []
# for i in range(10):
#     aList.append(i**2)

# new way
# aList = [i**2 for i in range(10)]



## slice
# print aList[:2]

## reverse access
# nl = aList[-1:0:-1]
# print nl

##unpacking
# x1, x2, x3, x4, x5 = aList

## Comparing objects
# b = aList
#
# if b is aList:
#     print "the same object"


# Remove duplicated elements
def remove_adjacent_duplication(listObject):
    # your code
    pass

#print remove_adjacent_duplication([1, 2, 3, 3, 5, 68, 68, 24])

# Mereg 2 lists
def merge_lists(list1, list2):
    # your code
    pass

#print merge_lists([1,2,45,19,2],[12,-12,'c',3,'5'])

# tuple
# c = (2, 3, 'cos')
# print c

## Order list of tuples by last element
# def order_tuples(listTuples):
#     # your code
#     pass
#
# print "is order ok?"+ str( order_tuples([(1, 3), (3, 2), (2, 1)]) == [(2, 1), (3, 2), (1, 3)])


# Guess number
# import random
# while True:
#     num = random.randint(1,9)
#     guess = input("Guess number from 1-9\n")
#     if num == guess:
#         print "Hurra, it's right"
#         break
#     else:
#         print "Bad lack, you should chose "+str(num)+", try again"




