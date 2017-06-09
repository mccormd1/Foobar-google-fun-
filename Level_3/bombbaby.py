'''
Bomb, Baby!
===========

You're so close to destroying the LAMBCHOP doomsday device you can taste it! But in order to do so, you need to deploy special self-replicating bombs designed for you by the brightest scientists on Bunny Planet. There are two types: Mach bombs (M) and Facula bombs (F). The bombs, once released into the LAMBCHOP's inner workings, will automatically deploy to all the strategic points you've identified and destroy them at the same time. 

But there's a few catches. First, the bombs self-replicate via one of two distinct processes: 
Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;
Every Facula bomb spontaneously creates a Mach bomb.

For example, if you had 3 Mach bombs and 2 Facula bombs, they could either produce 3 Mach bombs and 5 Facula bombs, or 5 Mach bombs and 2 Facula bombs. The replication process can be changed each cycle. 

Second, you need to ensure that you have exactly the right number of Mach and Facula bombs to destroy the LAMBCHOP device. Too few, and the device might survive. Too many, and you might overload the mass capacitors and create a singularity at the heart of the space station - not good! 

And finally, you were only able to smuggle one of each type of bomb - one Mach, one Facula - aboard the ship when you arrived, so that's all you have to start with. (Thus it may be impossible to deploy the bombs to destroy the LAMBCHOP, but that's not going to stop you from trying!) 

You need to know how many replication cycles (generations) it will take to generate the correct amount of bombs to destroy the LAMBCHOP. Write a function answer(M, F) where M and F are the number of Mach and Facula bombs needed. Return the fewest number of generations (as a string) that need to pass before you'll have the exact number of bombs necessary to destroy the LAMBCHOP, or the string "impossible" if this can't be done! M and F will be string representations of positive integers no larger than 10^50. For example, if M = "2" and F = "1", one generation would need to pass, so the answer would be "1". However, if M = "2" and F = "4", it would not be possible.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string) M = "2"
    (string) F = "1"
Output:
    (string) "1"

Inputs:
    (string) M = "4"
    (string) F = "7"
Output:
    (string) "4" 
'''

# M="4"
# F="31"
# F=int(F)
# M=int(M)
# # print
# # for
# import math
# # print(M*math.floor(F/M))
# # if F > M:
# #     F=F-M*(F/M)
# # print(F,M)
# 
# F=int(F)
# M=int(M)
# count=0
# breaker=0
# while breaker==0:
#     if F>M:
#         F=F-M
#         count+=1
#         print('Fbigger',F,M)
#     elif M>F:
#         M=M-F
#         count+=1
#         print('Mbigger',F,M)
#     else:
#         breaker=1
# print('firstcount',count)
#M=1 +4**50
# F=4**50

M="11"
F="12"


def solvable(a,b):
    if a > 0 and b > 0 and a!=b:
        return 1
    else:
        return 0
    


import math
#M ="10"
# F="40003p"

def answer(M,F):
    F=int(F)
    M=int(M)
    count=0
    if M==1 and F==1:
        return 0
    
    while (F!=1 or M!=1) and solvable(F,M)==1:
        if F>M:
            multF=math.floor(F/M)
            print('multF',multF)
            print('all',F,M,count)
            if multF==F:
                count+=multF-1
                F-=M*multF-1
#                 count+=1
#                 F-=M
            else:
                count+=multF
                F-=M*multF
#             print(count)
        elif M>F:
            multM=math.floor(M/F)
            print('multM',multM)
            print('all',F,M,count)
            if multM==M:
                count+=multM-1
                M-=F*multM-1
#                 count+=1
#                 M-=F
            else:
                count+=multM
                M-=F*multM
#             print(count)
        elif M==1 and F==1:
            break
    strcount=str(int(count))
    print(F,M,count)
    # print(isinstance(strcount,str))
    if count==0 or F==0 or M==0:
        return 'impossible'
    else:
        return strcount

print(answer(M,F))