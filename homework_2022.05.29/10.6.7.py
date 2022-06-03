from math import log
from numpy import argmax

def Decoding(x, transionLog, emissionLog, stateDict):
    s = [[0 for i in range(len(transionLog))] for j in range(len(x))]
    back = [[0 for i in range(len(transionLog))] for j in range(len(x))]
    
    for k in range(len(transionLog)):
        s[0][k] = log(1 / len(transionLog)) + emissionLog[k][x[0]]
    for i in range(1, len(x)):
        for k in range(len(transionLog)):
            currS = []
            for j in range(len(transionLog)):
                currS.append(s[i-1][j] + transionLog[j][k] + emissionLog[k][x[i]])
            back[i][k] = argmax(currS)
            s[i][k] = currS[argmax(currS)]
    currState = argmax(s[len(x)-1])
    stateList = [currState]
    for i in range(len(x) - 1, 0, -1):
        currState = back[i][currState]
        stateList.insert(0, currState)
    path = ''.join([stateDict[state] for state in stateList])
    return path

if __name__ == '__main__':
    f = open('input.txt', 'r')
    data = f.read().split()
    x = data[0]
    dashes = []
    for i in range(len(data)):
        if data[i] == '--------':
            dashes.append(i)
    alphabet = []
    for i in range(dashes[0] + 1, dashes[1]):
        alphabet.append(data[i])
    states = []
    for i in range(dashes[1] + 1, dashes[2]):
        states.append(data[i])
    n = len(states)
    m = len(alphabet)
    stateDict = {}
    for i in range(n):
        stateDict[i] = states[i]
    transitionLog = {}
    for i in range(n):
        transitionLog[i] = {}
        for k in range(n):
            transitionLog[i][k] = log(float(data[dashes[2] + n + 2 + i * (n + 1) + k]))
    emissionLog = {}
    for i in range(n):
        emissionLog[i] = {}
        for k in range(m):
            emissionLog[i][alphabet[k]] = log(float(data[dashes[3] + m + 2 + i * (m + 1) + k]))
    path = Decoding(x, transitionLog, emissionLog, stateDict)
    print(path)
    

