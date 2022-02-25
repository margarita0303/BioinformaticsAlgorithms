def FrequencyTable(text, k):
    freqDict = {}
    for i in range(0, len(text) -k):
        pattern = text[i:i+k]
        if pattern in freqDict:
            freqDict[pattern] += 1
        else:
            freqDict[pattern] = 1
    return freqDict

def FindClumps(text, k, L, t):
    patterns = []
    if (L > len(text)):
        return
    for i in range(0, len(text) - L):
        window = text[i:i+L]
        freqDict = FrequencyTable(window, k)
        for key in freqDict:
            if freqDict[key] >= t:
                patterns.append(key)
    patterns = list(set(patterns))
    patternsAsString = ""
    for i in patterns:
        patternsAsString = patternsAsString + " " + i
    return patternsAsString

f = open('dataset5.txt', 'rt')
input = f.read().split("\n")
text = input[0]
k = input[1]
L = input[2]
t = input[3]


print("Тест из примера:")
print(FindClumps("CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA", 5, 50, 4))
print("Тест на датасете:")
print(FindClumps(text, int(k), int(L), int(t)))
