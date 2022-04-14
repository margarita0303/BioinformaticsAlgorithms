def FindSpecialPosition(P, start):
    needToFind = start + 1
    for i in range(start, len(P)):
        if P[i] == (('+') + str(needToFind)) or P[i] == (('-') + str(needToFind)):
            return i
    return 0

def GreedySorting(P):
    approxReversalDistance = 0
    for k in range(0, len(P)):
        if P[k] == '-' + str(k + 1):
            P[k] = '+' + str(k + 1)
            approxReversalDistance += 1
            print(*P)
        if P[k] != '+' + str(k + 1):
            endPosition = FindSpecialPosition(P, k)
            startPosition = k
            syntenyBlock = P[startPosition:endPosition+1]
            syntenyBlock.reverse()
            for j in range(0, len(syntenyBlock)):
                if syntenyBlock[j][0] == '+':
                    syntenyBlock[j] = '-' + syntenyBlock[j][1:len(syntenyBlock[j])]
                else:
                    syntenyBlock[j] = '+' + syntenyBlock[j][1:len(syntenyBlock[j])]
            P = P[0:startPosition] + syntenyBlock + P[endPosition+1:len(P)]
            approxReversalDistance += 1
            print(*P)
        if P[k] == '-' + str(k + 1):
            P[k] = '+' + str(k + 1)
            approxReversalDistance += 1
            print(*P)
#     print(approxReversalDistance)
    return

P = ["-3", "+4", "+1", "+5", "+2"]
GreedySorting(P)


f = open('task1.txt', 'rt')
P = f.read().rstrip('\n').split(" ")
GreedySorting(P)
