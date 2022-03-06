#2.5.3

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

#Тест на примере:
text = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
k = 5
profile = ["0.2 0.2 0.3 0.2 0.3", "0.4 0.3 0.1 0.5 0.1", "0.3 0.3 0.5 0.2 0.4", "0.1 0.2 0.1 0.1 0.2"]
print(ProfileMostProbableKmer(text, k, profile))

#Тест на датасете:
f = open('dataset_2.5.3.txt', 'rt')
input = f.read().split("\n")
text = input[0]
k = input[1]
profile = []
for i in range(2, 6):
    profile.append(input[i])
print(ProfileMostProbableKmer(text, int(k), profile)) 
