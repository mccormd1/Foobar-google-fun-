# m=[[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]] 
# m=[[0, 2, 1, 0, 0], [0, 1, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0]]
# m=[[0, 2, 1, 0, 0, 0], [0, 0, 0, 3, 4, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]]
# m=[[0, 2, 1, 0, 0, 0], [0, 0, 0, 3, 4, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]]
# m=[[0, 0, 0, 0, 3, 5, 0, 0, 0, 2],[0, 0, 4, 0, 0, 0, 1, 0, 0, 0],[0, 0, 0, 4, 4, 0, 0, 0, 1, 1],[13, 0, 0, 0, 0, 0, 2, 0, 0, 0],[0, 1, 8, 7, 0, 0, 0, 1, 3, 0],[1, 7, 0, 0, 0, 0, 0, 2, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
m=[[0]]
import fractions
from copy import deepcopy

## need to define a bunch of matrix stuff.
def matsub(A,B): #performs matrix subtraction
    C=list(A)
    for i, row in enumerate(A):
        C[i]=[A[i][j]-B[i][j] for j,v in enumerate(row)]
    return C

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
    try:
        ##make duplicate of list
        dupem=list(m)
        ##calculate row sums (find zero rows)

        hrowsum=[]
        for i, row in enumerate(dupem):
            j=[]
            j.append(sum(row))
            j.append(i)
            hrowsum.append(j)

        # print(hrowsum)

        ##move rows into standard form (keep track of original location)

        moverowsum=list(hrowsum)
        keeprow=[]
        ki=[]
        moverow=[]
        mi=[]
        for i,row in enumerate(dupem):
            if moverowsum[i][0]==0:
                moverow.append(dupem[i])
                mi.append(i)
            else:
                keeprow.append(dupem[i])
                ki.append(i)
        # print('keep,move',keeprow,ki,moverow,mi)

        rowstandard=keeprow+moverow
        si=ki+mi
        # print(rowstandard,si)

        ## move columns into standard form (keep track of original location)

        back=[]
        front=[]
        for i,row in enumerate(rowstandard):
            fe=[]
            be=[]
            count=0
            for j in range(len(row)):
                if hrowsum[j][0]==0:
                    be.append(rowstandard[i][j])
                else:
                    fe.append(rowstandard[i][j])
            back.append(be)
            front.append(fe)

        mmm=[]
        for row  in range(len(front)):
            mmm.append(front[row]+back[row])


        ## create a standardized version of hrowsum
        copyhrowsum=deepcopy(hrowsum)
        moverowsum=[]
        for newi, originali in enumerate(si):
            moverowsum.append(copyhrowsum[originali])

        ## sets all absorbing states with loops back to itself to zero
        # for row in mmm:
        #     print(row)
    
        for newi, originali in enumerate(si):
            if hrowsum[originali][0]==mmm[newi][newi]:
                mmm[newi][newi]=0
                moverowsum[newi][0]=0

    
        ## sets all absorbing states with loops back to itself to zero
        # for row in mmm:
        #     print(row)
    
        for newi, originali in enumerate(si):
            if hrowsum[originali][0]==mmm[newi][newi]:
                mmm[newi][newi]=0


    

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

        # print(mm)
        ##first create absorbing states by setting self referencing value in full zero rows to 1
        Imark=[None]*len(m)
        Qmark=[None]*len(m)
        sumqmark=0
        for i, row in enumerate(mm):
            rowsum=sum(row)
        #     print(rowsum)
            if rowsum ==0:
        #         print(m[i],i)
                mm[i][i]=1
                Imark[i]=1
        
            else:
                Qmark[i]=1
                sumqmark+=1
        # print(sumqmark)
        # print ('help',mm,Qmark,sumqmark,Imark)


        # for row in mm:
        #     print(row)
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
        # print(I)
        F=getMatrixInverse(IQ)  #invert the matrix
        # print(F)

        FR=matmult(F,R) #matmultiply F by R
        # print(FR)
        if FR ==0:
            pass
#             return 0 #THIS NEEDS TO BE THERE FOR SOME REASON
        else:
            k=FR[0]
        # print(k,len(FR),len(FR[0]))

        #     fraclevels=[fractions.Fraction(i).limit_denominator(27) for i in FR[0]]
        # print(k)
        fraclevels=[]
        for i in FR[0]:
            fraclevels.append(fractions.Fraction(i).limit_denominator(100))
    
        # print(fraclevels)

        commonmult=0
        for i, value in enumerate(fraclevels):
            if i ==0:
                commonmult=value
            else:
                commonmult=fractions.gcd(commonmult,value)
    
        numerators=[i.numerator for i in fraclevels]
        denommults=[commonmult.denominator/i.denominator for i in fraclevels]
        interlist=[int(a*b) for a,b in zip(numerators,denommults)]

        # print(interlist)

        ##now we gotta get it back into the original shape

        ## turn into a full list of end numerators
        finallist=[]
        count=0
        for i in range(len(moverowsum)):
            if moverowsum[i][0]==0:
                finallist.append(interlist[count])
                count+=1
            elif moverowsum[i][0]!=0:
                finallist.append(0)
        # print('hrowcheck:',moverowsum,finallist)
        # print(sumqmark)

        ##turn back into original order
        standardlist=list(finallist)

    #     standardlist=[0]*len(finallist)
    #     for inew, ioriginal in enumerate(si):
    #         standardlist[ioriginal]=(finallist[inew])

        # print(standardlist)

        ## chop off non absorbing states
        anslist=standardlist[sumqmark:len(standardlist)]

        anslist.append(commonmult.denominator)

    #     print(anslist)

        return anslist
    except:
        if len(m)==1:
            return [1,1]
        else:
            return 0
    
    
print(answer(m))