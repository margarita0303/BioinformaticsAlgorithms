def BetterBWMatchingTmp(text, pattern):
    firstInput = {}
    for i, symb in enumerate(sorted(text)):
        if symb not in firstInput.keys():
            firstInput[symb] = i 
    start = 0
    end = len(text) - 1
    while start <= end:
        if len(pattern) != 0:
            symb = pattern[-1]
            pattern = pattern[:-1]
            if symb in text[start:end+1]:
                start = firstInput[symb] + text[:start].count(symb)
                end = firstInput[symb] + text[:(end + 1)].count(symb)-1
            else:
                return 0
        else:
            return end-start+1
        
def BetterBWMatching(text, patterns):
    result = []
    for pattern in patterns:
        result.append(BetterBWMatchingTmp(text, pattern))
    resultAsString = ' '.join(str(num) for num in result)
    return resultAsString

if __name__ == "__main__":
    f = open('input.txt', 'r')
    data = f.read().strip().split('\n')
    text = data[0]
    patterns = data[1].split(' ')
    print(BetterBWMatching(text, patterns)) 
