# 5.6.10
def ManhattanTourist(n, m, down, right):
    s = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        s[i][0] = s[i - 1][0] + down[i-1][0]
    for j in range(1, m + 1):
        s[0][j] = s[0][j - 1] + right[0][j - 1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(s[i][j - 1] + right[i][j - 1], s[i - 1][j] + down[i - 1][j])
    return s[n][m]

# Тест из примера:
n = 4
m = 4 
down = [[1, 0, 2, 4, 3], [4, 6, 5, 2, 1], [4, 4, 5, 2, 1], [5, 6, 8, 5, 3]]
right = [[3, 2, 4, 0], [3, 2, 4, 2], [0, 7, 3, 3], [3, 3, 0, 2], [1, 3, 2, 2]]
print(ManhattanTourist(n, m, down, right))

# Тест на датасете: 
f = open('dataset_5.6.10.txt', 'rt')
string = f.readline().rstrip().split(' ')
n = int(string[0])
m = int(string[1])
down = []
for i in range(0, n):
    string = f.readline().rstrip().split(' ')
    down.append([int(i) for i in string])
f.readline()
right = []
for i in range(0, n+1):
    string = f.readline().rstrip().split(' ')
    right.append([int(i) for i in string])
print(ManhattanTourist(n, m, down, right)) 
