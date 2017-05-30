h=5
q=[19,14,28,31]


p=[]
for j in q:
    top=2**h-1
    if j == top:
        p.append(-1)
    else:
        for i in range(1,h):
            power=h-i
            tophalf=top-1
            bottomhalf=tophalf-(-1+2**power)        
            if bottomhalf < j < tophalf:
                top=tophalf
            elif j < bottomhalf:
                top=bottomhalf
            elif j in [tophalf, bottomhalf]:
                p.append(top)
                break


print(p)

    