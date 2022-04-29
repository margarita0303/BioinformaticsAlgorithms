from math import sqrt

def MaximizingPoint(dataPoints, centers):
    dist = -1
    for point in dataPoints:
        curr = DistFromCenters(point, centers)
        if curr > dist:
            dist = curr
            maxPoint = point
    return maxPoint

def d(p1, p2):
    dist = 0
    for i in range(len(p1)):
        dist += (p1[i] - p2[i]) ** 2
    return sqrt(dist)


def DistFromCenters(point, centers):
    dist = float("Inf")
    for i in centers:
        current = d(i, point)
        if current < dist:
            dist = current
    return dist


def FarthestFirstTraversal(dataPoints, k, m):
    centers = [dataPoints[0]]
    while len(centers) < k:
        point = MaximizingPoint(dataPoints, centers)
        centers.append(point)
    return centers


if __name__ == "__main__":
    f = open('input.txt', 'r')
    input_lines = f.read().strip().split("\n")
    
    k, m = [int(x) for x in input_lines[0].split()]
    data = [[float(x) for x in line.split()] for line in input_lines[1:]]
    
    points = FarthestFirstTraversal(data, k, m)
    
    for center in points:
        print(" ".join(map(str, center)))

 
