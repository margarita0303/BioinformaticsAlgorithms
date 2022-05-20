def MultiplePatternMatchingCurrent(FirstOccurrence, LastColumn, pattern, checkPoints):
    top = 0
    bottom = len(LastColumn) - 1
    while top <= bottom:
        if len(pattern) != 0:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if symbol in LastColumn[top: bottom + 1]:
                top = FirstOccurrence[symbol] + CountSymbols(checkPoints, top, LastColumn, symbol)
                bottom = FirstOccurrence[symbol] + CountSymbols(checkPoints, bottom + 1, LastColumn, symbol) - 1
            else:
                return False, False
        else:
            return top, bottom

def BurrowsWheeler(text):
    rotations = sorted([text[i:] + text[:i] for i in range(len(text))])
    return ''.join([rot[-1] for rot in rotations])

def CheckPoints(text, step):
    symbols = list(set(text))
    checkpoints = {}
    for i in range(0, len(text), step):
        checkpoints[i] = {}
        for symbol in symbols:
            checkpoints[i][symbol] = text[:i].count(symbol)
    return checkpoints

def MakePartialSuffixArray(text, K):
    suffixes = []
    suffixArray = []
    for i in range(len(text)):
        suffixes.append(text[i:])
        suffixArray.append(i)
    suffixArray = [x for _, x in sorted(zip(suffixes, suffixArray), key=lambda pair: pair[0])]
    return {i: x for i, x in enumerate(suffixArray) if x % K == 0}

def CountSymbols(checkPoints, i, LastColumn, symbol):
    vals = [x for x in checkPoints.keys() if x <= i]
    nearest = min(vals, key=lambda x: abs(x - i))
    amount = checkPoints[nearest][symbol] + LastColumn[nearest:i].count(symbol)
    return amount

def MultiplePatternMatching(Text, patterns, C):
    bwt = BurrowsWheeler(Text + '$')
    FirstOccurrence = {}
    for i, symbol in enumerate(sorted(bwt)):
        if symbol not in FirstOccurrence.keys():
            FirstOccurrence[symbol] = i
    checkPoints = CheckPoints(bwt, C)
    partialSuffixArray = MakePartialSuffixArray(Text + '$', C)
    positions_dict = {}
    for pattern in pattern_list:
        tmp_positions_list = []
        top, bottom = MultiplePatternMatchingCurrent(FirstOccurrence, bwt, pattern, checkPoints)
        if top:
            for idx in range(top, bottom + 1):
                to_add = 0
                while idx not in partialSuffixArray.keys():
                    idx = FirstOccurrence[bwt[idx]] + CountSymbols(checkPoints, idx, bwt, bwt[idx])
                    to_add += 1
                tmp_positions_list.append(partialSuffixArray[idx] + to_add)
        positions_dict[pattern] = sorted(list(set(tmp_positions_list)))
    return positions_dict


if __name__ == "__main__":
    f = open('input.txt', 'r')
    data = f.read().strip().split('\n')
    Text = data[0]
    pattern_list = []
    tmp = data[1].split(' ')
    for i in range(0, len(tmp)):
        pattern_list.append(tmp[i])

    #Text = "AATCGGGTTCAATCGGGGT"
    #pattern_list = ['ATCG', 'GGGT']
    
    #Text = "aaa"
    #pattern_list = ['aaa']

    positions_dict = MultiplePatternMatching(Text, pattern_list, C=100)

    f2 = open('output.txt', 'w')
    for key in pattern_list:
        if len(positions_dict[key]) == 0:
            f2.write(key + ':\n')
            #print(key + ':')
        else:
            f2.write(key + ': ' + ' '.join(str(pos) for pos in positions_dict[key]) + '\n')
            #print(key + ': ' + ' '.join(str(pos) for pos in positions_dict[key]))
    f2.close()
    f.close()
