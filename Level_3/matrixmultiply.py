def matmult(A,B):
    
    m=[]
    for ar in range(len(A)):
        t=[]
        for bc in range(len(B[0])):
            trow=[]
            for ac in range(len(A[ar])):
                trow.append(A[ar][ac]*B[ac][bc])
            t.append(sum(trow))
        m.append(t)
    return m
