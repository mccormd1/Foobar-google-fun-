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
# m=[[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]] 
m=[[0, 2, 1, 0, 0], [0, 1, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# print(m)


    #for num in row:
    
    #print(rowsum)

# print(mm)
def answer(m):
    ##lol montecarlo simulation, because I'm an idiot - figure out the elegant way one day.
    import fractions

    def mygcd(a, b):
        """Calculate the Greatest Common Divisor of a and b.

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
        while b:
            a, b = b, a%b
        return a
  
    def allgcd(L):
        return reduce(fractions.gcd, L)

    # import random
    # def answer(m):
  

    mm=[]
    for row in m:
        rowprob=[]
        rowsum=sum(row)
        for i in row:
            if rowsum == 0:
                rowprob.append(0)
            else:
                rowprob.append(float(i)/rowsum)

        mm.append(rowprob)

    mma=list(mm)
    mmb=list(mm)
    statehold=[0]*len(mm)

    # print(sum(remain))
#     while sum(statehold)<1.0-1e-10:
    for ii in range(10):
    #     print(sum(remain))

        if sum(statehold) >1-1e-10:
            break
        for A, row in enumerate(mma):
    #         print('row',row)
            for X, value in enumerate(row):
    #             print(mm[X])
                if value == 0:
                    continue
                else:
                    if sum(mm[X])==0:
                        statehold[X]+=value
    #                     holdval[X]=value
    #                     print('hold',holdval)
                    else:
    #                     print('mma',mma)
                        print(A,row,X,value)
    #                   
                        mmb[X]=[value*k for k in mm[X]]
    #                     mma[X]=[k/sum(mma[X]) for k in mma[X]]
    #                     print (A,X,mma)
    #     remain[i]=sum([ab for a,b in zip(mm[j],mmk[j])])
                mma[X]=mmb[X]
    #     remain=
        
        print('\n',statehold,'sum',sum(statehold),'\n')

    # print(mm,mma)
    fraclevels=[fractions.Fraction(i).limit_denominator(27) for i in statehold[2:len(statehold)]]
    print(fraclevels)    
    fracdom=[i.denominator for i in fraclevels]
    print(fracdom)
    commonmult=0
    for i, value in enumerate(fraclevels):
        if i ==0:
            commonmult=value
        else:
            commonmult=fractions.gcd(commonmult,value)
        
    # print(commonmult)
    


    #     commonmult=mygcd(
    #     commonmult=reduce(lambda x, y:fractions.gcd(x,y),fraclevels)
    #     print commonmult
    #     commonmult=allgcd(fraclevels.denominator)

    numerators=[i.numerator for i in fraclevels]

    denommults=[commonmult.denominator/i.denominator for i in fraclevels]

    finallist=[int(a*b) for a,b in zip(numerators,denommults)]
    finallist.append(commonmult.denominator)
    # print(finallist)
    return finallist


print(answer(m))