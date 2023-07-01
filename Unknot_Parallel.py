import regina
import random
import time
from itertools import combinations
from threading import Thread
import multiprocessing


# Start all threads. 
Answer = [False]*101
# global thre
# thre = 20
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




def SpecialGreedyDeep(thre, D, S, k, we):
    # print(S)
    # print(D)
    # print(k)
    n = D.size()
    if(n==0) :
        Answer[we] = True
        return True
    if k<0 :
      # print(S)
      Answer[we] = False
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
            L = regina.Link(D)
            if L.r2(L.crossing(index), True, True) :
                S1 = refinery(S, index, next)
                greedy = True
                if(SpecialGreedyDeep(thre, L, S1, k, we)): 
                  Answer[we] = True
                  return True

    if(greedy) :
        Answer[we] = False
        return False
    
    # Let's apply special moves
    # R2-  :
    for index in S :
        next = D.crossing(index).next(1).crossing().index()
        if(next not in S):
            continue
        else :
            L = regina.Link(D)
            if L.r2(L.crossing(index), True, True):
                
                
                S1 = refinery(S, index, next)
                if(SpecialGreedyDeep(thre, L, S1, k, we)): 
                  Answer[we] = True 
                  return True
    
    # R1-  :
    for index in S :
        L = regina.Link(D)
        if L.r1(L.crossing(index), True, True) :
            
            
            S1 = refinery(S, index, n)
            if(SpecialGreedyDeep(thre, L, S1, k, we)): 
              Answer[we] = True
              return True

    
                

    # R1+  :
    for index in S :
        next = D.crossing(index).next(1).crossing().index()
        if(next not in S):
            continue
        else :
            L = regina.Link(D)
            if L.r1(L.crossing(index).next(1), 1, 1, True, True):
                S1 = S.copy()
                S1.add(n)
                if(SpecialGreedyDeep(thre, L, S1, k-1, we)): 
                  Answer[we] = True
                  return True
            L = regina.Link(D)
            if L.r1(L.crossing(index).next(1), 0, 1, True, True):
                S1 = S.copy()
                S1.add(n)
                if(SpecialGreedyDeep(thre, L, S1, k-1, we)): 
                  Answer[we] = True
                  return True
            L = regina.Link(D)
            if L.r1(L.crossing(index).next(1), 1, -1, True, True):
                S1 = S.copy()
                S1.add(n)
                if(SpecialGreedyDeep(thre, L, S1, k-1, we)): 
                  Answer[we] = True
                  return True
            L = regina.Link(D)
            if L.r1(L.crossing(index).next(1), 0, -1, True, True):
                S1 = S.copy()
                S1.add(n)
                if(SpecialGreedyDeep(thre, L, S1, k-1, we)): 
                  Answer[we] = True
                  return True
        next = D.crossing(index).next(0).crossing().index()
        if(next not in S):
            continue
        else :
            L = regina.Link(D)
            if L.r1(L.crossing(index).next(0), 1, 1, True, True):
                S1 = S.copy()
                S1.add(n)
                if(SpecialGreedyDeep(thre, L, S1, k-1, we)): 
                  Answer[we] = True
                  return True
            L = regina.Link(D)
            if L.r1(L.crossing(index).next(0), 0, 1, True, True):
                S1 = S.copy()
                S1.add(n)
                if(SpecialGreedyDeep(thre, L, S1, k-1, we)): 
                  Answer[we] = True
                  return True
            L = regina.Link(D)
            if L.r1(L.crossing(index).next(0), 1, -1, True, True):
                S1 = S.copy()
                S1.add(n)
                if(SpecialGreedyDeep(thre, L, S1, k-1, we)): 
                  Answer[we] = True
                  return True
            L = regina.Link(D)
            if L.r1(L.crossing(index).next(0), 0, -1, True, True):
                S1 = S.copy()
                S1.add(n)
                if(SpecialGreedyDeep(thre, L, S1, k-1, we)): 
                  Answer[we] = True
                  return True

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
                    L = regina.Link(D)
                    if L.r2(L.crossing(index).next(1), 0, L.crossing(index2).next(1), 1, True, True):
                        S1 = S.copy()
                        S1.add(n)
                        S1.add(n+1)
                        if(SpecialGreedyDeep(thre, L, S1, k-2, we)): 
                          Answer[we] = True
                          return True
                    L = regina.Link(D)
                    if L.r2(L.crossing(index).next(1), 0, L.crossing(index2).next(1), 0, True, True):
                        S1 = S.copy()
                        S1.add(n)
                        S1.add(n+1)
                        if(SpecialGreedyDeep(thre, L, S1, k-2, we)): 
                          Answer[we] = True
                          return True
                    L = regina.Link(D)
                    if L.r2(L.crossing(index).next(1), 1, L.crossing(index2).next(1), 1, True, True):
                        S1 = S.copy()
                        S1.add(n)
                        S1.add(n+1)
                        if(SpecialGreedyDeep(thre, L, S1, k-2, we)): 
                          Answer[we] = True
                          return True
                    L = regina.Link(D)
                    if L.r2(L.crossing(index).next(1), 1, L.crossing(index2).next(1), 0, True, True):
                        S1 = S.copy()
                        S1.add(n)
                        S1.add(n+1)
                        if(SpecialGreedyDeep(thre, L, S1, k-2, we)): 
                          Answer[we] = True
                          return True
                next = D.crossing(index2).next(0).crossing().index()
                if(next not in S):
                    continue
                else :
                    L = regina.Link(D)
                    if L.r2(L.crossing(index).next(1), 0, L.crossing(index2).next(0), 1, True, True):
                        S1 = S.copy()
                        S1.add(n)
                        S1.add(n+1)
                        if(SpecialGreedyDeep(thre, L, S1, k-2, we)): 
                          Answer[we] = True
                          return True
                    L = regina.Link(D)
                    if L.r2(L.crossing(index).next(1), 0, L.crossing(index2).next(0), 0, True, True):
                        S1 = S.copy()
                        S1.add(n)
                        S1.add(n+1)
                        if(SpecialGreedyDeep(thre, L, S1, k-2, we)): 
                          Answer[we] = True
                          return True
                    L = regina.Link(D)
                    if L.r2(L.crossing(index).next(1), 1, L.crossing(index2).next(0), 1, True, True):
                        S1 = S.copy()
                        S1.add(n)
                        S1.add(n+1)
                        if(SpecialGreedyDeep(thre, L, S1, k-2, we)): 
                          Answer[we] = True
                          return True
                    L = regina.Link(D)
                    if L.r2(L.crossing(index).next(1), 1, L.crossing(index2).next(0), 0, True, True):
                        S1 = S.copy()
                        S1.add(n)
                        S1.add(n+1)
                        if(SpecialGreedyDeep(thre, L, S1, k-2, we)): 
                          Answer[we] = True
                          return True
        next = D.crossing(index).next(0).crossing().index()
        if(next not in S):
            continue
        else :
            for index2 in S :
                next = D.crossing(index2).next(1).crossing().index()
                if(next not in S):
                    continue
                else :
                    L = regina.Link(D)
                    if L.r2(L.crossing(index).next(0), 0, L.crossing(index2).next(1), 1, True, True):
                        S1 = S.copy()
                        S1.add(n)
                        S1.add(n+1)
                        if(SpecialGreedyDeep(thre, L, S1, k-2, we)): 
                          Answer[we] = True
                          return True
                    L = regina.Link(D)
                    if L.r2(L.crossing(index).next(0), 0, L.crossing(index2).next(1), 0, True, True):
                        S1 = S.copy()
                        S1.add(n)
                        S1.add(n+1)
                        if(SpecialGreedyDeep(thre, L, S1, k-2, we)): 
                          Answer[we] = True
                          return True
                    L = regina.Link(D)
                    if L.r2(L.crossing(index).next(0), 1, L.crossing(index2).next(1), 1, True, True):
                        S1 = S.copy()
                        S1.add(n)
                        S1.add(n+1)
                        if(SpecialGreedyDeep(thre, L, S1, k-2, we)): 
                          Answer[we] = True
                          return True
                    L = regina.Link(D)
                    if L.r2(L.crossing(index).next(0), 1, L.crossing(index2).next(1), 0, True, True):
                        S1 = S.copy()
                        S1.add(n)
                        S1.add(n+1)
                        if(SpecialGreedyDeep(thre, L, S1, k-2, we)): 
                          Answer[we] = True
                          return True
                next = D.crossing(index2).next(0).crossing().index()
                if(next not in S):
                    continue
                else :
                    L = regina.Link(D)
                    if L.r2(L.crossing(index).next(0), 0, L.crossing(index2).next(0), 1, True, True):
                        S1 = S.copy()
                        S1.add(n)
                        S1.add(n+1)
                        if(SpecialGreedyDeep(thre, L, S1, k-2, we)): 
                          Answer[we] = True
                          return True
                    L = regina.Link(D)
                    if L.r2(L.crossing(index).next(0), 0, L.crossing(index2).next(0), 0, True, True):
                        S1 = S.copy()
                        S1.add(n)
                        S1.add(n+1)
                        if(SpecialGreedyDeep(thre, L, S1, k-2, we)): 
                          Answer[we] = True
                          return True
                    L = regina.Link(D)
                    if L.r2(L.crossing(index).next(0), 1, L.crossing(index2).next(0), 1, True, True):
                        S1 = S.copy()
                        S1.add(n)
                        S1.add(n+1)
                        if(SpecialGreedyDeep(thre, L, S1, k-2, we)): 
                          Answer[we] = True
                          return True
                    L = regina.Link(D)
                    if L.r2(L.crossing(index).next(0), 1, L.crossing(index2).next(0), 0, True, True):
                        S1 = S.copy()
                        S1.add(n)
                        S1.add(n+1)
                        if(SpecialGreedyDeep(thre, L, S1, k-2, we)): 
                          Answer[we] = True
                          return True
      # R3  :
    # print(thre)
    if(thre==0):
      return False
    thre -= 1
    for index in S:
        S1 = S
        L = regina.Link(D)
        if(L.r3(L.crossing(index), 0, True, True)) :
            next = D.crossing(index).next(1).crossing().index()
            if(next not in S) :
                continue
            if(D.crossing(index).sign()== -1) :
                cros2 = D.crossing(index).prev(0).crossing().index()
                if(cros2 not in S) :
                    continue
                
                
                if(SpecialGreedyDeep(thre ,L, S1, k, we)): 
                  Answer[we] = True
                  return True
            else :
                cros2 = D.crossing(index).next(0).crossing().index()
                if(cros2 not in S) :
                    continue
                # L = regina.Link(D)
                # L.r3(L.crossing(index), 0, True, True)
                if(SpecialGreedyDeep(thre , L, S1, k, we)): 
                  Answer[we] = True
                  return True
        L = regina.Link(D)
        if(L.r3(L.crossing(index), 1, True, True)) :
            next = D.crossing(index).next(1).crossing().index()
            if(next not in S) :
                continue
            if(D.crossing(index).sign()== -1) :
                cros2 = D.crossing(index).next(0).crossing().index()
                if(cros2 not in S) :
                    continue
                
                
                if(SpecialGreedyDeep(thre, L, S1, k, we)): 
                  Answer[we] = True
                  return True
            else :
                cros2 = D.crossing(index).prev(0).crossing().index()
                if(cros2 not in S) :
                    continue
                # L = regina.Link(D)
                # L.r3(L.crossing(index), 1, True, True)
                if(SpecialGreedyDeep(thre, L, S1, k, we)): 
                  Answer[we] = True
                  return True
    return False
        

