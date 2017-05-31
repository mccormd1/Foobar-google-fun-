area=15342

def answer(s):
    areas=[]
    areahold=s
    remain=1
    while remain>0:
        yards=areahold**.5
        biglength, remain=divmod(yards,1)
        bigarea=biglength**2
        areas.append(bigarea)
        areahold=areahold-bigarea
        #print (remain)
    return areas
    

print(answer(area))