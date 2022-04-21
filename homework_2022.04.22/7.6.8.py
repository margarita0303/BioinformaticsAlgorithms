def ClosestClusters(Clusters,D):
    c1, c2 = 0, 0
    l = len(Clusters)
    minDist = 1e10
    for cluster1 in range(0, l):
        for cluster2 in range(0, l):
            if cluster1 == cluster2:
                continue
            dist = 0
            for i in range(0, len(Clusters[cluster1])):
                for j in range(0, len(Clusters[cluster2])): 
                    dist += D[cluster1][cluster2]
            dist = dist / (len(Clusters[cluster1])*len(Clusters[cluster2]))
            if dist < minDist:
                minDist = dist
                c1 = cluster1
                c2 = cluster2
    return c1, c2

def RecountD(D, Clusters, cluster1, cluster2):
    n = len(D)
    newD = D.copy()
    newCluster = cluster1
    for i in range(0, n):
        for j in range(0, n):
            if i == newCluster and j == newCluster:
                newD[i][j] = 0
            elif j == newCluster:
                newD[i][j] = (D[i][cluster1] * len(Clusters[cluster1]) + D[i][cluster2] * len(Clusters[cluster2])) / (len(Clusters[cluster1]) + len(Clusters[cluster2]))
            elif i == newCluster:
                newD[i][j] = (D[cluster1][j] * len(Clusters[cluster1]) + D[cluster2][j] * len(Clusters[cluster2])) / (len(Clusters[cluster1]) + len(Clusters[cluster2]))
    newD.pop(cluster2)
    newD = [newD[i][0:cluster2]+newD[i][cluster2+1:len(newD[i])] for i in range(0,len(newD))]
    Clusters[cluster1] += Clusters[cluster2]
    Clusters.pop(cluster2)
    return newD, Clusters

def FindIndexInAllClusters(Clusters, AllClusters, cluster):
    for i in range(0, len(AllClusters)):
        if AllClusters[i] == Clusters[cluster]:
            return i
    return 0
    
# D = [[0, 3, 4, 3], [3, 0, 4, 5], [4, 4, 0, 2], [3, 5, 2, 0]]

def UPGMA(D, n):
    Clusters = [[i] for i in range(0, n)]
    AllClusters = [[i] for i in range(0, n)]
    T = [[] for i in range(0, n)]
    Age = [0 for i in range(0, n)]
    while len(Clusters) > 1:
        cluster1, cluster2 = ClosestClusters(Clusters, D)
        newCluster = Clusters[cluster1] + Clusters[cluster2]
        AllClusters.append(newCluster)
        T.append([])
        i1 = FindIndexInAllClusters(Clusters, AllClusters, cluster1)
        i2 = FindIndexInAllClusters(Clusters, AllClusters, cluster2)
        T[i1].append(len(T)-1)
        T[i2].append(len(T)-1)
        T[len(T)-1].append(i1)
        T[len(T)-1].append(i2)
        Age.append(D[cluster2][cluster1] / 2)
        D, Clusters = RecountD(D, Clusters, cluster1, cluster2)
    return T, Age


#f = open('task2.txt', 'rt')
#strings = f.read().rstrip().split('\n')
#n = int(strings[0])
#D = [strings[i].split(' ') for i in range(1, len(strings))]
#for i in range(n):
    #for j in range(n):
        #D[i][j] = float(D[i][j])
        
D = [[0, 20, 17, 11], [20, 0, 20, 13], [17, 20, 0, 10], [11, 13, 10, 0]]
n = 4

T, Age = UPGMA(D, n)
for index in range(0, len(T)):
    numbers = T[index]
    for j in range(0, len(numbers)):
        k = 3
        number = numbers[j]
        n1 = str(number)
        n2 = str('%.2f' % abs(Age[index]-Age[number]))
        print(str(index)+"->"+n1+":"+n2)
