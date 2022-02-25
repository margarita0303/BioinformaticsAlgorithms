def ComplementOfDNA(pattern):
    reversedPattern = pattern[::-1]
    complement = ""
    for i in reversedPattern:
        if i == 'A':
            complement += 'T'
        elif i == 'T':
            complement += 'A'
        elif i == 'G':
            complement += 'C'
        elif i == 'C':
            complement += 'G'
    return complement

def HammingDistance(pattern1, pattern2):
    count = 0
    for s1, s2 in zip(pattern1, pattern2):
        if s1 != s2:
            count += 1
    return count

def ApproximatePatternCount(text, pattern, d):
        count = 0
        for i in range (0, len(text) - len(pattern) + 1):
            tmpPattern = text[i:i+len(pattern)]
            if HammingDistance(pattern, tmpPattern) <= d:
                count += 1
        return count

def GetKMers(text, k):
    reversedText = ComplementOfDNA(text)
    kmers = []
    for i in range(0, len(text) - k):
        kmers.append(text[i:i+k])
        kmers.append(reversedText[i:i+k])
    return kmers
        
def FrequentWordsWithMissmatches(text, k, d):
    ans = ""
    dict = {}
    kmers = GetKMers(text, k)
    for kmer in kmers:
        matchCount = ApproximatePatternCount(text, kmer, d)
        reversedMatchCount = ApproximatePatternCount(text, ComplementOfDNA(kmer), d)
        dict[kmer] = matchCount + reversedMatchCount
    maxCount = max(dict.values())
    for pattern in dict:
        if dict[pattern] == maxCount:
            ans = ans + " " + pattern
    return ans
        
        
f = open('dataset9.txt', 'rt')
input = f.read().split("\n")
text = input[0]
k = input[1]
d = input[2]


print("Тест из примера:")
print(FrequentWordsWithMissmatches("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1))
print("Тест на датасете:")
print(FrequentWordsWithMissmatches(text, int(k), int(d))) 
