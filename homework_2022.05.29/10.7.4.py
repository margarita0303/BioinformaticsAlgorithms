def OutcomeLikelihood(x, transition, emission):
    forward = [[0 for i in range(len(transition))] for j in range(len(x))]
    for i in range(len(transition)):
        forward[0][i] = emission[i][x[0]] / len(transition)
    for i in range(1, len(x)):
        for k in range(len(transition)):
            newArr = [forward[i - 1][j] * transition[j][k] * emission[k][x[i]] for j in range(len(transition))]
            forward[i][k] = sum(newArr)
    ans = sum(forward[len(x) - 1])
    return ans

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
    transitionDict = {}
    for i in range(n):
        transitionDict[i] = {}
        for k in range(n):
            transitionDict[i][k] = float(data[dashes[2] + n + 2 + i * (n + 1) + k])
    emission = {}
    for i in range(n):
        emission[i] = {}
        for k in range(m):
            emission[i][alphabet[k]] = float(data[dashes[3]+m + 2 + i * (m+1)+k])
    ans = OutcomeLikelihood(x, transitionDict, emission) 
    print(ans)
