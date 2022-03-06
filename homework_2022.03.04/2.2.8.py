def AllKmers(Dna, k):
    kmers = set()
    for string in Dna:
        for i in range(0, len(string) - k):
            kmers.add(string[i:i+k])
    return kmers

def HammingDistance(pattern1, pattern2):
    count = 0
    for s1, s2 in zip(pattern1, pattern2):
        if s1 != s2:
            count += 1
    return count

def Nucleotides():
    return ['A', 'C', 'G', 'T']

def Neighbors(pattern, d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return Nucleotides()
    neighborhood = set()
    suffixNeighbors = Neighbors(pattern[1:len(pattern)], d)
    for text in suffixNeighbors:
        if HammingDistance(pattern[1:len(pattern)], text) < d:
            for nucleotide in Nucleotides():
                neighborhood.add(nucleotide + text)
        else:
            neighborhood.add(pattern[0] + text)
    return neighborhood

def PatternAppearsInEachDnaWithAtMostDMismatches(pattern, Dna, d):
    isAppears = []
    for j in range(0, len(Dna)):
        isAppears.append(False)
        string = Dna[j]
        for i in range(0, len(string) - len(pattern) + 1):
            if HammingDistance(string[i:i+len(pattern)], pattern) <= d:
                isAppears[j] = True
                break
    for j in isAppears:
        if j == False:
            return False
    return True
    

def MotifEnumeration(Dna, k, d):
    patterns = set()
    for kmer in AllKmers(Dna, k):
        for neighbor in Neighbors(kmer, d):
            if PatternAppearsInEachDnaWithAtMostDMismatches(neighbor, Dna, d):
                    patterns.add(neighbor)
    return patterns

#Тест на примере:
motifEnumeration = MotifEnumeration(["ATTTGGC", "TGCCTTA", "CGGTATC", "GAAAATT"], 3, 1)
motifEnumerationAsString = ""
for i in motifEnumeration:
    motifEnumerationAsString = motifEnumerationAsString + " " +  i
print(motifEnumerationAsString)

#Тест на датасете:
f = open('dataset_2.2.8.txt', 'rt')
input = f.read().split("\n")
k = input[0]
d = input[1]
Dna = input[2].split(" ")

motifEnumeration = MotifEnumeration(Dna, int(k), int(d))
motifEnumerationAsString = ""
for i in motifEnumeration:
    motifEnumerationAsString = motifEnumerationAsString + " " +  i
print(motifEnumerationAsString)
 
