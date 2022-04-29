def Closest_i_j(clusters, dist):
    i_, j_ = 0, 0
    minDist = float(1e9)
    for i in range(len(clusters) - 1):
        for j in range(i + 1, len(clusters)):
            currDist = 0
            for i1 in clusters[i]:
                for i2 in clusters[j]:
                    currDist += dist[i1][i2]
            currDist /= (len(clusters[i]) * len(clusters[j]))
            if currDist < minDist:
                minDist = currDist
                i_ = i
                j_ = j
    return i_, j_
    
def HierarchicalClustering(dist):
    clusters = [[i] for i in range(len(dist))]
    newClusters = []
    while len(clusters) != 1:
        i, j = Closest_i_j(clusters, dist)
        newCluster = clusters[i] + clusters[j]
        clusters = [c for c in clusters if c not in [clusters[i], clusters[j]]]
        clusters.append(newCluster)
        newClusters.append(newCluster)
    return newClusters


if __name__ == "__main__":
    f = open('input.txt', 'r')
    data = f.read().strip().split('\n')
    n = int(data[0])

    dist = []
    for i in range(1, len(data)):
        dist.append([float(d) for d in data[i].split(' ')])

    newClusters = HierarchicalClustering(dist)
    for c in newClusters:
        print(' '.join([str(x + 1) for x in c]))
