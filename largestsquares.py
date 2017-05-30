area=15342
areas=[]
areahold=area
remain=1
while remain>0:
    yards=areahold**.5
    biglength, remain=divmod(yards,1)
    bigarea=biglength**2
    areas.append(bigarea)
    areahold=areahold-bigarea
    print (remain)
print(areas)