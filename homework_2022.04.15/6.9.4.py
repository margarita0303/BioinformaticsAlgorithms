
def ParseInput(p_, q_):
    P = ""
    Q = ""
    for i in p_:
        if i == ')':
            P = P + ')' + '*'
        else:
            P = P + i
    for i in q_:
        if i == ')':
            Q = Q + ')' + '*'
        else:
            Q = Q + i
    P = P[0:len(P)-1]
    Q = Q[0:len(Q)-1]
    P = P.split('*')
    Q = Q.split('*')
    
    for i in range(0, len(P)):
        P[i] = P[i][1:len(P[i])-1]
    for i in range(0, len(Q)):
        Q[i] = Q[i][1:len(Q[i])-1]
    
    return P, Q

def Edges(P):
    edges  = []
    for i in P:
        numbers = i.split(' ')
        for j in range(0, len(numbers)):
            if numbers[j][0] == '-':
                numbers[j] = int(numbers[j][1:len(numbers[j])]) * (-1)
            else:
                numbers[j] = int(numbers[j][1:len(numbers[j])])
        numbers.append(numbers[0])
        for i in range(0, len(numbers)-1):
            edges.append([])
            edges[len(edges)-1] = []
            edges[len(edges)-1].append(numbers[i])
            edges[len(edges)-1].append(numbers[i+1]*(-1))
    return edges

def NextNode(edges, node):
    for e in edges:
        if node == e[0]:
            nextnode = e[1]
            break
        elif node == e[1]:
            nextnode = e[0]
            break
    if 'nextnode' in locals():
        edges.remove(e)
        return nextnode
    else:
        return False

def Cycle(egdes1, edges2):
    circles = []
    while egdes1:
        start = egdes1.pop()
        circle = start
        nextnode = NextNode(edges2, start[1])
        circle.append(nextnode)
        while True:
            nextnode = NextNode(egdes1, nextnode)
            if not nextnode:
                break
            else:
                circle.append(nextnode)
            nextnode = NextNode(edges2, nextnode)
            circle.append(nextnode)
        circles.append(circle[:-1])
    return len(circles)
    
def TwoBreakDistanceProblem(P, Q, blocks):
    cycles = 0
    edges1 = Edges(P)
    edges2 = Edges(Q)
    return blocks - Cycle(edges1, edges2)

p_ = "(+1 +2 +3 +4 +5 +6)"
q_ = "(+1 -3 -6 -5)(+2 -4)"
blocks = 0
P, Q = ParseInput(p_, q_)
for i in P:
    blocks += len((i.split(' ')))
print(TwoBreakDistanceProblem(P, Q, blocks))
