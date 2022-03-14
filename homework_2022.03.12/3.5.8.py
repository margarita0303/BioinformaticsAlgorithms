# Task 3.5.8
def DeBruijnGraph(kmers):
    k = len(kmers[0])
    uniqueKMinusOneKmers = set()
    deBruijnGraph = {}
    for kmer in kmers:
        prefix = kmer[0:k-1]
        suffix = kmer[1:k]
        if prefix not in deBruijnGraph:
            deBruijnGraph[prefix] = suffix
        else:
            deBruijnGraph[prefix] = deBruijnGraph[prefix] + ' ' + suffix
    for pattern in deBruijnGraph:
        if deBruijnGraph[pattern] != '':
            print(f'{pattern}: {deBruijnGraph[pattern]}')
        
#Тест из примера:
kmers = ["GAGG", "CAGG", "GGGG", "GGGA", "CAGG", "AGGG", "GGAG"]
print(DeBruijnGraph(kmers))

# Тест на датасете:
kmers = "".join(open('dataset_3.5.8.txt')).split()
print(DeBruijnGraph(kmers)) 
