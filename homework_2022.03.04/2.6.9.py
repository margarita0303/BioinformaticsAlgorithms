#2.6.9
 
def AllKmersForString(text, k):
    kmers = set()
    for i in range(0, len(text) - k + 1):
        kmers.add(text[i:i+k])
    return kmers
 
def IndexOfNucleotide():
    indexOfNucleotide = {}
    indexOfNucleotide['A'] = 0
    indexOfNucleotide['C'] = 1
    indexOfNucleotide['G'] = 2
    indexOfNucleotide['T'] = 3
    return indexOfNucleotide
 
def SimilarityToTheConsensus(pattern, profile):
    indexOfNucleotide = IndexOfNucleotide()
    similarity = 1
    for i in range(0, len(pattern)):
        symbol = pattern[i]
        similarity *= float(profile[indexOfNucleotide[symbol]].split(' ')[i])
    return similarity
 
def ProfileMostProbableKmer(text, k, profile):
    kmers = AllKmersForString(text, k)
    bestKmer = ""
    bestSimilarity = 0
    for kmer in kmers:
        similarity = SimilarityToTheConsensus(kmer, profile)
        if similarity > bestSimilarity:
            bestKmer = kmer 
            bestSimilarity = similarity
    return bestKmer
 
def HammingDistance(pattern1, pattern2):
    count = 0
    for s1, s2 in zip(pattern1, pattern2):
        if s1 != s2:
            count += 1
    return count
 
def CountSymbolInColumn(motifs, column, symbol):
    count = 0
    for i in range(0, len(motifs)):
        motif = motifs[i]
        if motif[column] == symbol:
            count += 1
    return count
 
def MakeProfile(motifs):
    profile = []
    lenOfMotif = len(motifs[0])
    numberOfMotifs = len(motifs)
    for i in "ACGT":
        stringInProfile = str(CountSymbolInColumn(motifs, 0, i)/numberOfMotifs)
        for j in range(1, lenOfMotif):
            stringInProfile = stringInProfile + " " + str(CountSymbolInColumn(motifs, j, i)/numberOfMotifs)
        profile.append(stringInProfile)
    return profile
 
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
 
def FirstKmers(Dna, k):
    kmers = []
    for string in Dna:
        kmers.append(string[0:k])
    return kmers
 
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
    
        
def GreedyMotifSearch(Dna, k, t):
    bestMotifs = FirstKmers(Dna, k)
    kmersForFirstString = AllKmersForString(Dna[0], k)
    for motif in kmersForFirstString:
        motifs = []
        motifs.append(motif)
        for i in range(1, t):
            profile = MakeProfileWithLaplaceRule(motifs)
            motifs.append(ProfileMostProbableKmer(Dna[i], k, profile))
        if ScoreOfMotifs(motifs) <= ScoreOfMotifs(bestMotifs):
            bestMotifs = motifs
    bestMotifsAsString = ""
    for motif in bestMotifs:
        bestMotifsAsString += (motif + " ") 
    return bestMotifsAsString
 
#Тест из примера:
k = 3
t = 5
Dna = ["GGCGTTCAGGCA", "AAGAATCAGTCA", "CAAGGAGTTCGC", "CACGTCAATCAC", "CAATAATATTCG"]
print(GreedyMotifSearch(Dna, k, t))
 
#Тест на датасете:
f = open('dataset_2.6.9.txt', 'rt')
input = f.read().split("\n")
k = input[0]
t = input[1]
Dna = input[2].split(" ")
print(GreedyMotifSearch(Dna, int(k), int(t))) 
