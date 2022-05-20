def CountSymbols(transformed):
    amount = {}
    symbolsWithAmount = []
    for char in transformed:
        if char not in amount.keys():
            amount[char] = 1
        else:
            amount[char] += 1
        symbolsWithAmount.append(char + str(amount[char]))
    ans = ['$1']
    return symbolsWithAmount, ans

def ReconstructFromBurrowsWheeler(transformed):
    symbolsWithAmount, ans = CountSymbols(transformed)
    firstCol = sorted(symbolsWithAmount, key=lambda x: x[0])
    for i in range(1, len(transformed)):
        prev = ans[i-1]
        for i, char in enumerate(symbolsWithAmount):
            if char == prev:
                idx = i
                break
        ans.append(firstCol[idx])
    originalText = ''
    for i in range(1, len(ans)):
        originalText = originalText + ''.join(i for i in ans[i] if not i.isdigit())
    originalText += '$'
    return originalText


if __name__ == "__main__":
    f = open('input.txt', 'r')
    data = f.read().strip().split('\n')
    transformed = data[0]
#     transformed = "TTCCTAACG$A"
    print(ReconstructFromBurrowsWheeler(transformed)) 
