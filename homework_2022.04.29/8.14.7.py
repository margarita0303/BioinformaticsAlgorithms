import numpy as np

# Псевдокод со степика

# HierarchicalClustering(D, n)
#     Clusters ← n single-element clusters labeled 1, ... , n 
#       construct a graph T with n isolated nodes labeled by single elements 1, ... , n 
#     while there is more than one cluster 
#         find the two closest clusters Ci and Cj 
#         merge Ci and Cj into a new cluster Cnew with |Ci| + |Cj| elements
#         add a new node labeled by cluster Cnew to T
#         connect node Cnew to Ci and Cj by directed edges
#         remove the rows and columns of D corresponding to Ci and Cj
#         remove Ci and Cj from Clusters
#         add a row/column to D for Cnew by computing D(Cnew, C) for each C in Clusters 
#         add Cnew to Clusters 
#     assign root in T as a node with no incoming edges
#     return T

def Closest_i_j(dist, clusters):
    index = np.argmin(dist)
    i, j = index // len(dist), index % len(dist)
    return i, j

def D_avg(i, j, dist, clusters):
    return (dist[i, :] * clusters[i][1] + dist[j, :] * clusters[j][1]) / (clusters[i][1] + clusters[j][1])
    
def NewClusters(n, dist):
        clusters = [[i, 1] for i in range(n)]
        newClusters = []
        g = [[] for _ in range(n)]
        while len(dist) > 1:
            newNode = len(g)
            i, j = Closest_i_j(dist, clusters)
            d_avg = D_avg(i, j, dist, clusters)
            d_avg = np.delete(d_avg, [i, j], 0)
            dist = np.delete(dist, [i, j], 0)
            dist = np.delete(dist, [i, j], 1)
            dist = np.insert(dist, len(dist), d_avg, 0)
            d_avg = np.insert(d_avg, len(d_avg), np.inf, 0)
            dist = np.insert(dist, len(dist)-1, d_avg, 1)
            g.append([clusters[i][0], clusters[j][0]])
            clusters.append([newNode, clusters[i][1] + clusters[j][1]])
            del clusters[max(i, j)]
            del clusters[min(i, j)]
            newClusters.append(NewCluster(g, newNode))
        return newClusters
    
def NewCluster(g, v):
        newCluster = []
        visited = [False for _ in range(len(g))]
        stack = []
        stack.append(v)
        while len(stack) > 0:
            v = stack.pop()
            if 0 == len(g[v]):
                newCluster.append(v + 1)
            if not visited[v]:
                visited[v] = True
                for w in g[v]:
                    stack.append(w)
        return newCluster
    
def HierarchicalClustering(n, dist):
    newClusters = NewClusters(n, dist)
    print('\n'.join([' '.join([str(c) for c in clusters]) for clusters in newClusters]))

if __name__ == "__main__":
    f = open('input.txt', 'r')
    data = f.read().strip().split('\n')
    n = int(data[0])
    dist = np.array([[float(v) for v in d.split()] for d in data[1:]])
    np.fill_diagonal(dist, np.inf)
    
    HierarchicalClustering(n, dist) 
