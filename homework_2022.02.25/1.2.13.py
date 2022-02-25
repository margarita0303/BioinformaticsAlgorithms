import numpy as np

def FrequencyTable(text, k):
    freqDict = {}
    for i in range(0, len(text) -k):
        pattern = text[i:i+k]
        if pattern in freqDict:
            freqDict[pattern] += 1
        else:
            freqDict[pattern] = 1
    return freqDict

def MaxValueInDict(dict):
    return max(dict.values())

def BetterFrequentWords(text, k):
    frequentPatterns = []
    freqDict = FrequencyTable(text, k)
    maxLen = MaxValueInDict(freqDict)
    for key in freqDict:
        if freqDict[key] == maxLen:
            frequentPatterns.append(key)
    return frequentPatterns
    
    
f = open('dataset_1.2.13.txt', 'rt')
input = f.read().split("\n")
text = input[0]
k = input[1]

print("Тест из примера:")
print(BetterFrequentWords("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4))
print("Тест на датасете:")
print(BetterFrequentWords(text, int(k)))
