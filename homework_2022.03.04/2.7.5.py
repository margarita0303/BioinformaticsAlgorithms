#2.7.5

from random import randint

def HammingDistance(pattern1, pattern2):
    count = 0
    for s1, s2 in zip(pattern1, pattern2):
        if s1 != s2:
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
 
def ScoreOfMotifs(motifs):
    consensus = Consensus(motifs)
    score = 0
    for motif in motifs:
        score += HammingDistance(motif, consensus)
    return score

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

def RandomMotifs(Dna, k):
    motifs = []
    for text in Dna:
        randomIndex = randint(0, len(text) - k)
        motifs.append(text[randomIndex:randomIndex + k])
    return motifs

def IndexOfNucleotide():
    indexOfNucleotide = {}
    indexOfNucleotide['A'] = 0
    indexOfNucleotide['C'] = 1
    indexOfNucleotide['G'] = 2
    indexOfNucleotide['T'] = 3
    return indexOfNucleotide

def CountProbability(kmer, profile, k):
    count = 1
    for i in range(0, k):
        symbol = kmer[i]
        indexOfNucleotide = IndexOfNucleotide()
        count *= float(profile[indexOfNucleotide[symbol]].split(' ')[i])
    return count
    

def MostLikelyMotifs(profile, Dna, k):
    motifs = []
    for text in Dna:
        bestProbability = 0
        bestMotif = ""
        for i in range(0, len(text) - k + 1):
            if bestProbability < CountProbability(text[i:i+k], profile, k):
                bestProbability = CountProbability(text[i:i+k], profile, k)
                bestMotif = text[i:i+k]
        motifs.append(bestMotif)
    return motifs

def RandomizedMotifSearch(Dna, k, t):
    motifs = RandomMotifs(Dna, k)
    bestMotifs = motifs
    while True:
        profile = MakeProfileWithLaplaceRule(motifs)
        motifs = MostLikelyMotifs(profile, Dna, k)
        if ScoreOfMotifs(motifs) < ScoreOfMotifs(bestMotifs):
            bestMotifs = motifs
        else:
            return bestMotifs
        
def FindBestMotifsUsingMonteCarlo(Dna, k, t):
    bestMotifs = RandomizedMotifSearch(Dna, k, t)
    for i in range(400):
        motifs = RandomizedMotifSearch(Dna, k, t)
        if ScoreOfMotifs(motifs) < ScoreOfMotifs(bestMotifs):
            bestMotifs = motifs
    #print(ScoreOfMotifs(bestMotifs))
    return bestMotifs

#Иногда выдает не такой ответ, как в примере, но чаще - такой.
#Как я понимаю, алгоритм рандомизированный, поэтому такое может происходить. 
#Кроме того, могут встречаться наборы с одинаковым score.
#Если выставить число итераций больше - то ответы, отличающиеся от ответа в примере встречаются реже (лично мне ни разу, сколько я запускала).
        
#Тест из примера:
k = 8
t = 5
Dna = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA", "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
       "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]
        
print(*FindBestMotifsUsingMonteCarlo(Dna, k, t)) 

#Тест на датасете:
f = open('dataset_2.7.5.txt', 'rt')
input = f.read().split("\n")
k = input[0]
t = input[1]
Dna = input[2].split(" ")
print(*FindBestMotifsUsingMonteCarlo(Dna, int(k), int(t)))

