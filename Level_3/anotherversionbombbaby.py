
M="11"
F="12"
import copy
def answer(M, F): 
    M = int(M)
    F = int(F)
    
    cycles = 0

    if M > F:
        maxi = M
        mini = F
    else:
        maxi = F
        mini = M

    while (maxi != 1 or mini != 1) and (maxi > 0 and mini > 0):

        if mini > maxi:
            hold = copy.deepcopy(maxi)
            maxi = mini
            mini = hold

        magic_number = maxi % mini

        if magic_number == 0 or magic_number == mini:
            if maxi == 1 and mini == 1:
                return str(cycles)
            else:
                maxi -= mini
                cycles += 1
        else:
            cycles += int((maxi - magic_number) / mini)
            maxi = magic_number

#         print(maxi, mini)

    if maxi == 0 or mini == 0:
        return 'impossible'
    else:
        return str(cycles)
        
print(answer(M,F))