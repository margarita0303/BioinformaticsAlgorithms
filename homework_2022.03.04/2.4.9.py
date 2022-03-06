#2.4.9

import math

def HammingDistance(pattern1, pattern2):
    count = 0
    for s1, s2 in zip(pattern1, pattern2):
        if s1 != s2:
            count += 1
    return count

def AllKmersForString(text, k):
    kmers = set()
    for i in range(0, len(text) - k):
        kmers.add(text[i:i+k])
    return kmers

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

def Nucleotides():
    return ['A', 'C', 'G', 'T']

def ScoreOfPattern(pattern, Dna):
    score = 0
    for string in Dna:
        scoreForString = math.inf
        allKmersForString = AllKmersForString(string, len(pattern))
        for kmer in allKmersForString:
            if HammingDistance(pattern, kmer) < scoreForString:
                scoreForString = HammingDistance(pattern, kmer)
        score += scoreForString
    return score
                        

def MedianString(Dna, k):
    distance = math.inf
    allKmerPatterns = Neighbors('A'*k, k)
    median = ""
    for pattern in allKmerPatterns:
        if distance > ScoreOfPattern(pattern, Dna):
            distance = ScoreOfPattern(pattern, Dna)
            median = pattern
    return median

#Тест на примере:
print(MedianString(["AAATTGACGCAT", "GACGACCACGTT", "CGTCAGCGCCTG", "GCTGAGCACCGG", "AGTTCGGGACAG"], 3))

#Тест на датасете:
f = open('dataset_2.4.9.txt', 'rt')
input = f.read().split("\n")
k = input[0]
Dna = input[1].split(" ")

print(MedianString(Dna, int(k))) 
