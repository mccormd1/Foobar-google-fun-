


# m=[[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]] 
# m=[[0, 2, 1, 0, 0], [0, 1, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0]]
# m=[[0, 2, 1, 0, 0, 0], [0, 0, 0, 3, 4, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]]
m=[[1, 1, 1, 0, 1, 0, 1, 0, 1, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[1, 0, 1, 1, 1, 0, 1, 0, 1, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[1, 0, 1, 0, 1, 1, 1, 0, 1, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[1, 0, 1, 0, 1, 0, 1, 1, 1, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[1, 0, 1, 0, 1, 0, 1, 0, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

##make duplicate of list
dupem=list(m)
from copy import deepcopy
##calculate row sums (find zero rows)

hrowsum=[]
for i, row in enumerate(dupem):
    j=[]
    j.append(sum(row))
    j.append(i)
    hrowsum.append(j)

print(hrowsum)

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
print(rowstandard,si)

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
for row in mmm:
    print(row)
    
for newi, originali in enumerate(si):
    if hrowsum[originali][0]==mmm[newi][newi]:
        mmm[newi][newi]=0
        moverowsum[newi][0]=0

    
print(hrowsum,si,moverowsum)            
print(id(hrowsum),id(moverowsum))            
            
            
# for row in mmm:
#     print(row)
