Nucleotides = ['A', 'C', 'G', 'T']

def HammingDistance(p, q):
    return sum([p[i] != q[i] for i in range(len(p))])

def FindRoot(edges, nodes):
    children = [child for parent, child in edges]
    root = nodes[0]
    i = 1
    while root in children:
        root = nodes[i]
        i += 1
    return root

def CreateAdjacencyList(edges, marks):
    AdjacencyList = []
    for edge in edges:
        if not IsLeaf(edge[0]):
            node0 = marks[edge[0]]
        else:
            node0 = edge[0]
        if not IsLeaf(edge[1]):
            node1 = marks[edge[1]]
        else:
            node1 = edge[1]
        AdjacencyList.append([node0, node1, HammingDistance(node0, node1)])
        AdjacencyList.append([node1, node0, HammingDistance(node0, node1)])
    return AdjacencyList

def CountDaughterLabel(countedScores, children, marks, v):
    daughterLabel = ''
    daughterScores = countedScores[children[0]]
    for pos, daughterScore in daughterScores.items():
        parentLetter = marks[v][pos]
        minNucs = [nuc for nuc, val in daughterScore.items() if val == min(daughterScore.values())]
        if parentLetter in minNucs:
            daughterLabel += parentLetter
        else:
            daughterLabel += minNucs[0]
    return daughterLabel

def CountSonLabel(countedScores, children, marks, v):
    sonLabel = ''
    sonScores = countedScores[children[1]]
    for pos, sonScore in sonScores.items():
        parentLetter = marks[v][pos]
        minNucs = [nuc for nuc, val in sonScore.items() if val == min(sonScore.values())]
        if parentLetter in minNucs:
            sonLabel += parentLetter
        else:
            sonLabel += minNucs[0]
    return sonLabel

def ConstructTree(edges, countedScores):
    nodes = [item for sublist in edges for item in sublist]
    nodes = list(set(nodes))
    root = FindRoot(edges, nodes)
    minParsimonyScore = 0
    marks = {}
    marks[root] = ''
    for pos, scores in countedScores[root].items():
        marks[root] += min(scores, key=scores.get)
        minParsimonyScore += min(scores.values())

    already??ounted = {}
    for node in nodes:
        if IsLeaf(node):
            already??ounted[node] = 1
        else:
            already??ounted[node] = 0
    already??ounted[root] = 1

    while 0 in list(already??ounted.values()):
        v, children = NextNodeToInitializeOnes(already??ounted)
        marks[children[0]] = CountDaughterLabel(countedScores, children, marks, v)
        already??ounted[children[0]] = 1
        marks[children[1]] = CountSonLabel(countedScores, children, marks, v)
        already??ounted[children[1]] = 1

    return [CreateAdjacencyList(edges, marks), minParsimonyScore]

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

def NextNodeToInitializeOnes(already??ounted):
    oneNodes = [node for node, isCounted in already??ounted.items() if isCounted == 1]
    for node in oneNodes:
        children = [child for parent, child in edges if parent == node]
        if not IsLeaf(node) and all([already??ounted[child] == 0 for child in children]):
            return node, children

def NextNodeToInitializeZeros(already??ounted):
    zeroNodes = [node for node, isCounted in already??ounted.items() if isCounted == 0]
    for node in zeroNodes:
        children = [child for parent, child in edges if parent == node]
        if all([already??ounted[child] == 1 for child in children]):
            return node, children
        
def InitializeLeafs(S, nodes, already??ounted, lenString):
    for v in nodes:
        S[v] = {}
        already??ounted[v] = 0
        # ???????? v - ?????? ????????
        if IsLeaf(v):
            already??ounted[v] = 1
            for pos in range(lenString):
                S[v][pos] = {}
                symbol = v[pos]
                for nucleotide in Nucleotides:
                    if symbol == nucleotide:
                        S[v][pos][nucleotide] = 0
                    else:
                        S[v][pos][nucleotide] = 1e9
    return S, already??ounted
    
# ?????????????? ???????????????????? ?????????????? S 
# S[v][pos][symb] - ???????????????? ?????? ?????????????? v, ?????? ?????????????? pos ?? ????????????-??????????, 
# ?????? ??????????????, ?????? ?? ?????????????? pos - ???????????? symb
def SmallParsimony(edges):
    already??ounted = {}
    S = {}
    nodes = [node for edge in edges for node in edge]
    nodes = list(set(nodes))
    lenString = LenOfDNAStrings(nodes)
    
    # ???????????? ?? ??????????????, ?????? ?????? ???????????????????????????? scores ???????? 0, ???????? 1e9 (inf)
    S, already??ounted = InitializeLeafs(S, nodes, already??ounted, lenString)
                        
    # ???????????? already??ounted[v] = 0 ?????? ???????? ?????????? v ???????????? ?? already??ounted[v] = 1 ?????? ???????? ???????????? v
    # ???????????????????? ?????????? ?????????????????????? ?? ?????????? ?? ???????????????? ??????????????????
    while 0 in list(already??ounted.values()):
        v, children = NextNodeToInitializeZeros(already??ounted)
        already??ounted[v] = 1
        S[v] = {}
        for pos in range(lenString):
            S[v][pos] = {}
            for nucleotide in Nucleotides:
                # ?????? ?????????????? ??????????????
                possibleScoresDaughter = []
                daughterScore = 0
                for symbol, score in S[children[0]][pos].items():
                    if symbol == nucleotide:
                        possibleScoresDaughter.append(score)
                    else:
                        possibleScoresDaughter.append(score+1)
                # ?????? ?????????????? ??????????????
                possibleScoresSon = []
                sonScore = 0
                for symbol, score in S[children[1]][pos].items():
                    if symbol == nucleotide:
                        possibleScoresSon.append(score)
                    else:
                        possibleScoresSon.append(score + 1)
                S[v][pos][nucleotide] = min(possibleScoresDaughter) + min(possibleScoresSon)
    return S


if __name__ == "__main__":
    #f = f = open('input.txt', 'r')
    #lines = f.read().strip().split("\n")
    #num_leaves = int(lines[0])
    #edges = []

    num_leaves = 4
    edges = [["4", "CAAATCCC"], ["4", "ATTGCGAC"], ["5", "CTGCGCTG"], ["5", "ATGGACGA"], ["6", "4"], ["6", "5"]]
    
    #for row in lines[1:]:
        #temp = row.rstrip().split('->')
        #edges.append(temp)

    countedScores = SmallParsimony(edges)
    final_edges, minParsimonyScore = ConstructTree(edges, countedScores)
    print(minParsimonyScore)
    for edge in final_edges:
        print(str(edge[0]) + '->' + str(edge[1]) + ':' + str(edge[2])) 

 
