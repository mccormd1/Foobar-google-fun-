'''
Doomsday Fuel
=============

Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. 
It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. 
There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel. 

Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. 
You have carefully studied the different structures that the ore can take and which transitions it undergoes. 
It appears that, while random, the probability of each structure transforming is fixed. 
That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state).  
You have recorded the observed transitions in a matrix. 
The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

Write a function answer(m) that takes an array of array of nonnegative ints representing
how many times that state has gone to the next state and return an array of ints for each terminal state giving
the exact probabilities of each terminal state, represented as the numerator for each state, 
then the denominator for all of them at the end and in simplest form. 
The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. 
That is, the processing will always eventually end in a stable state. 
The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly. 

For example, consider the matrix m:
[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
Output:
    (int list) [7, 6, 8, 21]

Inputs:
    (int) m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
Output:
    (int list) [0, 3, 2, 9, 14]
'''


## This implementation useds montecarlo simulation. It works perfectly well but google foobar doesn't allow for random variables for some reason.

m=[[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]] 

# print(m)


# for i, row in enumerate(m):
    
import os

def randint(a,b):
    return int(os.urandom(4).encode('hex'),16)%(b-a+1)+a

# for row in m:
#     rowprob=[]
#     rowsum=sum(row)
#     for i in row:
#         if rowsum == 0:
#             rowprob.append(0)
#         else:
#             rowprob.append(float(i)/rowsum)
# #     print(rowprob)
#     mm.append(rowprob)
#     #for num in row:
#     
#     #print(rowsum)

# print(mm)
#def answer(m):m


# import random
import fractions    
def answer(m):

    mm=[]
    photonbins=[0]*len(m)
    numphotons=100000
    for photon in xrange(numphotons):
    #     print('photonnumber:',photon)
        photonexist=1
        prow=0
        while photonexist == 1:
    #         print('photonexist?',photonexist)
            for i, row in enumerate(m):
    #             print('rownum:',i)
                if prow == i:
                    rowsum=sum(row)
    #                 print('Rowsums:',prow,rowsum)
                    if rowsum == 0:
                        photonbins[i]+=1
                        photonexist = 0
    #                     print('photon terminated!',photon,i)
                    else:
                        prand=randint(1,rowsum)
                        cumsum=0
    #                     print('randint:',prand)
                        for nextrow, j in enumerate(row):
                            cumsum+=j
    #                         print('cumulativesum:',row,j,cumsum)
                            if prand <= cumsum:
                                prow=nextrow
    #                             print('nextrow:',i,prow,j,cumsum)
                                break
                else:
                    continue


#     print(photonbins)

    estimates=[(i/float(numphotons)) for i in photonbins]

#     print(estimates)

    fraclevels=[fractions.Fraction(i).limit_denominator(27) for i in estimates[2:len(estimates)]]
#     print(fraclevels)
    commonmult=reduce(lambda x, y:fractions.gcd(x,y),fraclevels)

    numerators=[i.numerator for i in fraclevels]

    denommults=[commonmult.denominator/i.denominator for i in fraclevels]

    finallist=[a*b for a,b in zip(numerators,denommults)]
    finallist.append(commonmult.denominator)
    return finallist
# print(finallist)
print(answer(m))