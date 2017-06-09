#!/bin/python3
import sys
from itertools import product
import time
primeList = [2,3,5,7,11,13,17,19,23,29,31,37,41,43]

primeSet = [(1, 1, 1), (1, 1, 3), (1, 1, 5), (1, 1, 9), (1, 1, 0), (1, 2, 2), (1, 2, 4), (1, 2, 8), (1, 2, 0), (1, 3, 1), (1, 3, 3), (1, 3, 7), (1, 3, 9), (1, 4, 2), (1, 4, 6), (1, 4, 8), (1, 4, 0), (1, 5, 1), (1, 5, 5), (1, 5, 7), (1, 6, 4), (1, 6, 6), (1, 6, 0), (1, 7, 3), (1, 7, 5), (1, 7, 9), (1, 8, 2), (1, 8, 4), (1, 8, 8), (1, 9, 1), (1, 9, 3), (1, 9, 7), (1, 9, 9), (1, 0, 1), (1, 0, 2), (1, 0, 4), (1, 0, 6), (2, 1, 2), (2, 1, 4), (2, 1, 8), (2, 1, 0), (2, 2, 1), (2, 2, 3), (2, 2, 7), (2, 2, 9), (2, 3, 2), (2, 3, 6), (2, 3, 8), (2, 3, 0), (2, 4, 1), (2, 4, 5), (2, 4, 7), (2, 5, 4), (2, 5, 6), (2, 5, 0), (2, 6, 3), (2, 6, 5), (2, 6, 9), (2, 7, 2), (2, 7, 4), (2, 7, 8), (2, 8, 1), (2, 8, 3), (2, 8, 7), (2, 8, 9), (2, 9, 2), (2, 9, 6), (2, 9, 8), (2, 9, 0), (2, 0, 1), (2, 0, 3), (2, 0, 5), (2, 0, 9), (2, 0, 0), (3, 1, 1), (3, 1, 3), (3, 1, 7), (3, 1, 9), (3, 2, 2), (3, 2, 6), (3, 2, 8), (3, 2, 0), (3, 3, 1), (3, 3, 5), (3, 3, 7), (3, 4, 4), (3, 4, 6), (3, 4, 0), (3, 5, 3), (3, 5, 5), (3, 5, 9), (3, 6, 2), (3, 6, 4), (3, 6, 8), (3, 7, 1), (3, 7, 3), (3, 7, 7), (3, 7, 9), (3, 8, 2), (3, 8, 6), (3, 8, 8), (3, 8, 0), (3, 9, 1), (3, 9, 5), (3, 9, 7), (3, 0, 2), (3, 0, 4), (3, 0, 8), (3, 0, 0), (4, 1, 2), (4, 1, 6), (4, 1, 8), (4, 1, 0), (4, 2, 1), (4, 2, 5), (4, 2, 7), (4, 3, 4), (4, 3, 6), (4, 3, 0), (4, 4, 3), (4, 4, 5), (4, 4, 9), (4, 5, 2), (4, 5, 4), (4, 5, 8), (4, 6, 1), (4, 6, 3), (4, 6, 7), (4, 6, 9), (4, 7, 2), (4, 7, 6), (4, 7, 8), (4, 7, 0), (4, 8, 1), (4, 8, 5), (4, 8, 7), (4, 9, 4), (4, 9, 6), (4, 9, 0), (4, 0, 1), (4, 0, 3), (4, 0, 7), (4, 0, 9), (5, 1, 1), (5, 1, 5), (5, 1, 7), (5, 2, 4), (5, 2, 6), (5, 2, 0), (5, 3, 3), (5, 3, 5), (5, 3, 9), (5, 4, 2), (5, 4, 4), (5, 4, 8), (5, 5, 1), (5, 5, 3), (5, 5, 7), (5, 5, 9), (5, 6, 2), (5, 6, 6), (5, 6, 8), (5, 6, 0), (5, 7, 1), (5, 7, 5), (5, 7, 7), (5, 8, 4), (5, 8, 6), (5, 8, 0), (5, 9, 3), (5, 9, 5), (5, 9, 9), (5, 0, 2), (5, 0, 6), (5, 0, 8), (5, 0, 0), (6, 1, 4), (6, 1, 6), (6, 1, 0), (6, 2, 3), (6, 2, 5), (6, 2, 9), (6, 3, 2), (6, 3, 4), (6, 3, 8), (6, 4, 1), (6, 4, 3), (6, 4, 7), (6, 4, 9), (6, 5, 2), (6, 5, 6), (6, 5, 8), (6, 5, 0), (6, 6, 1), (6, 6, 5), (6, 6, 7), (6, 7, 4), (6, 7, 6), (6, 7, 0), (6, 8, 3), (6, 8, 5), (6, 8, 9), (6, 9, 2), (6, 9, 4), (6, 9, 8), (6, 0, 1), (6, 0, 5), (6, 0, 7), (7, 1, 3), (7, 1, 5), (7, 1, 9), (7, 2, 2), (7, 2, 4), (7, 2, 8), (7, 3, 1), (7, 3, 3), (7, 3, 7), (7, 3, 9), (7, 4, 2), (7, 4, 6), (7, 4, 8), (7, 4, 0), (7, 5, 1), (7, 5, 5), (7, 5, 7), (7, 6, 4), (7, 6, 6), (7, 6, 0), (7, 7, 3), (7, 7, 5), (7, 7, 9), (7, 8, 2), (7, 8, 4), (7, 8, 8), (7, 9, 1), (7, 9, 3), (7, 9, 7), (7, 0, 4), (7, 0, 6), (7, 0, 0), (8, 1, 2), (8, 1, 4), (8, 1, 8), (8, 2, 1), (8, 2, 3), (8, 2, 7), (8, 2, 9), (8, 3, 2), (8, 3, 6), (8, 3, 8), (8, 3, 0), (8, 4, 1), (8, 4, 5), (8, 4, 7), (8, 5, 4), (8, 5, 6), (8, 5, 0), (8, 6, 3), (8, 6, 5), (8, 6, 9), (8, 7, 2), (8, 7, 4), (8, 7, 8), (8, 8, 1), (8, 8, 3), (8, 8, 7), (8, 9, 2), (8, 9, 6), (8, 9, 0), (8, 0, 3), (8, 0, 5), (8, 0, 9), (9, 1, 1), (9, 1, 3), (9, 1, 7), (9, 1, 9), (9, 2, 2), (9, 2, 6), (9, 2, 8), (9, 2, 0), (9, 3, 1), (9, 3, 5), (9, 3, 7), (9, 4, 4), (9, 4, 6), (9, 4, 0), (9, 5, 3), (9, 5, 5), (9, 5, 9), (9, 6, 2), (9, 6, 4), (9, 6, 8), (9, 7, 1), (9, 7, 3), (9, 7, 7), (9, 8, 2), (9, 8, 6), (9, 8, 0), (9, 9, 1), (9, 9, 5), (9, 0, 2), (9, 0, 4), (9, 0, 8)]
primeSetStartingWithZero = [(0, 1, 1), (0, 1, 2), (0, 1, 4), (0, 1, 6), (0, 2, 1), (0, 2, 3), (0, 2, 5), (0, 2, 9), (0, 2, 0), (0, 3, 2), (0, 3, 4), (0, 3, 8), (0, 3, 0), (0, 4, 1), (0, 4, 3), (0, 4, 7), (0, 4, 9), (0, 5, 2), (0, 5, 6), (0, 5, 8), (0, 5, 0), (0, 6, 1), (0, 6, 5), (0, 6, 7), (0, 7, 4), (0, 7, 6), (0, 7, 0), (0, 8, 3), (0, 8, 5), (0, 8, 9), (0, 9, 2), (0, 9, 4), (0, 9, 8), (0, 0, 2), (0, 0, 3), (0, 0, 5), (0, 0, 7)]
#print(len(primeSet))
def check(s,primeList,l):
    for i in range(l-2):
        num = sum(s[i:i+3])
        if num not in primeList:
            return False
    for i in range(l-3):
        num = sum(s[i:i+4])
        if num not in primeList:
            return False
    for i in range(l-4):
        num = sum(s[i:i+5])
        if num not in primeList:
            return False
    return True

def getFuckinNumList(iterations, oldlist):
    newlist = []
    # print("got", iterations)
    if iterations > 1:
        for i in primeSetStartingWithZero+primeSet:
            for j in oldlist:
                newlist.append(j+i)
        return getFuckinNumList(iterations-1,newlist)
    else:
        return oldlist

# a = check((9, 0, 2, 0, 0, 5),primeList,6)
# print(a)
intlist = [1,2,3,4,5,6,7,8,9,0]
q = int(input().strip())
for _ in range(q):
    n = int(input().strip())
    c = 0
    numlist = primeSet[:]
    if n//3 >1:
        numlist = getFuckinNumList(n//3, numlist)
    if n%3 != 0:
        numlist = [x+i for x in numlist for i in product(intlist, repeat=n%3)]
    print(len(numlist))

    print((9, 0, 2, 0, 0, 5) in numlist)

    for j in numlist:
        # print(j)
        if check(j,primeList,n):
            c+=1
            # print(j)

    print(c)