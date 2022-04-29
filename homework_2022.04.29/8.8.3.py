from collections import defaultdict
from math import sqrt

def d(p1, p2):
    dist = 0
    for i in range(len(p1)):
        dist += (p1[i] - p2[i]) ** 2
    return sqrt(dist)

# новый центр соответствует центру тяжести
def NewCenter(cluster):
    center = [0] * len(cluster[0])
    for point in cluster:
        for i in range(len(cluster[0])):
            center[i] += point[i] / len(cluster)
    return center

def NearestCenter(point, centers):
    dist = float(1e9)
    center = centers[0]
    for i in centers:
        current = d(i, point)
        if current < dist:
            dist = current
            center = i
    return center

# назначаем каждую точку данных кластеру
def GetClustersWithPoints(dataPoints, centers):
    clusters = defaultdict(list)
    for point in dataPoints:
            center = NearestCenter(point, centers)
            clusters[tuple(center)].append(point)
    return clusters

# назначаем центр тяжести каждому кластеру
def NewCentersForClusters(clusters, centers):
    currCenters = [[]] * k
    for i in range(k):
        currCenters[i] = NewCenter(clusters[tuple(centers[i])])
    return currCenters
    

def LloydAlgorithm(dataPoints, k, m):
    centers = dataPoints[0:k]
    while True:
        clusters = GetClustersWithPoints(dataPoints, centers)
        currCenters = NewCentersForClusters(clusters, centers)
        # если центры перестали меняться, алгоритм сошелся и можно заканчивать
        if currCenters == centers:
            break
        else:
            centers = currCenters[:]
    return centers


if __name__ == "__main__":
    f = open('input.txt', 'r')
    input_lines = f.read().strip().split("\n")
    
    k, m = [int(x) for x in input_lines[0].split()]
    dataPoints = [[float(x) for x in line.split()] for line in input_lines[1:]]
    centers = LloydAlgorithm(dataPoints, k, m)
    for center in centers:
        print(" ".join(map(str, center))) 
