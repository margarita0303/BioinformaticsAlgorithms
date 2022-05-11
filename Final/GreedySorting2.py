# https://github.com/margarita0303/BioinformaticsAlgorithms/blob/main/homework_2022.04.15/6.4.4.py

def FindSpecialPosition2(P, nextVal, start):
    # nextVal - новый параметр, так как тут он уже не соответствует start + 1
    needToFind = int(nextVal[1:len(nextVal)])
    for i in range(start, len(P)):
        if P[i] == (('+') + str(needToFind)) or P[i] == (('-') + str(needToFind)):
            return i
    return 0


# все P заменяются на P1
def GreedySorting2(P1, P2):
    approxReversalDistance = 0
    for k in range(0, len(P1)):
        # поскольку знак должен быть теперь в соответствии с P2, а не "+", мы ищем, какой он должен быть
        sign = P2[k][0]
        reversedSign = ""
        if sign == '+':
            reversedSign = '-'
        else:
            reversedSign = '+'
        # меняем знак в соответствии со знаком в P2, а не на "+"
        if P1[k] == reversedSign + P2[k][1:len(P2[k])]:
            P1[k] = sign + P2[k][1:len(P2[k])]
            approxReversalDistance += 1
            print(*P1)
        # замена str(k + 1) на P2[k][1:len(P2[k])]
        if P1[k] != '+' + P2[k][1:len(P2[k])]:
            endPosition = FindSpecialPosition2(P1, P2[k], k)
            startPosition = k
            syntenyBlock = P1[startPosition:endPosition+1]
            syntenyBlock.reverse()
            for j in range(0, len(syntenyBlock)):
                if syntenyBlock[j][0] == '+':
                    syntenyBlock[j] = '-' + syntenyBlock[j][1:len(syntenyBlock[j])]
                else:
                    syntenyBlock[j] = '+' + syntenyBlock[j][1:len(syntenyBlock[j])]
            P1 = P1[0:startPosition] + syntenyBlock + P1[endPosition+1:len(P1)]
            approxReversalDistance += 1
            print(*P1)
        # поскольку знак должен быть теперь в соответствии с P2, а не "+", мы ищем, какой он должен быть
        sign = P2[k][0]
        reversedSign = ""
        if sign == '+':
            reversedSign = '-'
        else:
            reversedSign = '+'
        # меняем знак в соответствии со знаком в P2, а не на "+"
        if P1[k] == reversedSign + P2[k][1:len(P2[k])]:
            P1[k] = sign + P2[k][1:len(P2[k])]
            approxReversalDistance += 1
            print(*P1)
    return


P1 = ["-3", "+2", "+1", "+5", "+4"]
P2 = ["+2", "-1", "+5", "-4", "+3"]
GreedySorting2(P1, P2)






