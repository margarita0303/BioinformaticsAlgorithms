#https://github.com/margarita0303/BioinformaticsAlgorithms/blob/main/homework_2022.04.29/8.8.3.py

from collections import defaultdict
from math import sqrt
import random

def d(p1, p2):
    dist = 0
    for i in range(len(p1)):
        dist += (p1[i] - p2[i]) ** 2
    return sqrt(dist)

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

def GetClustersWithPoints(dataPoints, centers):
    clusters = defaultdict(list)
    for point in dataPoints:
            center = NearestCenter(point, centers)
            clusters[tuple(center)].append(point)
    return clusters

def NewCentersForClusters(clusters, centers):
    currCenters = [[]] * k
    for i in range(k):
        currCenters[i] = NewCenter(clusters[tuple(centers[i])])
    return currCenters
    

def LloydAlgorithm(dataPoints, k, m):
    #заменяю centers = dataPoints[0:k] на:
    centers = kMeansPlusPlusInitializer(dataPoints, k)
    while True:
        clusters = GetClustersWithPoints(dataPoints, centers)
        currCenters = NewCentersForClusters(clusters, centers)
        if currCenters == centers:
            break
        else:
            centers = currCenters[:]
    return centers

# новая функция вычисления вероятностей
def CountProbabilities(Data, Centers):
    probabilities = []
    for point in Data:
        nearestCenter = NearestCenter(point, Centers)
        dist = d(point, nearestCenter)
        probabilities.append(dist ** 2)
    probabilities = [pr / sum(probabilities) for pr in probabilities]
    return probabilities

# новая функция, вычисляющая начальные центры соответствующим алгоритмом
def kMeansPlusPlusInitializer(Data, k):
    randomNum = random.randint(0, len(Data)-1)
    Centers = [Data[randomNum]]
    while len(Centers) < k:
        probabilities = CountProbabilities(Data, Centers)
        DataPoint = random.choices(Data, weights=probabilities, k=1)[0]
        Centers.append(DataPoint)
    return Centers


if __name__ == "__main__":
    #f = open('input.txt', 'r')
    #input_lines = f.read().strip().split("\n")
    
    #k, m = [int(x) for x in input_lines[0].split()]
    #dataPoints = [[float(x) for x in line.split()] for line in input_lines[1:]]
    #centers = LloydAlgorithm(dataPoints, k, m)
    
    k, m = 2, 2
    dataPoints = [[1.3, 1.1], [1.3, 0.2], [0.6, 2.8], [3.0, 3.2], [1.2, 0.7], [1.4, 1.6], [1.2, 1.0], [1.2, 1.1], [0.6, 1.5], [1.8, 2.6], [1.2, 1.3], [1.2, 1.0], [0.0, 1.9]]
    centers = LloydAlgorithm(dataPoints, k, m)
        
    for center in centers:
        string = ""
        for i in center:
            string = string + str(round(i, 3)) + " "
        print(string)
        
        
      
