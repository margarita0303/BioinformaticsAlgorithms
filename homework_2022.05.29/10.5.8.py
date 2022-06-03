def ProbabilityOfAHiddenPathProblem(path, dict_):
    ans = 0.5
    for i in range(len(path) - 1):
        ans = ans * dict_[path[i]][path[i + 1]]
    return ans
    
if __name__ == '__main__':
    f = open('input.txt', 'r')
    data = f.read().split()
    path = data[0]
    dict_ = {'A':{'A':float(data[-5]), 'B':float(data[-4])}, 'B':{'A':float(data[-2]), 'B':float(data[-1])}}
    print(dict_)
    ans = ProbabilityOfAHiddenPathProblem(path, dict_) 
    print(ans)
