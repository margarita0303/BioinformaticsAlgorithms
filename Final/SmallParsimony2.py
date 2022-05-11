# https://github.com/margarita0303/BioinformaticsAlgorithms/blob/main/homework_2022.04.22/7.9.10.py

# удалена куча кода, связанная с построением дерева, оставлен только код для нахождения maxParsimony

def FindRoot(edges, nodes):
    children = [child for parent, child in edges]
    root = nodes[0]
    i = 1
    while root in children:
        root = nodes[i]
        i += 1
    return root

# эта функция дерево больше не строит, но все еще возвращает ParsimonyScore (только уже max), решила не переименовывать
def ConstructTree(edges, countedScores, scoreTable, dictNucleotides):
    nodes = [item for sublist in edges for item in sublist]
    nodes = list(set(nodes))
    root = FindRoot(edges, nodes)
    maxParsimonyScore = 0
    for pos, scores in countedScores[root].items():
        # заменяю min на max
        maxParsimonyScore += max(scores.values())

    return maxParsimonyScore

def IsLeaf(s):
    try:
        int(s)
        return False
    except ValueError:
        return True
    
def LenOfDNAStrings(nodes):
    length = 0
    for node in nodes:
        if IsLeaf(node):
            length = len(node)
            return length
    return 0

def NextNodeToInitializeZeros(alreadyСounted):
    zeroNodes = [node for node, isCounted in alreadyСounted.items() if isCounted == 0]
    for node in zeroNodes:
        children = [child for parent, child in edges if parent == node]
        if all([alreadyСounted[child] == 1 for child in children]):
            return node, children
        
def InitializeLeafs(S, nodes, alreadyСounted, lenString, Nucleotides):
    for v in nodes:
        S[v] = {}
        alreadyСounted[v] = 0
        if IsLeaf(v):
            alreadyСounted[v] = 1
            for pos in range(lenString):
                S[v][pos] = {}
                symbol = v[pos]
                for nucleotide in Nucleotides:
                    if symbol == nucleotide:
                        S[v][pos][nucleotide] = 0
                    else:
                        # заменяем 1e9 на -1e9, так как ищем максимум
                        S[v][pos][nucleotide] = -1e9
    return S, alreadyСounted
    
def SmallParsimony(edges, Nucleotides, scoreTable, dictNucleotides):
    alreadyСounted = {}
    S = {}
    nodes = [node for edge in edges for node in edge]
    nodes = list(set(nodes))
    lenString = LenOfDNAStrings(nodes)
    S, alreadyСounted = InitializeLeafs(S, nodes, alreadyСounted, lenString, Nucleotides)
                        
    while 0 in list(alreadyСounted.values()):
        v, children = NextNodeToInitializeZeros(alreadyСounted)
        alreadyСounted[v] = 1
        S[v] = {}
        for pos in range(lenString):
            S[v][pos] = {}
            for nucleotide in Nucleotides:
                possibleScoresDaughter = []
                daughterScore = 0
                for symbol, score in S[children[0]][pos].items():
                    # пересчитываем score с помощью таблицы, а не +0 / +1
                    possibleScoresDaughter.append(score + scoreTable[dictNucleotides[symbol]][dictNucleotides[nucleotide]])
                possibleScoresSon = []
                sonScore = 0
                for symbol, score in S[children[1]][pos].items():
                    # пересчитываем score с помощью таблицы, а не +0 / +1
                    possibleScoresSon.append(score + scoreTable[dictNucleotides[symbol]][dictNucleotides[nucleotide]])
                # замена min на max
                S[v][pos][nucleotide] = max(possibleScoresDaughter) + max(possibleScoresSon)
    return S


if __name__ == "__main__":
    
    #f = open('input.txt', 'r')
    #lines = f.read().strip().split("\n")
    #num_leaves = int(lines[0])
    #edges = []
    
    # считывание BLOSUM62
    f2 = open("BLOSUM62.txt")
    lines2 = f2.read().strip().split("\n")
    Nucleotides = lines2[0].split(' ')
    Nucleotides = [n for n in Nucleotides if n != '']
    dictNucleotides = {}
    for i in range(len(Nucleotides)):
        dictNucleotides[Nucleotides[i]] = i
    scoreTable = lines2[1:]
    for i in range(len(scoreTable)):
        newLine = scoreTable[i].split(' ')
        newLine = [item for item in newLine if item != '']
        scoreTable[i] = newLine[1:len(newLine)]
    scoreTable = [[int(i) for i in line] for line in scoreTable]
    
    
    #for row in lines[1:]:
        #temp = row.rstrip().split('->')
        #edges.append(temp)
        
    num_leaves = 4
    edges = [["4", "A"], ["4", "A"], ["5", "C"], ["5", "C"], ["6", "4"], ["6", "5"]]
    # должно быть 36

    countedScores = SmallParsimony(edges, Nucleotides, scoreTable, dictNucleotides)
    maxParsimonyScore = ConstructTree(edges, countedScores, scoreTable, dictNucleotides)

    print(maxParsimonyScore)




