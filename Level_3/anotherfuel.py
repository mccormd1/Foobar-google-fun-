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

# m=[[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]] 
# m=[[0, 2, 1, 0, 0], [0, 1, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 4, 0, 0, 0], [0, 0, 0, 0, 0]]
import fractions
## need to define a bunch of matrix stuff.
def matsub(A,B): #performs matrix subtraction
    for i, row in enumerate(A):
        A[i]=[A[i][j]-B[i][j] for j,v in enumerate(row)]
    return A

def transposeMatrix(mat):
    t = []
    for r in range(len(mat)):
        tRow = []
        for c in range(len(mat[r])):
            if c == r:
                tRow.append(mat[r][c])
            else:
                tRow.append(mat[c][r])
        t.append(tRow)
    return t

def getMatrixMinor(mat,i,j):
    return [row[:j] + row[j+1:] for row in (mat[:i]+mat[i+1:])]

def getMatrixDeternminant(mat):
    #base case for 2x2 matrix
    if len(mat) == 2:
        return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]

    determinant = 0
    for c in range(len(mat)):
        determinant += ((-1)**c)*mat[0][c]*getMatrixDeternminant(getMatrixMinor(mat,0,c))
    return determinant

def getMatrixInverse(mat):
    determinant = getMatrixDeternminant(mat)
    #special case for 2x2 matrix:
    if len(mat) == 2:
        return [[mat[1][1]/determinant, -1*mat[0][1]/determinant],
                [-1*mat[1][0]/determinant, mat[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(mat)):
        cofactorRow = []
        for c in range(len(mat)):
            minor = getMatrixMinor(mat,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors           


def matmult(A,B):
    
    mat=[]
    r=len(B)
    if r is not 0:
        for ar in range(len(A)):
            t=[]
            for bc in range(len(B[0])):
                trow=[]
                for ac in range(len(A[ar])):
                    trow.append(A[ar][ac]*B[ac][bc])
                t.append(sum(trow))
            mat.append(t)
        return mat
    else:
        return 0




def answer(m):

    #sort rows
    mmm=list(m)
    rowsum=[]
    for i, row in enumerate(mmm):
        rowsum.append(sum(row))



    for i,row in enumerate(mmm):
        if rowsum[i]==0:
            mmm.append(mmm.pop(i))
        for j in range(len(row)):
            if rowsum[j]==1:
               mmm[i].append(mmm[i].pop(j))


    print(mmm)

    mm=[]   #convert into percentages
    for row in mmm:
        rowprob=[]
        rowsum=sum(row)
        for i in row:
            if rowsum == 0:
                rowprob.append(0)
            else:
                rowprob.append((float(i)/rowsum))
    
        mm.append(rowprob)
    


    print(mm)
    ##first create absorbing states by setting self referencing value in full zero rows to 1
    Imark=[None]*len(m)
    Qmark=[None]*len(m)
    for i, row in enumerate(mm):
        rowsum=sum(row)
    #     print(rowsum)
        if rowsum ==0:
    #         print(m[i],i)
            mm[i][i]=1
            Imark[i]=1
        
        else:
            Qmark[i]=1

    print (mm,Qmark,Imark)



    ## list should be a version of the standard form p=[Q, R],[0 It] 
    # '''
    # [
    #   [0,1,|0,0,0,1],  
    #   [4,0,|0,3,2,0],
    #   -------------  
    #   [0,0,|1,0,0,0],  
    #   [0,0,|0,1,0,0],  
    #   [0,0,|0,0,1,0],  
    #   [0,0,|0,0,0,1],  
    # ]
    # '''
    ##split the matrix into it's parts (only need Q right now)

    QR=[mm[i] for i, a in enumerate(Qmark) if a==1]
    Q=[[0]*Qmark.count(1) for i, a in enumerate(Qmark) if a==1]
    R=[[0]*Imark.count(1) for i, a in enumerate(Qmark) if a==1]
    I=list(Q)

    for i, row in enumerate(QR):
        Q[i]=[QR[i][j] for j, a in enumerate(Qmark) if a==1]
        R[i]=[QR[i][j] for j, a in enumerate(Imark) if a==1]

    # print('R is:',R)
    # Q=[QR[i]
    # I=[m[i][i] for i, a in enumerate(Imark) if a==1]

    # Create identity same size as Q
    for i in range(Qmark.count(1)):
        I[i][i] = 1.0

    # print('Q is:',Q,I)
    ## the fundamental matrix F=(I-Q)^-1, lets get I-Q first. different I than above.

    IQ=matsub(I,Q)
    F=getMatrixInverse(IQ)  #invert the matrix
    # print(F)

    FR=matmult(F,R) #matmultiply F by R
    if FR ==0:
#         pass
        return 0
    else:
        k=FR[0]
    print(k,len(FR),len(FR[0]))

    #     fraclevels=[fractions.Fraction(i).limit_denominator(27) for i in FR[0]]
    fraclevels=[]
    for i in FR[0]:
        fraclevels.append(fractions.Fraction(i).limit_denominator(27))
    
    # print(fraclevels)

    commonmult=0
    for i, value in enumerate(fraclevels):
        if i ==0:
            commonmult=value
        else:
            commonmult=fractions.gcd(commonmult,value)
    
    numerators=[i.numerator for i in fraclevels]

    denommults=[commonmult.denominator/i.denominator for i in fraclevels]

    finallist=[int(a*b) for a,b in zip(numerators,denommults)]
    finallist.append(commonmult.denominator)
#     print(finallist)
    return finallist

print(answer(m))