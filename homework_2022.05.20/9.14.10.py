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
        
def CountSymbols(checkPoints, i, LastColumn, symbol):
    vals = [x for x in checkPoints.keys() if x <= i]
    nearest = min(vals, key=lambda x: abs(x - i))
    amount = checkPoints[nearest][symbol] + LastColumn[nearest:i].count(symbol)
    return amount

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


def patternToSeeds(pattern, d):
    minsize = len(pattern) // (d + 1)
    cutPoints = list(range(0, len(pattern) - minsize + 1, minsize))
    cutPoints.append(len(pattern))
    seeds = []
    offsets = []
    for i in range(1, len(cutPoints)):
        seeds.append(pattern[cutPoints[i - 1]: cutPoints[i]])
        offsets.append(cutPoints[i - 1])
    return seeds, offsets


def findPositions(seed, FirstOccurrence, bwt, checkPoints, partialSuffixArray):
    positions = []
    top, bottom = MultiplePatternMatchingCurrent(FirstOccurrence, bwt, seed, checkPoints)
    if top:
        for idx in range(top, bottom + 1):
            to_add = 0
            while idx not in partialSuffixArray.keys():
                idx = FirstOccurrence[bwt[idx]] + CountSymbols(checkPoints, idx, bwt, bwt[idx])
                to_add += 1
            positions.append(partialSuffixArray[idx] + to_add)
    return positions


def MultiplePatternMatching(Text, pattern_list, d, C):
    bwt = BurrowsWheeler(Text + '$')
    FirstOccurrence = {}
    for idx, symbol in enumerate(sorted(bwt)):
        if symbol not in FirstOccurrence.keys():
            FirstOccurrence[symbol] = idx
    checkPoints = CheckPoints(bwt, C)
    partialSuffixArray = MakePartialSuffixArray(Text + '$', C)
    positions_dict = {}
    for pattern in pattern_list:
        seeds, offsets = patternToSeeds(pattern, d)
        pattern_pos_list = set()
        for candidate_seed, offset in zip(seeds, offsets):
            seed_pos_list = findPositions(candidate_seed, FirstOccurrence, bwt, checkPoints, partialSuffixArray)
            for candidate_pos in seed_pos_list:
                pattern_position = candidate_pos - offset
                if pattern_position >= 0 and pattern_position + len(pattern) <= len(Text):
                    approximate_match_flag = True
                    num_mismatch = 0
                    for idx, symbol in enumerate(pattern):
                        if symbol != Text[pattern_position + idx]:
                            num_mismatch += 1
                            if num_mismatch > d:
                                approximate_match_flag = False
                                break
                    if approximate_match_flag:
                        pattern_pos_list.add(pattern_position)
        positions_dict[pattern] = sorted(pattern_pos_list)
    return positions_dict


if __name__ == "__main__":
    f = open('input.txt', 'r')
    data = f.read().strip().split('\n')
    Text = data[0]
    pattern_list = []
    tmp = data[1].split(' ')
    for i in range(0, len(tmp)):
        pattern_list.append(tmp[i])
    d = int(data[2])

    positions_dict = MultiplePatternMatching(Text, pattern_list, d, C=100)
    f2 = open('output.txt', 'w')
    for key in pattern_list:
        if len(positions_dict[key]) == 0:
            f2.write(key + ':\n')
            print(key + ':')
        else:
            f2.write(key + ': ' + ' '.join(str(pos) for pos in positions_dict[key]) + '\n')
            print(key + ': ' + ' '.join(str(pos) for pos in positions_dict[key]))
    f2.close()
    f.close() 