def SpecialGreedy(D, k, all_set):
    # global thre
    thre = 20
    n = D.size()
    # while(True) :
        # Get all combinations of [2, 1, 3]
        # and length 2
    random_numb = [*range(1, n + 1)]
    threads = []
    random_numb = [n]
    random.shuffle(random_numb)
    print(random_numb)
    
    for i in random_numb :
        comb = combinations(all_set, i)
       
        for j in list(comb) :
          # print(j)
            # if(SpecialGreedyDeep(thre, D, set(j), k, 0)) :
            #     return True
          # t = multiprocessing.Process(target = SpecialGreedyDeep, args=(D, set(j), k, len(threads),))
          
          t = Thread(target = SpecialGreedyDeep, args=(thre, D, set(j), k, len(threads),))
          
          threads.append(t)
          if(len(threads)==4) :
            for t in threads :
              t.start()
            # print("strike")
            for t in threads :
              t.join()
            threads = []  
            if(True in Answer) :
              return True
            
    if(len(threads)!=0) :
        for t in threads :
              t.start()
        print("strike1")
        for t in threads :
          t.join()
        threads = []      
        if(True in Answer) :
          return True
        
            # print(set(j))
        # special_set = set(random.sample(range(0,n), random.randint(1, min(n, 3*k))))
            # if(SpecialGreedyDeep(D, set(j), k)) :
            #     return True



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
# if(lnk.simplifyExhaustive	(-1, 100,)) :
#     print("True")
# else : print("False")

if(SpecialGreedy(lnk, k, all_set)) :
    print("True")
else : print("False")
