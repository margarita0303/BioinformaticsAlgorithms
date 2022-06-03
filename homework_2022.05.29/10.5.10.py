def ProbabilityOfAnOutcomeGivenAHiddenPathProblem(x, path, dict_):
    ans = 1
    for i in range(len(x)):
        ans = ans * dict_[path[i]][x[i]]
    return ans
    
if __name__ == '__main__':
    f = open('input.txt', 'r')
    data = f.read().split()
    x = data[0]
    path = data[6]
    dict_ = {}
    dict_['A'] = {'x':float(data[-7]), 'y':float(data[-6]), 'z':float(data[-5])}
    dict_['B'] = {'x':float(data[-3]), 'y':float(data[-2]), 'z':float(data[-1])}
    ans = ProbabilityOfAnOutcomeGivenAHiddenPathProblem(x, path, dict_) 
    print(ans)
