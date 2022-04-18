def LimbLengthProblem(n, j, matrix):
    i, k = 0, 0
    minLimbLength = 1e9
    for i1 in range(0, n):
        if i1 == j:
            continue
        for i2 in range(0, n):
            if i2 == j:
                continue
            i, k = i1, i2
            limbLength = 0.5 * (int(matrix[i][j]) + int(matrix[j][k]) - int(matrix[i][k]))
            if limbLength < minLimbLength:
                minLimbLength = limbLength
    return int(minLimbLength)
            
n = 4
j = 1
matrix = [[0, 13, 21, 22], [13, 0, 12, 13], [21, 12, 0, 13], [22, 13, 13, 0]]
print(LimbLengthProblem(n, j, matrix))

f = open('task1.txt', 'rt')
strings = f.read().rstrip().split('\n')
n = int(strings[0])
j = int(strings[1])
matrix = [strings[i].split(' ') for i in range(2, len(strings))]
print(LimbLengthProblem(n, j, matrix)) 
