#2.9.4

import random
from random import randint
import numpy as np

def HammingDistance(pattern1, pattern2):
    count = 0
    for s1, s2 in zip(pattern1, pattern2):
        if s1 != s2:
            count += 1
    return count

def IndexOfNucleotide():
    indexOfNucleotide = {}
    indexOfNucleotide['A'] = 0
    indexOfNucleotide['C'] = 1
    indexOfNucleotide['G'] = 2
    indexOfNucleotide['T'] = 3
    return indexOfNucleotide

def CountSymbolInColumn(motifs, column, symbol):
    count = 0
    for i in range(0, len(motifs)):
        motif = motifs[i]
        if motif[column] == symbol:
            count += 1
    return count

def Consensus(motifs):
    lenOfMotif = len(motifs[0])
    consensus = ""
    for i in range(0, lenOfMotif):
        newSymbol = "A"
        maxCount = 0
        if CountSymbolInColumn(motifs, i, 'A') > maxCount:
            newSymbol = "A"
            maxCount = CountSymbolInColumn(motifs, i, 'A')
        if CountSymbolInColumn(motifs, i, 'C') > maxCount:
            newSymbol = "C"
            maxCount = CountSymbolInColumn(motifs, i, 'C')
        if CountSymbolInColumn(motifs, i, 'G') > maxCount:
            newSymbol = "G"
            maxCount = CountSymbolInColumn(motifs, i, 'G')
        if CountSymbolInColumn(motifs, i, 'T') > maxCount:
            newSymbol = "T"
            maxCount = CountSymbolInColumn(motifs, i, 'T')
        consensus += newSymbol
    return consensus

def AllKmersForString(text, k):
    kmers = set()
    for i in range(0, len(text) - k + 1):
        kmers.add(text[i:i+k])
    return kmers

def RandomMotifs(Dna, k):
    motifs = []
    for text in Dna:
        randomIndex = randint(0, len(text) - k)
        motifs.append(text[randomIndex:randomIndex + k])
    return motifs

def CountSymbolInColumn(motifs, column, symbol):
    count = 0
    for i in range(0, len(motifs)):
        motif = motifs[i]
        if motif[column] == symbol:
            count += 1
    return count

def MakeProfileWithLaplaceRule(motifs):
    profile = []
    lenOfMotif = len(motifs[0])
    numberOfMotifs = len(motifs)
    for i in "ACGT":
        stringInProfile = str((CountSymbolInColumn(motifs, 0, i) + 1)/(numberOfMotifs + 4))
        for j in range(1, lenOfMotif):
            stringInProfile = stringInProfile + " " + str((CountSymbolInColumn(motifs, j, i) + 1)/(numberOfMotifs+4))
        profile.append(stringInProfile)
    return profile

def CountProbability(kmer, profile, k):
    count = 1
    for i in range(0, k):
        symbol = kmer[i]
        indexOfNucleotide = IndexOfNucleotide()
        count *= float(profile[indexOfNucleotide[symbol]].split(' ')[i])
    return count

def Random(text, k, profile):
    probs = []
    for i in range(len(text) - k + 1):
        pattern = text[i : i + k]
        probs.append(CountProbability(pattern, profile, k))
    i = np.random.choice(len(probs), p = np.array(probs) / np.sum(probs))
    return i


def ScoreOfMotifs(motifs):
    consensus = Consensus(motifs)
    score = 0
    for motif in motifs:
        score += HammingDistance(motif, consensus)
    return score

def GibbsSampler(Dna, k, t, N):
    motifs = RandomMotifs(Dna, k)
    bestMotifs = motifs
    for j in range(0, N):
        i = randint(0, t - 1)
        profile = MakeProfileWithLaplaceRule(motifs)
        index = Random(Dna[i], k, profile)
        motifs[i - 1] = Dna[i][index:index+k]
        if ScoreOfMotifs(motifs) < ScoreOfMotifs(bestMotifs):
            bestMotifs = motifs
    return bestMotifs

def FindBestMotifsUsingMonteCarlo(Dna, k, t, N):
    bestMotifs = RandomMotifs(Dna, k)
    for i in range(20):
        motifs = GibbsSampler(Dna, k, t, N)
        if ScoreOfMotifs(motifs) < ScoreOfMotifs(bestMotifs):
            bestMotifs = motifs
    #print(ScoreOfMotifs(bestMotifs))
    return bestMotifs

#Тест из примера:
k = 8
t = 5
N = 100
DnaString = "CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG TAGTACCGAGACCGAAAGAAGTATACAGGCGT TAGATCAAGTTTCAGGTGCACGTCGGTGAACC AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
Dna = DnaString.split(" ")
print(*FindBestMotifsUsingMonteCarlo(Dna, k, t, N))

#Тест на датасете:
f = open('dataset_2.9.4.txt', 'rt')
input = f.read().split("\n")
k = input[0]
t = input[1]
N = input[2]
Dna = input[3].split(" ")
print(*FindBestMotifsUsingMonteCarlo(Dna, int(k), int(t), int(N))) 
