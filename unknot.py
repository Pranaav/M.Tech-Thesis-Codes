import regina
import random
from itertools import combinations


def refinery(S, i, j) :
    S1 = set()
    for ind in S :
        if (ind==i) or (ind == j) :
            continue
        elif (ind > i) and (ind < j) :
            S1.add(ind-1)
        elif (ind < i) and (ind > j) :
            S1.add(ind-1)
        elif (ind > i) and (ind > j) :
            S1.add(ind -2)   
        else :
            S1.add(ind)
    return S1




def SpecialGreedyDeep(D, S, k):
    # print(S)
    # print(D)
    # print(k)
    n = D.size()
    if(n==0) :
        return True
    if k<0 :
        return False
    # if D is unknot return true
    # for()

    # Greedy move r2-
    greedy = False
    for index in range(0, n):
        if(index in S) : 
            continue
        next = D.crossing(index).next(1).crossing().index()
        if(next in S):
            continue
        else :
            if D.r2(D.crossing(index), True, False) :
                L = regina.Link(D)
                L.r2(L.crossing(index), True, True)
                S1 = refinery(S, index, next)
                greedy = True
                if(SpecialGreedyDeep(L, S1, k)): return True
    if(greedy) :
        return False
    
    # Let's apply special moves
    # R2-  :
    for index in S :
        next = D.crossing(index).next(1).crossing().index()
        if(next not in S):
            continue
        else :
            if D.r2(D.crossing(index), True, False) :
                L = regina.Link(D)
                L.r2(L.crossing(index), True, True)
                S1 = refinery(S, index, next)
                if(SpecialGreedyDeep(L, S1, k)): return True
    
    # R1-  :
    for index in S :
        if D.r1(D.crossing(index), True, False) :
            L = regina.Link(D)
            L.r1(L.crossing(index), True, True)
            S1 = refinery(S, index, n)
            if(SpecialGreedyDeep(L, S1, k-1)): return True

    # R3  :
    for index in S:
        S1 = S
        if(D.r3(D.crossing(index), 0, True, False)) :
            next = D.crossing(index).next(1).crossing().index()
            if(next not in S) :
                continue
            if(D.crossing(index).sign()== -1) :
                cros2 = D.crossing(index).prev(0).crossing().index()
                if(cros2 not in S) :
                    continue
                L = regina.Link(D)
                L.r3(L.crossing(index), 0, True, True)
                if(SpecialGreedyDeep(L, S1, k-2)): return True
            else :
                cros2 = D.crossing(index).next(0).crossing().index()
                if(cros2 not in S) :
                    continue
                L = regina.Link(D)
                L.r3(L.crossing(index), 0, True, True)
                if(SpecialGreedyDeep(L, S1, k-2)): return True
        if(D.r3(D.crossing(index), 1, True, False)) :
            next = D.crossing(index).next(1).crossing().index()
            if(next not in S) :
                continue
            if(D.crossing(index).sign()== -1) :
                cros2 = D.crossing(index).next(0).crossing().index()
                if(cros2 not in S) :
                    continue
                L = regina.Link(D)
                L.r3(L.crossing(index), 0, True, True)
                if(SpecialGreedyDeep(L, S1, k-2)): return True
            else :
                cros2 = D.crossing(index).prev(0).crossing().index()
                if(cros2 not in S) :
                    continue
                L = regina.Link(D)
                L.r3(L.crossing(index), 0, True, True)
                if(SpecialGreedyDeep(L, S1, k-2)): return True

    # R1+  :
    for index in S :
        next = D.crossing(index).next(1).crossing().index()
        if(next not in S):
            continue
        else :
            if D.r1(D.crossing(index).next(1), 1, 1, True, False) :
                L = regina.Link(D)
                L.r1(L.crossing(index).next(1), 1, 1, True, True)
                S1 = S.copy()
                S1.add(n)
                if(SpecialGreedyDeep(L, S1, k-3)): return True
        next = D.crossing(index).next(0).crossing().index()
        if(next not in S):
            continue
        else :
            if D.r1(D.crossing(index).next(0), 1, 1, True, False) :
                L = regina.Link(D)
                L.r1(L.crossing(index).next(0), 1, 1, True, True)
                S1 = S.copy()
                S1.add(n)
                if(SpecialGreedyDeep(L, S1, k-3)): return True


    # R2+  :
    for index in S :
        next = D.crossing(index).next(1).crossing().index()
        if(next not in S):
            continue
        else :
            for index2 in S :
                next = D.crossing(index2).next(1).crossing().index()
                if(next not in S):
                    continue
                else :
                    if D.r2(D.crossing(index).next(1), 0, D.crossing(index2).next(1), 1, True, False) :
                        L = regina.Link(D)
                        L.r2(L.crossing(index).next(1), 0, L.crossing(index2).next(1), 1, True, True)
                        S1 = S.copy()
                        S1.add(n)
                        S1.add(n+1)
                        if(SpecialGreedyDeep(L, S1, k-4)): return True
                next = D.crossing(index2).next(0).crossing().index()
                if(next not in S):
                    continue
                else :
                    if D.r2(D.crossing(index).next(1), 0, D.crossing(index2).next(0), 1, True, False) :
                        L = regina.Link(D)
                        L.r2(L.crossing(index).next(1), 0, L.crossing(index2).next(0), 1, True, True)
                        S1 = S.copy()
                        S1.add(n)
                        S1.add(n+1)
                        if(SpecialGreedyDeep(L, S1, k-4)): return True
        next = D.crossing(index).next(0).crossing().index()
        if(next not in S):
            continue
        else :
            for index2 in S :
                next = D.crossing(index2).next(1).crossing().index()
                if(next not in S):
                    continue
                else :
                    if D.r2(D.crossing(index).next(0), 0, D.crossing(index2).next(1), 1, True, False) :
                        L = regina.Link(D)
                        L.r2(L.crossing(index).next(0), 0, L.crossing(index2).next(1), 1, True, True)
                        S1 = S.copy()
                        S1.add(n)
                        S1.add(n+1)
                        if(SpecialGreedyDeep(L, S1, k-4)): return True
                next = D.crossing(index2).next(0).crossing().index()
                if(next not in S):
                    continue
                else :
                    if D.r2(D.crossing(index).next(0), 0, D.crossing(index2).next(0), 1, True, False) :
                        L = regina.Link(D)
                        L.r2(L.crossing(index).next(0), 0, L.crossing(index2).next(0), 1, True, True)
                        S1 = S.copy()
                        S1.add(n)
                        S1.add(n+1)
                        if(SpecialGreedyDeep(L, S1, k-4)): return True
        






def SpecialGreedy(D, k, all_set):
    n = D.size()
    # while(True) :
        # Get all combinations of [2, 1, 3]
        # and length 2
    for i in range(1, min(n, 3*k) + 1) :
        comb = combinations(all_set, i)
        for j in list(comb) :
            # print(set(j))
        # special_set = set(random.sample(range(0,n), random.randint(1, min(n, 3*k))))
            print(j)
            if(SpecialGreedyDeep(D, set(j), k)) :
                return True



file = open("input.txt")

content = file.readlines()

n = int(content[0])
gauss_code = content[1]
k = int(content[2])

print(gauss_code)

lnk = regina.Link.fromGauss(gauss_code)

print(lnk.crossing(1))
all_set = set()
for i in range(0, n):
    all_set.add(i)
# tracker = regina.ProgressTrackerOpen()
# if(lnk.simplifyExhaustive	(1, 0, tracker)) :
#     print("True")
# else : print("False")
if(SpecialGreedy(lnk, k, all_set)) :
    print("True")
else : print("False")
