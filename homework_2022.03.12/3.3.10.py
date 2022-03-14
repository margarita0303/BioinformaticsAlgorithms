def OverlapGraph(kmers):
    k = len(kmers[0])
    overlapGraph = {}
    for kmer1 in kmers:
        suffixKmer1 = kmer1[1:k]
        overlapGraph[kmer1] = ''
        setForNeighbours = set()
        for kmer2 in kmers:
            if kmer2 in setForNeighbours:
                continue
            else:
                setForNeighbours.add(kmer2)
            prefixKmer2 = kmer2[0:k - 1]
            if suffixKmer1 == prefixKmer2 and kmer1 != kmer2:
                overlapGraph[kmer1] += ' ' + kmer2
        if overlapGraph[kmer1] != '':
            print(f'{kmer1}:{overlapGraph[kmer1]}')
 
#Тест из примера:
kmers = ["ATGCG", "GCATG", "CATGC", "AGGCA", "GGCAT", "GGCAC"]
OverlapGraph(kmers)

# Тест на датасете:
kmers = "".join(open('dataset_3.3.10.txt')).split()
print(OverlapGraph(kmers)) 
